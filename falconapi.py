import falcon, json
from db_utils.db_connector import  model_connector_factory


class FilterEmails(object):
    def on_put(self, req, resp):
        res = model_connector_factory.get_emails("Security alert")
        for row in res:
            print(res)
        # print(model_connector_factory.get_emails("Security alert"))
        print("test")
        pass

#  https://stoplight.io/blog/python-rest-api/

#  https://stackoverflow.com/questions/35778772/how-to-mark-messages-as-read-using-gmail-api-as-i-parse

api = falcon.API()
filter_endpoint = FilterEmails()
api.add_route('/filteremails', filter_endpoint)