from flask import Flask
from flask import request,redirect,render_template
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://ananth:ananth@localhost/ananth_test2'
db=SQLAlchemy(app)


class Emails(db.Model):
    
    mail_id = db.Column(db.Text, primary_key=True)
    subject = db.Column(db.Text)
    from_add = db.Column(db.Text)
    epoch = db.Column(db.Float)
    from_name = db.Column(db.Text)