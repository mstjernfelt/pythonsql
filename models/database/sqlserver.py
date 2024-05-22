import pyodbc
from models.system import database


class sqlserver:
    """
    This class is responsible for connecting to a SQL Server database and executing queries.
    """

    settings = database.database()

    def __init__(self):
        """
        The constructor for SQLServerConnector class.

        Parameters:
            server (str): The server name.
            database (str): The database name.
            username (str): The username for the database.
            password (str): The password for the database.
        """
        self.server = self.settings.server_name
        self.database = self.settings.database
        self.username = self.settings.username
        self.password = self.settings.password
        self.driver = '{ODBC Driver 17 for SQL Server}'

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
