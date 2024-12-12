import unittest
from app import create_app

class FlaskTestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()
        self.app.testing = True

    def test_home(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b"Welcome to the Raspberry Pi Metrics API!")

    def test_cpu_temperature(self):
        response = self.client.get('/cpu-temperature')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"cpu_temperature", response.data)

    def test_disk_usage(self):
        response = self.client.get('/disk-usage')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"total", response.data)
        self.assertIn(b"used", response.data)
        self.assertIn(b"free", response.data)
        self.assertIn(b"percent", response.data)

if __name__ == '__main__':
    unittest.main()