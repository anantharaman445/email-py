from datetime import datetime
from dateutil import parser as date_parser
from datetime import timezone
from db_utils.db_connector import db_connector_factory
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools


app_credentials = "./auth/credentials.json"


scopes = [
    "https://www.googleapis.com/auth/gmail.readonly",
    "https://www.googleapis.com/auth/gmail.modify",
]


def get_email_service(user_app_token):
    store = file.Storage(user_app_token)
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets(app_credentials, scopes)
        creds = tools.run_flow(flow, store)
    service = build("gmail", "v1", http=creds.authorize(Http()))
    return service


def convert_datetime_to_utc(date_time_str):
    """
    input (str)    : Sun, 18 Jul 2021 15:36:29 +0530 (IST)
    output (float) : 1626622589.0
    """
    date_time = date_parser.parse(date_time_str)
    utc_time = date_time.replace(tzinfo=timezone.utc)
    utc_timestamp_epoch = utc_time.timestamp()
    return utc_timestamp_epoch


def create_email_table():
    db_connector_factory.create_emails_table()


def end_db_operations():
    db_connector_factory.close_connection()


def insert_records(mail_id, subject, from_add, epoch):
    db_connector_factory.insert_email_records(mail_id, subject, from_add, epoch)


def mark_email_unread(email_service, email_message_id):
    modified_msg = (
        email_service.users()
        .messages()
        .modify(userId="me", id=email_message_id, body={"removeLabelIds": ["UNREAD"]})
        .execute()
    )

    return modified_msg


def get_message_by_id(email_service, email_message_id):
    msg = (
        email_service.users().messages().get(userId="me", id=email_message_id).execute()
    )
    return msg
