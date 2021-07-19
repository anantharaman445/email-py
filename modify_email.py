import json
from db_utils.db_connector import db_connector_factory
from email_ops.google_client_services import get_user_email_service, remove_labels, add_labels
from email_ops.get_mail_utils import get_time_delta_days
import sys
from operate_email.models import session, Emails

# or  result = session.query(Customers).filter(or_(Customers.id>2, Customers.name.like('Ra%')))
# and result = session.query(Customers).filter(Customers.id>2, Customers.name.like('Ra%'))

#  "prperties": [
#             {
#                 "field": "from_address",
#                 "predicate": "contains",
#                 "value": "info@guvi.in"
#             },
#             {
#                 "field": "subject",
#                 "predicate": "contains",
#                 "value": "Offering Placement"
#             },
#             {
#                 "field": "epoch",
#                 "predicate": "less than",
#                 "value": "2 days"
#             }
#         ],
#         "predicate": "all",
#         "action": {
#             "move_message": "inbox",
#             "mark_as": "read"
#         }
rules = json.load(open('./rules/rules.json'))

def get_rule(rule_no):
    return rules[rule_no]

def parse_rule(rule):
    properties = rule["properties"]
    pass

def get_records(predicate, subject, from_address, start_epoch, end_epoch):
    pass
   
   
   
    search = "%{}%".format("Offering Placement promising")
    # user = User.query.filter((User.email == email) | (User.name == name)).first()
    emails = session.query(Emails).filter(Emails.subject.like(search), ).all()
    print(emails)
    for row in emails:
        
        print(row.mail_id)
    pass

if __name__ == '__main__':
    # test_models()
    rule_no = sys.argv[1]
    rule_no = "Rule" + rule_no
    