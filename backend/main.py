import os
from flask import Flask
from application import config
from application.config import LocalDevelopmentConfig
from application.database import db
from application import workers
from flask_restful import Resource,Api
from sqlalchemy.orm import scoped_session, sessionmaker
from flask_security import Security, SQLAlchemySessionUserDatastore, SQLAlchemyUserDatastore,utils
from application.models import User, Role
from flask_login import LoginManager
# from flask_cors import cors
from flask_cors import CORS 

app = None
api=None
def create_app():
    app = Flask(__name__, template_folder="templates")
    if os.getenv('ENV', "development") == "production":
      raise Exception("Currently no production config is setup.")
    else:
      print("Staring Local Development")
      app.config.from_object(LocalDevelopmentConfig)
    db.init_app(app)
    app.app_context().push()
    app.logger.info("App setup complete")
    # Setup Flask-Security
    user_datastore = SQLAlchemySessionUserDatastore(db.session, User, Role)
    security = Security(app, user_datastore)
    api=Api(app)
    app.app_context().push()
    celery = workers.celery

    # Update with configuration
    celery.conf.update(
        broker_url = app.config["CELERY_BROKER_URL"],
        result_backend = app.config["CELERY_RESULT_BACKEND"]
    )

    celery.Task = workers.ContextTask
    app.app_context().push()
    return app, api, celery

app, api,celery = create_app()
CORS(app)
# Import all the controllers so they are loaded
from application.controllers import *
from application.api import  UserAPI,ListAPI,CardAPI,OneListAPI,OneCardAPI
api.add_resource(UserAPI,"/api/<string:User_Id>/<string:password>",'/api/User/Create')
api.add_resource(ListAPI,"/api/<string:User_Id>/getList","/api/<string:User_Id>/AddList","/api/<string:User_Id>/<string:List_Id>/EditList","/api/<string:User_Id>/<string:List_Id>/DeleteList")
api.add_resource(OneListAPI,"/api/<string:User_Id>/<string:Name>/getList")
api.add_resource(OneCardAPI,"/api/<string:User_Id>/<string:Title>/getCard")
api.add_resource(CardAPI,"/api/<string:List_Id>/GetCards","/api/<string:User_Id>/<string:Card_Id>/DeleteCard","/api/<string:User_Id>/<string:Card_Id>/EditCard","/api/<string:User_Id>/<string:List_Id>/AddCard")


# from application.api import TestAPI
# api.add_resource(TestAPI, "/api/test")


@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('404.html'), 404


@app.errorhandler(403)
def not_authorized(e):
    # note that we set the 403 status explicitly
    return render_template('403.html'), 403

if __name__ == '__main__':
  # Run the Flask app
  app.run(host='0.0.0.0',debug=True,port=8000)
