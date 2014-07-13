from publictitles import server, db
from factories import TitleFactory
import json
import unittest


class AppTestCase(unittest.TestCase):

    def setUp(self):
        SQLALCHEMY_DATABASE_URI = "sqlite://"
        server.app.config['TESTING'] = True
        server.app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
        db.create_all()

        title = TitleFactory(title_number= 'TN7654321', address = '308 Negra Arroyo Lane', postcode = '87104')
        db.session.add(title)
        db.session.commit()

        self.app = server.app.test_client()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_get_title(self):
        response = self.app.get('/titles/TN7654321')
        response_json = json.loads(response.data)

        assert response_json['title_number'] == 'TN7654321'
        assert response_json['address'] == '308 Negra Arroyo Lane'
        assert response_json['postcode'] == '87104'
