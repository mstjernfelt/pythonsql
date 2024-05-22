import pyodbc

class sqlserver:
    """
    This class is responsible for connecting to a SQL Server database and executing queries.
    """

    def __init__(self, server, database, username, password):
        """
        The constructor for SQLServerConnector class.

        Parameters:
            server (str): The server name.
            database (str): The database name.
            username (str): The username for the database.
            password (str): The password for the database.
        """
        self.server = server
        self.database = database
        self.username = username
        self.password = password
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

        # Fetch all rows from the executed query
        rows = self.cursor.fetchall()

        return rows

    def close(self):
        """
        Closes the connection to the SQL Server database.
        """
        # Close the connection
        self.conn.close()
