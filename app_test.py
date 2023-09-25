import unittest
import app

class TestApp(unittest.TestCase):

    print('----------RUNNING TESTS----------')
    def test_parseXML(self):
        # Test the parseXML function
        xml_path = './test.xml'
        parsed_data = app.parseXML(xml_path)

        # Add assertions to check if the parsing works correctly
        self.assertEqual(len(parsed_data['subdomains']), 1)
        self.assertEqual(len(parsed_data['cookies']), 2)

    def test_redisSave(self):
        # Test the redisSave function
        subdomains = ['testdomain']
        cookies = [('testname1', 'testhost1', 'testcookie1'), ('testname2', 'testhost2', 'testcookie2')]

        # Call the redisSave function and check that it doesn't raise any exceptions
        try:
            app.redisSave(subdomains, cookies)
        except Exception as e:
            self.fail(f"redisSave raised an exception: {e}")

if __name__ == '__main__':
    unittest.main()
