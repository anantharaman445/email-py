
import base64
from email_ops.get_mail_utils import (
    convert_datetime_to_utc,
    end_db_operations,
    create_email_table,
    insert_records,
    get_email_service
)


def get_emails(user_app_token, maxResults):

    service = get_email_service(user_app_token)

    # Call the Gmail API to fetch INBOX
    results = (
        service.users()
        .messages()
        .list(userId="me", labelIds=["INBOX"], maxResults=maxResults)
        .execute()
    )
    messages = results.get("messages", [])

    if not messages:
        pass
        print("No messages found.")
    else:
        create_email_table()
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
                    from_add = header["value"]
                if header["name"] == "Date":
                    epoch = convert_datetime_to_utc(header["value"])

            insert_records(mail_id, subject, from_add, epoch)

        end_db_operations()
