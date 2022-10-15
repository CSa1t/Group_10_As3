from flask import Flask


def create_app():
    app=Flask(__name__)
    
    #add Blueprints
    from . import views
    app.register_blueprint(views.mainbp)
    from . import markets
    app.register_blueprint(markets.bp)

    return app