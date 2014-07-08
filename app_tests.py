from publictitles import server
import unittest

class AppTestCase(unittest.TestCase):

    def setUp(self):
        server.app.config['TESTING'] = True
        self.app = server.app.test_client()

    #Nothing to put into the teardown for this testcase
    #def tearDown(self):

    def test_hello_world(self):
        rv = self.app.get('/titles/DN100')
        print rv.data
        assert 'Hello DN100' in rv.data

if __name__ == '__main__':
    unittest.main()
