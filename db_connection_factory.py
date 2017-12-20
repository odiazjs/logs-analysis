import psycopg2
# create a database connection
# in the right order as such :
# 1. new DbConnectionFactory('dbname')
# 2. connect()
# 3. executeQuery(query)
class DbConnectionFactory():
    def __init__(self, dbname):
        self._dbname = dbname
        self._connect()

    # Create a connection and
    # stablish a pointer cursor to the db
    def _connect(self):
        self.db = psycopg2.connect(database=self._dbname)
        self.cursor = self.db.cursor()

    # Pass in and execute any
    # given sql query statement
    def executeQuery(self, query):
        self.cursor.execute(query)
        return self.cursor