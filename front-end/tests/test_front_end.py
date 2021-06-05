from flask import url_for
from flask_testing import TestCase
import requests_mock 

from app import app, db

class TestBase(TestCase):
    def create_app(self):
        app.config.update(SQLALCHEMY_DATABASE_URI="sqlite:///test.db",
        SECRET_KEY='SECRET_KEY',
        WTF_CSRF_ENABLED=False,
        DEBUG=True,
        )
        return app

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

class TestHome(TestBase):
    def test_home(self):
        with requests_mock.Mocker() as mocker:
            mocker.get('http://project_random_operator:5000/operator', json={"operator":'Ash', "difficulty":0})
            mocker.get('http://project_random_strat:5000/strat', json={"strat":'Train', "difficulty":20})
            mocker.post('http://project_points:5000/points', text='35')
            response = self.client.get(url_for('home'))
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'Ash', response.data)
            self.assertIn(b'Train', response.data)
            self.assertIn(b'35', response.data)