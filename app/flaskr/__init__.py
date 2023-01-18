import os

from flask import Flask, render_template
import requests
import json
from flask import request
# this is the api code


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
    @app.route("/", methods=['GET','POST'])
    def index():    
        api_url=requests.get("https://www.amiiboapi.com/api/amiibo/").text
        api=json.loads(api_url)           
        return render_template('index.html', api=api)
    @app.route("/allamiibo", methods=['GET','POST'])
    def allamiibo():    
        api_url=requests.get("https://www.amiiboapi.com/api/amiibo/").text
        api=json.loads(api_url)           
        return render_template('allamiibo.html', api=api)

    @app.route('/sort/character', methods=['GET'])
    def sortCharacter():
        api_url=requests.get("https://www.amiiboapi.com/api/amiibo/").text
        api=json.loads(api_url) 
        for i in api:
            sortednamedict=i.sort()
            print(sortednamedict)
        return render_template('character.html',methods=['GET'],api=api,sortednamedict=sortednamedict)
    #@app.route("/filter/<filter>")
    #def getFilter():
    return app