from flask.ext.restful import Api
from .health import Health

from publictitles import app, db

from publictitles.resources import TitleResource

api = Api(app)
api.add_resource(TitleResource, '/titles/<string:title_number>')
Health(app, checks=[db.health])
