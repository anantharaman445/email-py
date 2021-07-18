import psycopg2


class DbConnector:
    def __init__(self):
        self.con = psycopg2.connect(database="ananth", user="ananth", password="ananth", host="127.0.0.1", port="5432")
        self.cur = self.con.cursor()
    
    def close_connection(self):
        self.con.close()
    
    def create_emails_table(self):

        try:
            self.cur.execute('''CREATE TABLE IF NOT EXISTS EMAILS
                                (MAIL_ID TEXT PRIMARY KEY     NOT NULL,
                                SUBJECT           TEXT    NOT NULL,
                                FROM_ADD            INT     NOT NULL,
                                EPOCH        FLOAT);''')
            self.con.commit()
                            
        except Exception as e:
            self.cur.execute("rollback")
            self.cur.execute('''CREATE TABLE IF NOT EXISTS EMAILS
                                (MAIL_ID TEXT PRIMARY KEY     NOT NULL,
                                SUBJECT           TEXT    NOT NULL,
                                FROM_ADD            INT     NOT NULL,
                                EPOCH        FLOAT);''')     
            self.con.commit()
        print("Table verified/created successfully")

db_connector_factory = DbConnector()