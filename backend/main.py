import os
from flask import Flask
from application import config
from application.config import LocalDevelopmentConfig
from application.database import db
from flask_restful import Resource,Api
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
    api=Api(app)
    app.app_context().push()
    return app,api

app, api = create_app()
CORS(app)

# Import all the controllers so they are loaded
from application.controllers import *
from application.api import  UserAPI,AllThreadsAPI,ThreadAPI,ConnectionAPI,AllUsersAPI,AllThreadsUserAPI
from application.api import PostAPI,AssesmentAPI,MessageAPI,AspirantAPI,AllPostAPI,AllConnectionAPI
from application.api import AllMessageAPI,AllAssesmentsUserAPI,AllAssesmentsAPI,AllAspirantsUsersAPI
from application.api import TopAssesmentsAPI,TopPostAPI,TopThreadsAPI
api.add_resource(UserAPI,"/api/<string:user_id>/<string:password>",'/api/user/CreateUser',"/api/<string:email_id>/<string:password>/Login")
api.add_resource(AllThreadsAPI,'/api/<string:user_id>/<string:password>/getThreads')
api.add_resource(AllAspirantsUsersAPI,'/api/<string:user_id>/<string:password>/Aspirant/getAllAspirantsUsers')
api.add_resource(AllThreadsUserAPI,'/api/<string:user_id>/<string:password>/getThreadsUser')
api.add_resource(AllAssesmentsUserAPI,"/api/<string:user_id>/<string:password>/GetAssesmentsUser")
api.add_resource(AllUsersAPI,'/api/<string:user_id>/<string:password>/getUsers')
api.add_resource(TopThreadsAPI,'/api/<string:user_id>/<string:password>/TopTopics')
api.add_resource(TopAssesmentsAPI,'/api/<string:user_id>/<string:password>/TopAsses')
api.add_resource(TopPostAPI,'/api/<string:user_id>/<string:password>/TopContri')
api.add_resource(AllAssesmentsAPI,'/api/<string:user_id>/<string:password>/getAllAssesments')
api.add_resource(AllConnectionAPI,'/api/<string:user_id>/<string:password>/getConnections')
api.add_resource(AllPostAPI,'/api/<string:user_id>/<string:password>/<string:thread_id>/getPosts')
api.add_resource(ThreadAPI,"/api/<string:user_id>/<string:password>/<string:thread_id>",'/api/<string:user_id>/<string:password>/CreateThread')
api.add_resource(PostAPI,"/api/<string:user_id>/<string:password>/<string:thread_id>/<string:post_id>",'/api/<string:user_id>/<string:password>/<string:thread_id>/CreatePost')
api.add_resource(AssesmentAPI,"/api/<string:user_id>/<string:password>/Assesment/<string:assesment_id>",'/api/<string:user_id>/<string:password>/CreateAssesment')
api.add_resource(AspirantAPI,"/api/<string:user_id>/<string:password>/<string:assesment_id>/Aspirant",'/api/<string:user_id>/<string:password>/<string:assesment_id>/CreateAspirant')
api.add_resource(ConnectionAPI,"/api/<string:user_id>/<string:password>/Connection/<string:connection_id>",'/api/<string:user_id>/<string:password>/CreateConnection')
api.add_resource(AllMessageAPI,"/api/<string:user_id>/<string:password>/<string:connection_id>/getMessages")
api.add_resource(MessageAPI,"/api/<string:user_id>/<string:password>/<string:connection_id>/Message/<string:message_id>",'/api/<string:user_id>/<string:password>//<string:connection_id>/CreateMessage')

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
