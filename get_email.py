from email_ops.get_mail_utils import user_app_token, app_credentials, scopes
from email_ops.get_email_ops import get_emails

# maxResults is the number of emails the user wanted to fetch at a time. out customised default value is 1
get_emails(user_app_token, app_credentials, scopes, maxResults=1)