from publictitles import server, db
from factories import TitleFactory
import json
import unittest


class AppTestCase(unittest.TestCase):

    def setUp(self):
        db.create_all()
        title = TitleFactory(title_number= 'TN7654321', address = '308 Negra Arroyo Lane', postcode = '87104')
        db.session.add(title)
        db.session.commit()

        self.app = server.app.test_client()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_get_unknown_title(self):
        response = self.app.get('/title/TN99999')
        assert response.status_code == 400

    def test_get_existing_title(self):
        response = self.app.get('/title/TN7654321')

        response_json = json.loads(response.data)

        assert response_json['title_number'] == 'TN7654321'
        assert response_json['address'] == '308 Negra Arroyo Lane'
        assert response_json['postcode'] == '87104'

    def test_post_title(self):
        response = self.app.post('/title/DN100' ,
                                data='{"title_number":"DN100","address":"1224 New Street","postcode":"PL1 7YY"}',
                                content_type='application/json')

        assert response.status_code == 200
