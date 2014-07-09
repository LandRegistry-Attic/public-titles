from publictitles import server
import unittest

class AppTestCase(unittest.TestCase):

    def setUp(self):
        server.app.config['TESTING'] = True
        self.app = server.app.test_client()

    #Nothing to put into the teardown for this testcase
    #def tearDown(self):

    def test_get_title(self):
        rv = self.app.get('/titles/DN100')
        assert 'DN100' in rv.data
