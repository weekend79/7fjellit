"""
My imports
"""
import os
from flask import Flask, render_template, url_for

# Connection configuration
app = Flask(__name__)


"""
App routes
"""
# Index
@app.route('/')
def index():
    return render_template('index.html')


# Services / Tjenester
@app.route('/tjenester')
def tjenester():
    return render_template('tjenester.html')


# About 7 Fjell IT / Om 7 Fjell IT
@app.route('/about')
def about():
    return render_template('about.html')


# Contact / Kontakt oss 
@app.route('/contact')
def contact():
    return render_template('contact.html')


# App development
@app.route('/app_dev')
def app_dev():
    return render_template('app_dev.html')


# It-Services / It Drift
@app.route('/drift')
def drift():
    return render_template('drift.html')


# Coding / programmering
@app.route('/kode')
def kode():
    return render_template('kode.html')


# Cloud services / Skytjenester
@app.route('/sky')
def sky():
    return render_template('sky.html')


# Websites / Nettside
@app.route('/web')
def web():
    return render_template('web.html')


# Webshop / Nettbutikk
@app.route('/webshop')
def webshop():
    return render_template('webshop.html')

# App run
if __name__ == '__main__':
    app.secret_key = os.getenv('SECRET_KEY')
    app.run(host=os.environ.get('IP', '0.0.0.0'),
            port=int(os.environ.get('PORT', '5000')), 
            debug=True)