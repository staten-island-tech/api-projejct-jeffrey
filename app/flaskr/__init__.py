import os

from flask import Flask, render_template
import requests
from .api import api


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
    def home():
        return render_template('index.html')

    @app.route("/<path:value>", methods=['GET', 'POST'])
    def getValue(value):
        for a in api['data']:
            for b in api['type']:
                if value == b['value']: 
                    return render_template("interest.html",api=api,value=value)
        return render_template("error.html")

    @app.errorhandler(404)
    def interestnotfound(error):
        return render_template ('error.html'), 404

    return app