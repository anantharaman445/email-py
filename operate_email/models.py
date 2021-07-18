from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, Integer, String, Float, Text, MetaData, Table
Base=declarative_base()
DB_URI = 'postgresql+psycopg2://ananth:ananth@localhost/ananth_test2'
engine = create_engine(DB_URI, echo=True)

metadata = MetaData()

emails = Table('emails', metadata,
   Column('mail_id', Text, primary_key=True),
   Column('subject', Text),
   Column('from_add', Text),
   Column('epoch', Float)
)

