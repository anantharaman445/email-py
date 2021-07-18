import falcon, json

class FilterEmails(object):
    def on_put(self, req, resp):
        pass

#  https://stoplight.io/blog/python-rest-api/

#  https://stackoverflow.com/questions/35778772/how-to-mark-messages-as-read-using-gmail-api-as-i-parse

api = falcon.API()
filter_endpoint = FilterEmails()
api.add_route('/filteremails', filter_endpoint)