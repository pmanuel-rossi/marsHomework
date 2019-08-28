"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template, redirect
from WebScrapingHomework import app
import scrape_mars

@app.route('/')
@app.route('/home')
def home():
    data = scrape_mars.retrieveData()
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
				data = data
    )

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )

@app.route("/scrape")
def scrapeMars():
	marsData = scrape_mars.scrapeMars()
	scrape_mars.storeInDb(marsData)
	return redirect("/")