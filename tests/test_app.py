from publictitles import server, db
from . factories import TitleFactory

import unittest


class AppTestCase(unittest.TestCase):

    def setUp(self):
        SQLALCHEMY_DATABASE_URI = "sqlite://"
        server.app.config['TESTING'] = True
        server.app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
        db.create_all()

        title = TitleFactory()
        db.session.add(title)
        db.session.commit()
        print "This is the title"
        print title

        self.app = server.app.test_client()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_get_title(self):
        rv = self.app.get('/titles/TN1234567')
        assert 'TN1234567' in rv.data
