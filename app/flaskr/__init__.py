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
        try:
            return render_template('allamiibo.html', api=api)
        except:
            return render_template('error.html')

    @app.route('/sort/character', methods=['GET'])
    def sortCharacter():
        api_url=requests.get("https://www.amiiboapi.com/api/amiibo/").text
        api=json.loads(api_url) 
        for i in api['amiibo']:
            sortednamedict=sorted(i['character'])
            print(sortednamedict)
        try:
            return render_template('character.html',methods=['GET'],api=api,sortednamedict=sortednamedict)
        except:
            return render_template('error.html')

    
    @app.route('/sort/search/?name=<path:amiiboname>',methods=['GET','POST'])
    def sortSearch(amiiboname):
        amiiboname=request.form.get("amiiboname")
        api_url=requests.get(f"https://www.amiiboapi.com/api/amiibo/?name={amiiboname}").text
        api=json.loads(api_url) 
        try:
            return render_template('name.html',methods=['GET','POST'],api=api)
        except:
            return render_template('error.html')
        
    @app.errorhandler(404)
    def page_not_found(error):
        return render_template('error.html'),404
    return app