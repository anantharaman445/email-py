
from flask import Flask
from flask import request,redirect,render_template
from flask_sqlalchemy import SQLAlchemy

from operate_email.models import *
from email_ops.google_client_services  import get_user_email_service, add_labels


@app.route('/filteremails',methods=['PUT'])
def filterEmails():
    
    if request.method=='PUT':
        user_app_token = "./user_token/token.json"
        email_service = get_user_email_service(user_app_token)
        search = "%{}%".format("The scan of 15 repositories uncovered secrets")
        emails = Emails.query.filter(Emails.subject.like(search)).all()
        for row in emails:
            add_labels(email_service, row.mail_id)
       
    return {}

if __name__ == '__main__':
   app.run(debug=True)
   db.create_all()