from flask import url_for
from flask_testing import TestCase
from unittest.mock import patch 

from app import app

class TestBase(TestCase):
    def create_app(self):
        return app

class TestOpp(TestBase):
    def test_operator(self):
        for _ in range(20):
            response = self.client.get(url_for('operator'))
            self.assertEqual({'Sledge':0, 'Thatcher':10, 'Ash':0, 'Thermite':10, 'Montagne':20, 'Twitch':10, 'Blitz':10, 'Fuze':20, 'Glaz':20, 'Buck':0, 'Blackbeard':0, 'Capitao':10, 'Hibana':10}[response.json["operator"]],response.json["difficulty"])
