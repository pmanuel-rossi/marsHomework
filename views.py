"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template, redirect
from WebScrapingHomework import app
import scrape_mars



@app.route("/scrape")
def scrapeMars():
	marsData = scrape_mars.scrapeMars()
	scrape_mars.storeInDb(marsData)
	return redirect("/")