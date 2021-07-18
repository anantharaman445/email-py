
from flask import Flask
from flask import request,redirect,render_template
from flask_sqlalchemy import SQLAlchemy

from operate_email.models import *


@app.route('/filteremails',methods=['PUT'])
def Categoryform():
    if request.method=='PUT':
        search = "%{}%".format("Security alert")
        emails = Emails.query.filter(Emails.subject.like(search)).all()
        for row in emails:
            print(row.mail_id)
       
    return {}

if __name__ == '__main__':
   app.run(debug=True)
   db.create_all()