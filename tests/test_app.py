from publictitles import server, db
from factories import TitleFactory
import json
import unittest


class AppTestCase(unittest.TestCase):

    def setUp(self):
        db.create_all()
        title = TitleFactory(title_number= 'TN7654321', house_number= "1", road= 'Negra Arroyo Lane', town="Croydon", postcode = '87104')
        db.session.add(title)
        db.session.commit()
        self.app = server.app.test_client()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_get_unknown_title(self):
        response = self.app.get('/titles/TN99999')
        assert response.status_code == 404

    def test_get_existing_title(self):
        response = self.app.get('/titles/TN7654321')

        response_json = json.loads(response.data)

        assert response_json['title_number'] == 'TN7654321'
        assert response_json['house_number'] == '1'
        assert response_json['road'] == 'Negra Arroyo Lane'
        assert response_json['town'] == 'Croydon'
        assert response_json['postcode'] == '87104'

    def test_put_title(self):
        response = self.app.put('/titles/DN100' ,
                                data='{"title_number":"DN100","house_number":"1", "road":"New Street", "town":"Croydon","postcode":"PL1 7YY","price_paid":"233"}',
                                content_type='application/json')

        assert response.status_code == 201


    def test_put_title_twice_gives_correct_status_codes(self):
        response = self.app.put('/titles/DN100' ,
                                data='{"title_number":"DN100","house_number":"1", "road":"New Street", "town":"Croydon","postcode":"PL1 7YY","price_paid":"233"}',
                                content_type='application/json')

        assert response.status_code == 201

        response = self.app.put('/titles/DN100' ,
                                data='{"title_number":"DN100","house_number":"1", "road":"New Street", "town":"Croydon","postcode":"PL1 7YY","price_paid":"233"}',
                                content_type='application/json')

        assert response.status_code == 200
