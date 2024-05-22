from models.database.sqlserver import sqlserver

"""This module contains the Item class which is a blueprint for creating an item object."""
class Item:
    def __init__(self, timestamp, No_, No_2, Description, Search_Description, Description_2, Base_Unit_of_Measure, Price_Unit_Conversion, Type, Inventory_Posting_Group):
        self.timestamp = timestamp
        self.No_ = No_
        self.No_2 = No_2
        self.Description = Description
        self.Search_Description = Search_Description
        self.Description_2 = Description_2
        self.Base_Unit_of_Measure = Base_Unit_of_Measure
        self.Price_Unit_Conversion = Price_Unit_Conversion
        self.Type = Type
        self.Inventory_Posting_Group = Inventory_Posting_Group
        self.sqlserver = sqlserver(sqlserver('slp', 'CRONUS', 'admin', 'Bright2021!'))  # Create an instance of SQLServer

    def findset(self):
        query = 'SELECT * FROM [CRONUS Sverige AB$Item$437dbf0e-84ff-417a-965d-ed2bb9650972]'
        rows = self.sqlserver.execute_query(query)  # Use the SQLServer instance to execute the query

        # Rest of the code...

        # Clear the items list before populating it
        Item.items.clear()

        for row in rows:
            item = Item(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9])
            Item.items.append(item)

        self.sqlserver.close()

        return Item.items

    @classmethod
    def items(cls):
        return cls.items        