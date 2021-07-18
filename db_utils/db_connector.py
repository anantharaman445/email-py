import psycopg2


class DbConnector:
    def __init__(self):
        self.con = psycopg2.connect(
            database="ananth_test2",
            user="ananth",
            password="ananth",
            host="127.0.0.1",
            port="5432",
        )
        self.cur = self.con.cursor()

    def close_connection(self):
        self.con.close()

    def create_emails_table(self):

        try:
            self.cur.execute(
                """CREATE TABLE IF NOT EXISTS EMAILS
                                (MAIL_ID TEXT PRIMARY KEY     NOT NULL,
                                SUBJECT           TEXT    NOT NULL,
                                FROM_ADD            TEXT     NOT NULL,
                                EPOCH        FLOAT);"""
            )
            self.con.commit()

        except Exception as e:
            self.cur.execute("rollback")
            self.cur.execute(
                """CREATE TABLE IF NOT EXISTS EMAILS
                                (MAIL_ID TEXT PRIMARY KEY     NOT NULL,
                                SUBJECT           TEXT    NOT NULL,
                                FROM_ADD            TEXT     NOT NULL,
                                EPOCH        FLOAT);"""
            )
            self.con.commit()
        print("Table verified/created successfully")

    def insert_email_records(self, mail_id, subject, from_add, epoch):
        try:
            insert_str = "INSERT INTO EMAILS(MAIL_ID,SUBJECT,FROM_ADD,EPOCH) VALUES ('{}' , '{}', '{}' , '{}') ON CONFLICT (mail_id) DO NOTHING".format(
                    mail_id, subject, from_add, epoch
                )
            self.cur.execute(insert_str)
            self.con.commit()
            print("email {} inerted successfully".format(mail_id))
        except Exception as e:
            print(e)
            


db_connector_factory = DbConnector()
