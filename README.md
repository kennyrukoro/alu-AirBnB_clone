AirBnB Clone - The Console.
Project Description
This is the first step towards building a full web application: an AirBnB clone. This project implements a command interpreter to manage AirBnB objects, which serves as the foundation for future projects, including HTML/CSS templating, database storage, API development, and front-end integration.

The console provides a simple command-line interface to:

Create new objects (User, State, City, Place, etc.)
Retrieve objects from storage
Perform operations on objects (count, compute stats, etc.)
Update object attributes
Delete objects
Manage object persistence through file storage

Command Interpreter.
The command interpreter is a limited shell designed specifically for managing AirBnB objects. It's built using Python's cmd module and provides an interactive interface for object management.

Use of both interactive and non interactive.

Use on interactive

$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) % Create user
(hbnb) % show user 1010-2020-2222
(hbnb) quit
$


Use on Non Interactive mode like in Shell project in C

$ echo "help" | ./console.py 
(hbnb)

Documented commands (typr help <topic>):
=======================================
EOF help quit
(hbnb)
$

Or using a seperate file
$ cat test_help
help
$

$ cat test_help | ./console.py
(hbnb)

Documented commands (typr help <topic>):
=======================================
EOF help quit
(hbnb)
$

### Available Commands.

| Command | Syntax | Description |
|---------|--------|-------------|
| help | `help [command]` | Display help information |
| quit | `quit` | Exit the program |
| EOF | `EOF` or `Ctrl+D` | Exit the program |
| create | `create <class>` | Create a new instance |
| show | `show <class> <id>` | Display an instance |
| destroy | `destroy <class> <id>` | Delete an instance |
| all | `all [class]` | Display all instances |
| update | `update <class> <id> <attribute> <value>` | Update an instance |


### Examples

#### Creating Objects
```bash 
(hbnb) create BaseModel
49faff9a-6318-451f-87b6-910505c55907
(hbnb) create User
2dd6ef5c-467c-4f82-9521-a772ea7d84e9
```

#### Showing Objects
```bash
(hbnb) show BaseModel 49faff9a-6318-451f-87b6-910505c55907
[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'id': '49faff9a-6318-451f-87b6-910505c55907', 'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'updated_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903300)}
```

#### Updating Objects
```bash
(hbnb) update User 2dd6ef5c-467c-4f82-9521-a772ea7d84e9 first_name "John"
(hbnb) show User 2dd6ef5c-467c-4f82-9521-a772ea7d84e9
[User] (2dd6ef5c-467c-4f82-9521-a772ea7d84e9) {'id': '2dd6ef5c-467c-4f82-9521-a772ea7d84e9', 'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'updated_at': datetime.datetime(2017, 10, 2, 3, 11, 3, 49401), 'first_name': 'John' }
```

#### Listing All Objects
```bash
(hbnb) all BaseModel
["[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'id': '49faff9a-6318-451f-87b6-910505c55907', 'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'updated_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903300)}"]
```

## Project Structure

```
alu-AirBnB_clone/
├── console.py          # Command interpreter
├── models/             # Model classes
│   ├── __init__.py
│   ├── base_model.py   # Base class for all models
│   ├── user.py         # User model
│   ├── state.py        # State model
│   ├── city.py         # City model
│   ├── amenity.py      # Amenity model
│   ├── place.py        # Place model
│   ├── review.py       # Review model
│   └── engine/         # Storage engine
│       ├── __init__.py
│       └── file_storage.py
├── tests/              # Unit tests
│   ├── __init__.py
│   └── test_models/
│       ├── __init__.py
│       ├── test_base_model.py
│       └── test_engine/
│           ├── __init__.py
│           └── test_file_storage.py
├── README.md           # This file
└── AUTHORS             # Contributors list
```

## Classes

The project implements the following classes:

- **BaseModel**: Base class that defines common attributes and methods
- **User**: User information and authentication
- **State**: State/province information
- **City**: City information
- **Amenity**: Available amenities
- **Place**: Property listings
- **Review**: User reviews and ratings

## Storage

The project uses a file-based storage system that:
- Serializes objects to JSON format.
- Saves data to a file (`file.json`).
- Reloads data when the program starts.
- Maintains object relationships and integrity

## Testing

Run all tests:
```bash
$ python3 -m unittest discover tests
```

Run specific test files:
```bash
$ python3 -m unittest tests/test_models/test_base_model.py
```

Run tests in non-interactive mode:
```bash
$ echo "python3 -m unittest discover tests" | bash
```

## Requirements

- Python 3.8.5+
- Ubuntu 20.04 LTS
- pycodestyle 2.7.*
- All files must be executable
- All modules, classes, and functions must be documented

## Installation

1. Clone the repository:
```bash
$ git clone https://github.com/Frankish0014/alu-AirBnB_clone.git
$ cd alu-AirBnB_clone
```

2. Make the console executable:
```bash
$ chmod +x console.py
```

3. Run the console:
```bash
$ ./console.py
```

## Authors

- Frank Ishimwe (f.ishimwe@alustudent.com)
- Kenny Crepin Rukoro (k.rukoro@alustudent.com)