from flask.ext.restful import Api

from publictitles import app

from publictitles.resources import TitleResource

api = Api(app)
api.add_resource(TitleResource, '/titles/<string:title_number>')
