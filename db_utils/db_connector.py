import psycopg2


class DbConnector:
    def __init__(self):
        self.con = psycopg2.connect(database="ananth", user="ananth", password="ananth", host="127.0.0.1", port="5432")
    
    def close_connection(self):
        self.con.close()
    

db_connector_factory = DbConnector()