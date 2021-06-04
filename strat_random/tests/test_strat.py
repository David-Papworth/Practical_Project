from flask import url_for
from flask_testing import TestCase
from unittest.mock import patch 

from app import app

class TestBase(TestCase):
    def create_app(self):
        return app

class TestHome(TestBase):
    def test_strat(self):
        for _ in range(20):
            response = self.client.get(url_for('strat'))
            self.assertEqual({'Primary Only':0, 'Secondary Only':20, 'Snail Mode':40, 'Train':20, 'Rush':0, '1 minute plant':20, 'last minute rush':20, 'knife only':40}[response.json["strat"]],response.json["difficulty"])