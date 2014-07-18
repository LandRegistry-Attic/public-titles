from flask.ext.restful import Resource, fields, marshal_with, abort, reqparse

from publictitles.models import Title
from publictitles import app, db

class TitleResource(Resource):

    resource_fields = { 'title_number':   fields.String,
                                    'house_number':   fields.String,
                                    'road':   fields.String,
                                    'town':   fields.String,
                                    'postcode':   fields.String,
                                    'price_paid':   fields.String}

    def __init__(self):
        self.parser = reqparse.RequestParser()
        for key, val in TitleResource.resource_fields.items():
            self.parser.add_argument(key, type=str)

    @marshal_with(resource_fields)
    def get(self, title_number):
        title = Title.query.filter_by( title_number = title_number).first()
        if title:
            return title
        else:
            abort(404, message="Title number {} doesn't exist".format(title_number))

    def put(self, title_number):
        args = self.parser.parse_args()
        existing_title = Title.query.filter_by( title_number = args['title_number']).first()
        if existing_title:
            app.logger.info('Title number %s already exists. Replace with %s' % (args['title_number'], args))
            db.session.delete(existing_title)
        app.logger.info('Create title with args %s' % args)
        title = Title(**args)
        db.session.add( title )
        db.session.commit()
        return "", 200

