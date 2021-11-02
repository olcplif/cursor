import unittest
from app import app


class TestForWeather(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()
        app.config["Unit_test"] = True

    def test_weather_1(self):
        response = self.client.get('/weather?city=Lviv')
        self.assertEqual(response.status_code, 200)
        self.assertIn(response.json['location']['name'], "Lviv")

    def test_your_weather_2(self):
        response = self.client.get('/get-your-weather')
        self.assertNotEqual(response.status_code, 404)
        self.assertEqual(response.status_code, 200)

    def test_weather_cities_3(self):
        response = self.client.get('/weather-cities?cities=Poltava%20Lviv%20Reshetylivka%20Odesa')
        self.assertEqual(response.status_code, 200)
        response_data = response.get_data(as_text=True)
        self.assertIn("Poltava", response_data)
        self.assertIn("Lviv", response_data)
        self.assertIn("Reshetylivka", response_data)
        self.assertIn("Odesa", response_data)
        self.assertNotIn("No matching location found.", response_data)


if __name__ == 'main':
    unittest.main()
