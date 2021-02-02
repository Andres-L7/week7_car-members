from cars_api import app
from flask import render_template

#home Route -- AKA Main Landing Page Route
@app.route('/')
def home():
    return render_template('home.html')