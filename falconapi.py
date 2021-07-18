import falcon, json

class FilterEmails(object):
    def on_put(self, req, resp):
        pass


api = falcon.API()
filter_endpoint = FilterEmails()
api.add_route('/filteremails', filter_endpoint)