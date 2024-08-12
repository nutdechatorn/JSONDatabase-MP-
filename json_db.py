"""
JSONDatabase Library for MicroPython
------------------------------------

A lightweight JSON-based database library for MicroPython. This library allows
you to store, retrieve, update, and delete records in a JSON file, simulating
a simple database.

Author: Nutdechatorn P.

Usage:
    - Insert records into a table
    - Retrieve records with optional filtering
    - Update records based on a query
    - Delete records based on a query
    - Show the contents of a specific table or all tables
    - Save the database to a file

"""

import json
import uos

class JSONDatabase:
    def __init__(self, db_file="data.json"):
        """
        Initialize the JSONDatabase class.

        Parameters:
        db_file (str): The name of the JSON file to be used as the database.
                       If the file does not exist, it will be created.

        The database is loaded into memory from the specified JSON file.
        """
        self.db_file = db_file
        self._db = self._load_database()  # Load the database into memory

    def _load_database(self):
        """
        Load the database from the JSON file.

        Returns:
        dict: The database content as a dictionary.

        If the file does not exist, an empty dictionary is returned.
        """
        try:
            with open(self.db_file, 'r') as file:
                return json.load(file)
        except OSError:
            # If the file doesn't exist, return an empty dictionary
            return {}

    def _save_database(self):
        """
        Save the current state of the database to the JSON file.

        This method writes the in-memory database back to the JSON file.
        """
        with open(self.db_file, 'w') as file:
            json.dump(self._db, file)

    def save_database(self):
        """
        Public method to save the database to the JSON file.

        This method can be called to manually save the database after multiple
        changes have been made.
        """
        self._save_database()

    def insert_record(self, table, record):
        """
        Insert a new record into a specific table.

        Parameters:
        table (str): The name of the table where the record should be inserted.
        record (dict): The record data as a dictionary.

        If the table does not exist, it will be created.
        """
        if table not in self._db:
            self._db[table] = []
        
        self._db[table].append(record)

    def get_records(self, table, query=None):
        """
        Get records from a specific table, optionally filter with a query.

        Parameters:
        table (str): The name of the table to retrieve records from.
        query (dict): A dictionary specifying the query for filtering records.

        Returns:
        list: A list of records that match the query. If no query is provided,
              all records from the table are returned.
        """
        if table not in self._db:
            return []
        
        if query is None:
            return self._db[table]
        
        # Filter records based on the query
        return [record for record in self._db[table] if all(record.get(k) == v for k, v in query.items())]

    def update_record(self, table, query, updates):
        """
        Update records in a specific table based on a query.

        Parameters:
        table (str): The name of the table where the records should be updated.
        query (dict): A dictionary specifying the query for selecting records.
        updates (dict): A dictionary containing the fields to be updated.

        Returns:
        bool: True if any records were updated, False otherwise.
        """
        if table not in self._db:
            return False
        
        updated = False
        for record in self._db[table]:
            if all(record.get(k) == v for k, v in query.items()):
                record.update(updates)
                updated = True
        
        return updated

    def delete_records(self, table, query):
        """
        Delete records in a specific table based on a query.

        Parameters:
        table (str): The name of the table where the records should be deleted.
        query (dict): A dictionary specifying the query for selecting records.

        Returns:
        bool: True if any records were deleted, False otherwise.
        """
        if table not in self._db:
            return False
        
        original_length = len(self._db[table])
        self._db[table] = [record for record in self._db[table] if not all(record.get(k) == v for k, v in query.items())]
        
        return len(self._db[table]) < original_length

    def show_table(self, table=None):
        """
        Print the contents of a specific table or all tables in a readable format.

        Parameters:
        table (str): The name of the table to display. If None or "all", all tables
                     in the database will be displayed.

        This method is useful for inspecting the contents of the database during
        development or debugging.
        """
        if table is None or table == "all":
            # Show all tables
            for tbl_name in self._db:
                print(f"\nTable '{tbl_name}':")
                records = self._db[tbl_name]
                if not records:
                    print("  (Empty)")
                else:
                    for i, record in enumerate(records, start=1):
                        print(f"  Record {i}: {record}")
        else:
            # Show a specific table
            if table not in self._db:
                print(f"Table '{table}' does not exist.")
                return
            
            records = self._db[table]
            if not records:
                print(f"Table '{table}' is empty.")
                return

            print(f"Table '{table}':")
            for i, record in enumerate(records, start=1):
                print(f"Record {i}: {record}")
