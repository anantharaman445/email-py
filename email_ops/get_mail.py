from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
import base64
from email_ops.get_mail_utils import convert_datetime_to_utc
#  from get_email.get_mail_utils import user_app_token, app_credentials, scopes, convert_datetime_to_utc



def get_emails(user_app_token, app_credentials, SCOPES):

    store = file.Storage(user_app_token)
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets(app_credentials, SCOPES)
        creds = tools.run_flow(flow, store)
    service = build("gmail", "v1", http=creds.authorize(Http()))

    # Call the Gmail API to fetch INBOX
    results = (
        service.users()
        .messages()
        .list(userId="me", labelIds=["INBOX"], maxResults=1)
        .execute()
    )
    messages = results.get("messages", [])

    if not messages:
        pass
        print("No messages found.")
    else:

        for message in messages:
            msg = (
                service.users().messages().get(userId="me", id=message["id"]).execute()
            )

            payload = msg["payload"]

            headers = payload["headers"]
            mail_id = message["id"]
            for header in headers:
                if header["name"] == "Subject":
                    subject = header["value"]
                if header["name"] == "From":
                    from_ad = header["value"]
                if header["name"] == "Date":
                    date = convert_datetime_to_utc(header["value"])
            
            print(subject, from_ad, date)


# if __name__ == "__main__":
#     main(user_app_token, app_credentials, scopes)
