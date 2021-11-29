from flask import url_for
from flask_testing import TestCase
from application import app
from unittest.mock import patch
import requests_mock


class TestBase(TestCase):
    def create_app(self):
        return app

class TestResponse(TestBase):

    def test_BMW_SUV(self):
        with patch('requests.get') as a:
            a.return_value.text = 'BMW'
            with patch('random.randrange') as b:
                    b.return_value = 'SUV'
                    response = self.client.post(
                        url_for('model'),
                        data = 'BMW SUV')
                    self.assertEqual(b'X5', response.data)

    def test_BMW_Saloon(self):
        with patch('requests.get') as a:
            a.return_value.text = 'BMW'
            with patch('random.randrange') as b:
                    b.return_value = 'Saloon'
                    response = self.client.post(
                        url_for('model'),
                        data = 'BMW Saloon')
                    self.assertIn(b'5 Series', response.data)

    def test_BMW_Hatchback(self):
        with patch('requests.get') as a:
            a.return_value.text = 'BMW'
            with patch('random.randrange') as b:
                    b.return_value = 'Hatchback'
                    response = self.client.post(
                        url_for('model'),
                        data = 'BMW Hatchback')
                    self.assertIn(b'1 Series', response.data)

    def test_BMW_Coupe(self):
        with patch('requests.get') as a:
            a.return_value.text = 'BMW'
            with patch('random.randrange') as b:
                    b.return_value = 'Coupe'
                    response = self.client.post(
                        url_for('model'),
                        data = 'BMW Coupe')
                    self.assertIn(b'4 Series', response.data)

    def test_Mercedes_SUV(self):
        with patch('requests.get') as a:
            a.return_value.text = 'Mercedes'
            with patch('random.randrange') as b:
                    b.return_value = 'SUV'
                    response = self.client.post(
                        url_for('model'),
                        data = 'Mercedes SUV')
                    self.assertIn(b'GLE', response.data)


    def test_Mercedes_Saloon(self):
        with patch('requests.get') as a:
            a.return_value.text = 'Mercedes'
            with patch('random.randrange') as b:
                    b.return_value = 'Saloon'
                    response = self.client.post(
                        url_for('model'),
                        data = 'Mercedes Saloon')
                    self.assertIn(b'E-Class', response.data)

    def test_Mercedes_Hatchback(self):
        with patch('requests.get') as a:
            a.return_value.text = 'Mercedes'
            with patch('random.randrange') as b:
                    b.return_value = 'Hatchback'
                    response = self.client.post(
                        url_for('model'),
                        data = 'Mercedes Hatchback')
                    self.assertIn(b'A-Class', response.data)

    def test_Mercedes_Coupe(self):
        with patch('requests.get') as a:
            a.return_value.text = 'Mercedes'
            with patch('random.randrange') as b:
                    b.return_value = 'Coupe'
                    response = self.client.post(
                        url_for('model'),
                        data = 'Mercedes Coupe')
                    self.assertIn(b'C-Class', response.data)
    
    def test_Audi_SUV(self):
        with patch('requests.get') as a:
            a.return_value.text = 'Audi'
            with patch('random.randrange') as b:
                    b.return_value = 'SUV'
                    response = self.client.post(
                        url_for('model'),
                        data = 'Audi SUV')
                    self.assertIn(b'Q7', response.data)

                    

    def test_Audi_Saloon(self):
        with patch('requests.get') as a:
            a.return_value.text = 'Audi'
            with patch('random.randrange') as b:
                    b.return_value = 'Saloon'
                    response = self.client.post(
                        url_for('model'),
                        data = 'Audi Saloon')
                    self.assertIn(b'A6', response.data)

    def test_Audi_Hatchback(self):
        with patch('requests.get') as a:
            a.return_value.text = 'Audi'
            with patch('random.randrange') as b:
                    b.return_value = 'Hatchback'
                    response = self.client.post(
                        url_for('model'),
                        data = 'Audi Hatchback')
                    self.assertIn(b'A3', response.data)

    def test_Audi_Coupe(self):
        with patch('requests.get') as a:
            a.return_value.text = 'Audi'
            with patch('random.randrange') as b:
                    b.return_value = 'Coupe'
                    response = self.client.post(
                        url_for('model'),
                        data = 'Audi Coupe')
                    self.assertIn(b'A5', response.data)


    def test_VW_SUV(self):
        with patch('requests.get') as a:
            a.return_value.text = 'VW'
            with patch('random.randrange') as b:
                    b.return_value = 'SUV'
                    response = self.client.post(
                        url_for('model'),
                        data = 'VW SUV')
                    self.assertIn(b'Toureg', response.data)

                    

    def test_VW_Saloon(self):
        with patch('requests.get') as a:
            a.return_value.text = 'VW'
            with patch('random.randrange') as b:
                    b.return_value = 'Saloon'
                    response = self.client.post(
                        url_for('model'),
                        data = 'VW Saloon')
                    self.assertIn(b'Passat', response.data)

    def test_VW_Hatchback(self):
        with patch('requests.get') as a:
            a.return_value.text = 'VW'
            with patch('random.randrange') as b:
                    b.return_value = 'Hatchback'
                    response = self.client.post(
                        url_for('model'),
                        data = 'VW Hatchback')
                    self.assertIn(b'Golf', response.data)

    def test_VW_Coupe(self):
        with patch('requests.get') as a:
            a.return_value.text = 'VW'
            with patch('random.randrange') as b:
                    b.return_value = 'Coupe'
                    response = self.client.post(
                        url_for('model'),
                        data = 'VW Coupe')
                    self.assertIn(b'Arteon', response.data)


    


