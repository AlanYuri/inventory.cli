# CLI Inventory System

A simple inventory management system developed in Python using a Command-Line Interface (CLI).

## Features

* Register new equipment
* Automatically assign unique IDs
* Store equipment information in memory
* List all registered equipment
* Simple and user-friendly menu navigation

## Project Structure

```python
inventory = []

def show_menu():
    ...

def register_equipment():
    ...

def listing_equipments():
    ...
```

## Requirements

* Python 3.8 or higher

## How to Run

1. Clone the repository:

```bash
git clone https://github.com/AlanYuri/cli-inventory-system.git
```

2. Navigate to the project folder:

```bash
cd cli-inventory-system
```

3. Run the application:

```bash
python main.py
```

## Menu Options

### 1 - Register New Equipment

Allows the user to register a new device by providing:

* Device name
* IP address
* Status (Active/Inactive)

Example:

```text
Name of device: Router01
IP Address: 192.168.0.1
Status: Active
```

### 2 - List Equipments

Displays all registered equipment in the following format:

```text
Id: 1 | Name: Router01 | Ip: 192.168.0.1 | Status: Active
```

### 3 - Logoff

Closes the application safely.

## Example Usage

```text
==============================
 CLI Inventory System
==============================
1 - Register new equipment
2 - List equipments
3 - Logoff
==============================
Choose an option: 1

--- Register Equipment ---
Name of device: Firewall01
IP Address: 10.0.0.1
Status: Active

[Success] 'Firewall01' successfully registered!
```

## Future Improvements

* Edit equipment information
* Remove equipment
* Search by ID or name
* Save data to a JSON file
* Database integration (SQLite/MySQL)
* Input validation for IP addresses
* User authentication

## Technologies Used

* Python 3
* Command-Line Interface (CLI)

## License

This project is open-source and available under the MIT License.
