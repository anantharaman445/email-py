
from email_ops.get_email_ops import get_emails
user_app_token = "./user_token/token.json"

# maxResults is the number of emails the user wanted to fetch at a time. out customised default value is 2
get_emails(user_app_token, maxResults=10)