# Item Module Documentation
This repository contains the Item class which serves as a blueprint for creating and managing item objects. The class is designed to interface with a SQL Server database to perform various operations related to items.

## Class: Item
### Description
The Item class provides methods to interact with items in the SQL Server database. It supports creating, retrieving, validating, and inserting items.

### Attributes
items: A class-level list that stores all item instances.
item_table_name: The name of the table in the SQL Server database where items are stored.
### Constructor
__init__()
Initializes an instance of the Item class.
Creates an instance of the sqlserver class.
Initializes item attributes (timestamp, No_, Description, Base_Unit_of_Measure) to None.
### Properties
timestamp: Get and set the timestamp of the item.
No_: Get and set the No field of the item.
Description: Get and set the description of the item.
Base_Unit_of_Measure: Get and set the base unit of measure of the item. Validates the unit of measure against the database.
Methods
findset()
Fetches all items from the database and populates the items list.

Returns: A list of Item instances representing the fetched items.
validate(property_name, value, runtrigger=False)
Validates and sets a property value.

Parameters:

property_name (str): The name of the property to validate.
value: The value to set.
runtrigger (bool): If True, calls the setter method; otherwise, sets the instance variable directly.
Raises: AttributeError if the property does not exist.

insert()
Inserts a new item into the database.

Note: Ensures the item does not already exist and validates the Base_Unit_of_Measure.
### Usage Example
```
from models.database.sqlserver import sqlserver

# Create a new item instance
item = Item()

# Set item properties
item.No_ = "12345"
item.Description = "Sample Item"
item.Base_Unit_of_Measure = "PCS"

# Insert the new item into the database
item.insert()

# Fetch and display all items
all_items = Item().findset()
for i in all_items:
    print(f"Item No: {i.No_}, Description: {i.Description}, Base Unit: {i.Base_Unit_of_Measure}")
```

### Dependencies
sqlserver module: Provides database connection and query execution functionalities.
## License
This project is licensed under the MIT License.