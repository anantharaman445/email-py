from operate_email.models import session, Emails
import operator
import json

operator_map = {
    "greater than": operator.gt,
    "less than": operator.lt,
    ">=": operator.ge,
    "<=": operator.le,
    "Equals": operator.eq,
    "Does not Equal": operator.ne,
}

rules = json.load(open("./rules/rules.json"))


def get_records_all(res):
    """
    res :
    {'subject': ['contains', 'Offering Placement'], 'from_address': ['contains', 'info@guvi.in'], 'epoch': 1626738565.55318}

    """
    query = session.query(Emails)
    for attr, value in res.items():
        if attr != "epoch":
            operator = value[0]
            if operator in operator_map:
                query = query.filter(
                    operator_map[operator](getattr(Emails, attr), value[1])
                )
            elif operator == "contains":
                search = "%{}%".format(value[1])
                query = query.filter(getattr(Emails, attr).like(search))

        else:
            query = query.filter(Emails.epoch < value)

    results = query.all()

    return results
