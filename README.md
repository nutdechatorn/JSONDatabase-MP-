# JSONDatabase-MP-
JSONDatabase Library for MicroPython
The JSONDatabase library is a lightweight, easy-to-use database solution for MicroPython projects. It stores data in JSON format, making it ideal for small-scale projects on microcontrollers like the ESP32.

Features
Insert Records: Add new records to any table.
Retrieve Records: Fetch records from a table, optionally filtering by criteria.
Update Records: Modify existing records in a table based on a query.
Delete Records: Remove records from a table based on a query.
Show Tables: Display the contents of a specific table or all tables in the database.
Save Database: Manually save the database to a JSON file.
Installation
Upload the json_db.py file to your MicroPython device using a tool like mpremote, ampy, or your IDE.

bash
Copy code
mpremote cp json_db.py :/lib/json_db.py
How to Use the Library
1. Initialization
First, you need to initialize the JSONDatabase class, which loads the database from a JSON file. If the file does not exist, it creates an empty database.

```
from json_db import JSONDatabase

# Initialize the database
db = JSONDatabase("my_data.json")

```

2. Insert Records
Use the insert_record method to add a new record to a specific table.

Example:

```
db.insert_record("users", {"id": 1, "name": "John Doe", "email": "john@example.com"})
db.insert_record("users", {"id": 2, "name": "Jane Doe", "email": "jane@example.com"})
```


This will insert two records into the users table.



3. Retrieve Records
Use the get_records method to fetch records from a table. You can retrieve all records or filter them based on specific criteria.

Retrieve All Records:

```
all_users = db.get_records("users")
print(all_users)
```
Retrieve Records with a Query:

```
jane_doe = db.get_records("users", {"name": "Jane Doe"})
print(jane_doe)
```

4. Update Records
Use the update_record method to modify existing records in a table. You specify the query to find the record and provide the updates.

Example:

```
db.update_record("users", {"id": 1}, {"email": "john.doe@example.com"})
```

This will update the email of the user with id 1.

5. Delete Records
Use the delete_records method to remove records from a table. You specify the query to find the records to delete.

Example:

```

db.delete_records("users", {"id": 2})

```

This will delete the user with id 2.

6. Show Table Contents
Use the show_table method to print the contents of a specific table or all tables in the database.

Show a Specific Table:

```
db.show_table("users")
```

Show All Tables:

```
db.show_table()

```
7. Save Database
Use the save_database method to manually save the current state of the database to the JSON file. This is useful if you've made multiple changes and want to save them all at once.

Example:

```
db.save_database()

```
8. Load Database Automatically
The JSONDatabase class automatically loads the database from the JSON file when you initialize it. There's no need to call a separate load function.

Example Usage
Here's a complete example of using the JSONDatabase library:

```
from json_db import JSONDatabase

# Initialize the database
db = JSONDatabase("my_data.json")

# Insert records into the "users" table
db.insert_record("users", {"id": 1, "name": "John Doe", "email": "john@example.com"})
db.insert_record("users", {"id": 2, "name": "Jane Doe", "email": "jane@example.com"})

# Retrieve and print all users
users = db.get_records("users")
print("All users:", users)

# Update a user's email
db.update_record("users", {"id": 1}, {"email": "john.doe@example.com"})

# Delete a user
db.delete_records("users", {"id": 2})

# Show all tables
db.show_table()

# Save the database
db.save_database()

```

License
This project is licensed under the MIT License.

Contributing
Feel free to submit issues or pull requests if you have any improvements or suggestions!

Contact
For any questions or comments, please reach out at nutdechatorn@gmail.com
