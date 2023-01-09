import os

from flask import Flask, render_template
import requests
import json
# this is the api code
api_url=requests.get("https://www.amiiboapi.com/api/amiibo/").json()
api=api_url['amiibo']

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route("/")
    def index():
        return render_template('index.html', api=api)

    #@app.route("/filter/<filter>")
    #def getFilter():


    @app.errorhandler(404)
    def interestnotfound(error):
        return render_template ('error.html'), 404

    return app