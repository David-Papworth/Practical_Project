from flask import url_for
from flask_testing import TestCase
from unittest.mock import patch 

from app import app

class TestBase(TestCase):
    def create_app(self):
        return app

class TestHome(TestBase):
    def test_points(self):
        test_cases=[(0,0), (0,20), (0,40), (10,0), (10,20), (10,40), (20,0), (20,20), (20,40)]
        for ops,stra in test_cases:
            response = self.client.post(url_for('points'), json={"difficulty":ops, "difficulty_strat":stra})
            lower = 0 + ops + stra
            upper = 50 + ops + stra
            self.assertIn(int(response.data),range(lower,upper))