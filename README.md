AirBnB Clone - Console (HBNB)
Project Overview

This project is the first step of the AirBnB clone. It focuses on building a command-line interpreter (hbnb) to manage AirBnB-like objects in Python. The interpreter allows you to create, update, show, and destroy objects, and persist them using JSON storage.

This project lays the foundation for later steps including web front-end, database integration, and API development.

Features

Command-line Interpreter using the cmd module

BaseModel class to handle:

Unique id using uuid4

created_at and updated_at timestamps

Serialization and deserialization via dictionaries and JSON

User class inheriting from BaseModel with attributes:

email, password, first_name, last_name

FileStorage engine to save and reload objects from file.json

Interactive commands:

create <ClassName> – creates a new instance and prints its ID

show <ClassName> <id> – prints the string representation of an object

destroy <ClassName> <id> – deletes an object

all [ClassName] – prints all objects, optionally filtered by class

update <ClassName> <id> <attribute> "<value>" – updates an object’s attribute

quit or EOF – exits the interpreter

Non-interactive mode works with piped commands

Getting Started
Requirements

Python 3.8+

Ubuntu 20.04 LTS (recommended)

PEP8 compliant code

Project Structure
AirBnB_clone/
│
├── console.py               # Entry point for command interpreter
├── models/
│   ├── __init__.py          # Creates storage instance
│   ├── base_model.py        # BaseModel class
│   ├── user.py              # User class
│   └── engine/
│       ├── __init__.py
│       └── file_storage.py  # FileStorage class
├── tests/                   # Unit tests for all classes
├── file.json                # JSON storage file (generated at runtime)
├── README.md                # This file
└── AUTHORS                  # Contributors

How to Use
Launching the Console

Interactive mode:

$ ./console.py
(hbnb)


Non-interactive mode:

$ echo "help" | ./console.py

Example Commands
(hbnb) create BaseModel
# Returns: 1234-5678-9012-3456

(hbnb) show BaseModel 1234-5678-9012-3456
# Returns: [BaseModel] (1234-5678-9012-3456) {'id': '1234-5678-9012-3456', 'created_at': ..., 'updated_at': ...}

(hbnb) update BaseModel 1234-5678-9012-3456 name "Alice"

(hbnb) all BaseModel
# Returns: ["[BaseModel] (1234-5678-9012-3456) {...}"]

(hbnb) destroy BaseModel 1234-5678-9012-3456

(hbnb) quit


Note: All changes are persisted automatically in file.json.

Running Tests

All classes and functionality are unit tested using unittest.

Run all tests:

$ python3 -m unittest discover tests


Run a specific test file:

$ python3 -m unittest tests/test_models/test_base_model.py

Authors

Ariane ITETERO