from application import app, db
from application.models import pick
from flask import render_template, request, redirect, url_for

@app.route('/')
def home():
    picks = pick.query.limit(5)
    