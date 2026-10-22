import psycopg2

class PGDatabase:
    def __init__(self, host, port, database, user, password):
        self.connection = psycopg2.connect(
            host=host,
            port=port,
            database=database,
            user=user,
            password=password,
        )
        self.connection.autocommit = True
        self.cursor = self.connection.cursor()

    def post(self, query, args=()):
        self.cursor.execute(query, args)

    def close(self):
        self.connection.close()