from datetime import datetime
from dateutil import parser as date_parser
from datetime import timezone
from db_utils.db_connector import db_connector_factory


def get_user_email_service(user_app_token):
    return get_user_email_service(user_app_token)


def create_email_table():
    db_connector_factory.create_emails_table()


def end_db_operations():
    db_connector_factory.close_connection()


def insert_records(mail_id, subject, from_add, epoch):
    db_connector_factory.insert_email_records(mail_id, subject, from_add, epoch)


def get_message_by_id(email_service, email_message_id):
    msg = (
        email_service.users().messages().get(userId="me", id=email_message_id).execute()
    )
    return msg


def convert_datetime_to_utc(date_time_str):
    """
    input (str)    : Sun, 18 Jul 2021 15:36:29 +0530 (IST)
    output (float) : 1626622589.0
    """
    date_time = date_parser.parse(date_time_str)
    utc_time = date_time.replace(tzinfo=timezone.utc)
    utc_timestamp_epoch = utc_time.timestamp()
    return utc_timestamp_epoch

# def get_time_delta_days(no_of_days=-1):
#     start_date_time = datetime.now()
#     end_date_time = (start_date_time + timedelta(days=no_of_days))
#     start_epoch = start_date_time.replace(tzinfo=timezone.utc).timestamp()
#     end_epoch = end_date_time.replace(tzinfo=timezone.utc).timestamp()
#     return start_epoch, end_epoch




