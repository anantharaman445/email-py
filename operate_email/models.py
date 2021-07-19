
from sqlalchemy import orm
from sqlalchemy.ext.declarative import declarative_base
import sqlalchemy as sa

base = declarative_base()
engine = sa.create_engine("postgresql+psycopg2://ananth:ananth@localhost/ananth_test2")
base.metadata.bind = engine
session = orm.scoped_session(orm.sessionmaker())(bind=engine)



class Emails(base):
    __tablename__ = 'emails'
    mail_id = sa.Column(sa.Text, primary_key=True)
    subject = sa.Column(sa.Text)
    from_address = sa.Column(sa.Text)
    from_name = sa.Column(sa.Text)
    epoch = sa.Column(sa.Float)
    from_name = sa.Column(sa.Text)