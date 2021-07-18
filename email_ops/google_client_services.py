app_credentials = "./auth/credentials.json"


scopes = [
    "https://www.googleapis.com/auth/gmail.readonly",
    "https://www.googleapis.com/auth/gmail.modify",
]

from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools


def get_user_email_service(user_app_token):
    store = file.Storage(user_app_token)
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets(app_credentials, scopes)
        creds = tools.run_flow(flow, store)
    service = build("gmail", "v1", http=creds.authorize(Http()))
    return service

def get_inbox_emails(maxResults, email_service):
    results = (
        email_service.users().messages()
        .list(userId="me", labelIds=["INBOX"], maxResults=maxResults)
        .execute()
        )
    return results
    
def get_message_by_id(email_service, email_message_id):
    msg = (
        email_service.users().messages().get(userId="me", id=email_message_id).execute()
    )
    return msg


def remove_labels(email_service, email_message_id, label_value = ["UNREAD"]):
    modified_msg = (
        email_service.users()
        .messages()
        .modify(userId="me", id=email_message_id, body={"removeLabelIds": label_value})
        .execute()
    )

    return modified_msg

def add_labels(email_service, email_message_id, label_value = ["UNREAD"]):
    modified_msg = (
        email_service.users()
        .messages()
        .modify(userId="me", id=email_message_id, body={"addLabelIds": label_value})
        .execute()
    )

    return modified_msg