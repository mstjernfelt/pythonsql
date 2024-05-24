import pyodbc
from models.system import settings


class sqlserver:
    """
    This class is responsible for connecting to a SQL Server database and executing queries.
    """
    # Load the settings from the config.json file
    config = settings.load_settings()

    def __init__(self):
        """
        The constructor for SQLServerConnector class.
        """
        self.server = self.config.server_name
        self.database = self.config.server_name
        self.username = self.config.username
        self.password = self.config.password
        self.driver = self.config.driver

    def connect(self):
        """
        Connects to the SQL Server database using the provided server, database, username, and password.
        """
        # Create the connection string
        connection_string = f'DRIVER={self.driver};SERVER={self.server};DATABASE={
            self.database};UID={self.username};PWD={self.password}'

        # Create the connection
        self.conn = pyodbc.connect(connection_string)

        # Create a cursor from the connection
        self.cursor = self.conn.cursor()

    def execute_query(self, query):
        """
        Executes a SQL query on the connected database.

        Parameters:
            query (str): The SQL query to execute.

        Returns:
            list: A list of rows returned by the query.
        """
        # Execute the query
        self.cursor.execute(query)

        # Check if the query is a SELECT query
        if query.strip().upper().startswith('SELECT'):
            # Fetch all rows
            rows = self.cursor.fetchall()
            return rows
        else:
            # Commit the changes
            self.cursor.commit()
            return None

    def close(self):
        """
        Closes the connection to the SQL Server database.
        """
        # Close the connection
        self.conn.close()
