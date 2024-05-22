from models.database.table.item import Item

# Fetch items from the database
myItems = Item()

#myItems.findset()

myItems.validate('No_', '999999', True)
myItems.validate('Description', 'Test Item', True)
myItems.validate('Base_Unit_of_Measure', 'styck', True)

myItems.insert()

# Add a loop to print items
for item in Item.items:
    print(item.No_, item.Description, item.Base_Unit_of_Measure)