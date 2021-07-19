import json
from email_ops.google_client_services import (
    get_user_email_service,
    remove_labels,
    add_labels,
)
from email_ops.get_mail_utils import get_time_delta_days
import sys
from operate_email.query_generator import operator_map, rules, get_records_all, get_records_any


def get_rule(rule_no):
    return rules[rule_no]


def parse_rule(rule):

    rule = get_rule(rule)

    properties = rule["properties"]
    predicate = rule["predicate"]
    action = rule["action"]
    prop_dict = {}
    for prop in properties:

        prop_dict[prop["field"]] = []

        prop_dict[prop["field"]].append(prop["predicate"])
        prop_dict[prop["field"]].append(prop["value"])

    return prop_dict, predicate, action


def get_props(rule):
    """
    prop_dict = {'from_address': ['contains', 'info@guvi.in'], 'subject': ['contains', 'Offering Placement'], 'epoch': ['less than', '2 days']}
    """
    prop_dict, predicate, action = parse_rule(rule)
    subject = prop_dict["subject"]
    from_address = prop_dict["from_address"]
    epoch = prop_dict["epoch"]
    epoch_split = epoch[1].split()

    if epoch_split[1] == "months":
        days = int(epoch_split[0]) * 30
    else:
        days = int(epoch_split[0])

    if epoch[0] == "less than":
        days = days * (-1)
        epoch_start, epoch_end = get_time_delta_days(days)
    else:
        epoch_start, epoch_end = get_time_delta_days(days)
    res = dict(subject=subject, from_address=from_address, epoch=epoch_start)
    return res, predicate, action


def modify_email(rule):
    res_dict, predicate, action = get_props(rule)
    
    if predicate == "all":
        rows = get_records_all(res_dict)
    elif predicate == "any":
        rows = get_records_any(res_dict)
    
    user_app_token = "./user_token/token.json"
    
    email_service = get_user_email_service(user_app_token)
    
    for row in rows:
        if action["mark_as"] == "read":
            remove_labels(email_service, row.mail_id)
        elif action["mark_as"] == "un_read":
            add_labels(email_service, row.mail_id)


if __name__ == "__main__":
    rule_no = sys.argv[1]
    rule_no = "Rule" + rule_no
    modify_email(rule_no)
