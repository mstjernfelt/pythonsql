import os

class database:
    def __init__(self):
        if os.getenv('ENV') == 'prod':
            from models.system.prod_settings import ProdSettings
            
            self.server_name = ProdSettings.server_name
            self.database = ProdSettings.database
            self.username = ProdSettings.username
            self.password = ProdSettings.password
        else:
            from models.system.test_settings import TestSettings
            
            self.server_name = TestSettings.server_name
            self.database = TestSettings.database
            self.username = TestSettings.username
            self.password = TestSettings.password
        
    @property
    def server_name(self):
        '''
        Get and set the database setting.
        '''
        return self._server_name
    
    @server_name.setter
    def server_name(self, value):
        self._server_name = value
        
    @property
    def database(self):
        '''
        Get and set the database of the item.
        '''
        return self._database
    
    @database.setter
    def database(self, value):
        self._database = value
        
    @property
    def username(self):
        '''
        Get and set the username of the item.
        '''
        return self._username
    
    @username.setter
    def username(self, value):
        self._username = value
        
    @property
    def password(self):
        '''
        Get and set the password of the item.
        '''
        return self._password
    
    @password.setter
    def password(self, value):
        self._password = value 