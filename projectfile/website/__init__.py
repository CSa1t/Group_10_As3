from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy

db=SQLAlchemy()

def create_app():
    app=Flask(__name__)

    bootstrap = Bootstrap(app)

    #Secret key
    app.secret_key='somerandomvalue'

    #Blueprints
    from . import views
    app.register_blueprint(views.mainbp)
    from . import markets
    app.register_blueprint(markets.bp)

    return app
