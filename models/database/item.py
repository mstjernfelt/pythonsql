from models.database.sqlserver import sqlserver

"""This module contains the Item class which is a blueprint for creating an item object."""
class Item:
    # A list to store the items
    items = []    
    item_table_name = '[CRONUS Sverige AB$Item$437dbf0e-84ff-417a-965d-ed2bb9650972]'
        
    def __init__(self):
        # Create an instance of SQLServer
        self.sqlserver = sqlserver()
        
        self._timestamp = None  # Initialize timestamp
        self._No_ = None  # Initialize No field
        self._Description = None  # Initialize description
        self._Base_Unit_of_Measure = None # Initialize base unit of measure
        
#region Properties
    @property
    def timestamp(self):
        '''
        Get and set the timestamp of the item.
        '''
        return self._timestamp

    @timestamp.setter
    def timestamp(self, value):
        self._timestamp = value

    @property
    def No_(self):
        '''
        Get and set the No field of the item.
        '''
        return self._No_

    @No_.setter
    def No_(self, value):
        self._No_ = value

    @property
    def Description(self):
        '''
        Get and set the description of the item.
        '''
        return self._Description
    
    @Description.setter
    def Description(self, value):
        self._Description = value
        
    @property
    def Base_Unit_of_Measure(self):
        '''
        Get and set the base unit of measure of the item.
        '''
        return self._Base_Unit_of_Measure
    
    @Base_Unit_of_Measure.setter
    def Base_Unit_of_Measure(self, value):
        # Query the database to check so that the Base_Unit_of_Measure exists in the Unit_of_Measure table
        query = f"SELECT * FROM [CRONUS Sverige AB$Unit of Measure$437dbf0e-84ff-417a-965d-ed2bb9650972] WHERE Code = '{value}'"
        
        # Connect to the SQL Server database
        self.sqlserver.connect()
        
        # Use the SQLServer instance to execute the query
        rows = self.sqlserver.execute_query(query)
        
        # Check if the Base_Unit_of_Measure exists in the Unit_of_Measure table
        if len(rows) == 0:
            raise ValueError(f'The Base_Unit_of_Measure \'{value}\' does not exist in the Unit_of_Measure table.')
        
        self._Base_Unit_of_Measure = value
#endregion

#region Methods
    def findset(self):
        '''
        Fetches the items from the database and populates the items list.
        '''
        query = f'SELECT * FROM {self.item_table_name}'
        
        # Connect to the SQL Server database
        self.sqlserver.connect()
        
        # Use the SQLServer instance to execute the query
        rows = self.sqlserver.execute_query(query)

        # Rest of the code...

        # Clear the items list before populating it
        fetchedItem = Item()
        fetchedItem.items.clear()

        for row in rows:
            fetchedItem = Item()
            
            fetchedItem.validate('timestamp', row[0], False)
            fetchedItem.validate('No_', row[1], False)
            fetchedItem.validate('Description', row[3], False)
            fetchedItem.validate('Base_Unit_of_Measure', row[6], False)
            
            Item.items.append(fetchedItem)

        self.sqlserver.close()

        return Item.items
    
    def validate(self, property_name, value, runtrigger = False):
        '''
        Validates and sets a property.
        '''

        if not hasattr(self, property_name):
            raise AttributeError(f'field {property_name} does not exist in the item object.')

        if not runtrigger:
            # Set the instance variable directly
            setattr(self, '_' + property_name, value)
            return

        # Call the appropriate setter method
        setattr(self, property_name, value)

    # Insert a new item into the database and also check so that the item does not already exist, and also so that Base_Unit_of_Measure exists in the Unit_of_Measure table
    def insert(self):
        '''
        Inserts a new item into the database.
        '''
        query = f"INSERT INTO {self.item_table_name} (No_, Description, [Base Unit of Measure]) VALUES ('{self.No_}', '{self.Description}', '{self.Base_Unit_of_Measure}')"
        
        # Connect to the SQL Server database
        self.sqlserver.connect()
        
        # Use the SQLServer instance to execute the query
        self.sqlserver.execute_query(query)

        self.sqlserver.close()
#endregion