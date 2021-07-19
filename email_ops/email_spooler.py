
import base64
from email_ops.get_mail_utils import (
    convert_datetime_to_utc,
    end_db_operations,
    create_email_table,
    insert_records,
)

from email_ops.google_client_services import get_user_email_service , get_message_by_id, get_inbox_emails

def get_emails(user_app_token, maxResults):
    """
    This function does 
    1. get the auth service from google api
    2. get the emails based on the user's auth
    3. push each row to the db(before the upsert function will create table emails if it is not there)
    """

    service = get_user_email_service(user_app_token)

    # Call the Gmail API to fetch INBOX
    results = get_inbox_emails(maxResults, service)

    messages = results.get("messages", [])

    # create / check if the table exists
    create_email_table()
    
    for message in messages:
        msg = get_message_by_id(service, message["id"])
        payload = msg["payload"]

        headers = payload["headers"]
        mail_id = message["id"]
        for header in headers:
            if header["name"] == "Subject":
                subject = header["value"]
            if header["name"] == "From":
                value = header["value"].split()
                from_add = value[-1]
                value.remove(value[-1])
                print(value)
                from_name = " ".join(value)
            if header["name"] == "Date":
                epoch = convert_datetime_to_utc(header["value"])

        insert_records(mail_id, subject, from_add, from_name, epoch)

    end_db_operations()
