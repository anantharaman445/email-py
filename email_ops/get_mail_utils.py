
from datetime import datetime
from dateutil import parser as date_parser
from datetime import timezone
from db_utils.db_connector import db_connector_factory

app_credentials = "./auth/credentials.json"
user_app_token = "./user_token/token.json"
scopes = "https://www.googleapis.com/auth/gmail.readonly"



def convert_datetime_to_utc(date_time_str):
    """
    input (str)    : Sun, 18 Jul 2021 15:36:29 +0530 (IST)
    output (float) : 1626622589.0
    """
    date_time = date_parser.parse(date_time_str)
    utc_time = date_time.replace(tzinfo=timezone.utc)
    utc_timestamp_epoch = utc_time.timestamp()
    return utc_timestamp_epoch
