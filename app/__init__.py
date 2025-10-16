import logging
from flask import Flask, request
from .config import Config
from .exceptions import register_error_handlers
from .celery_app import celery
from .routes import routes_bp

def create_app():
    app = Flask(__name__)

    @app.before_request
    def log_request():
        print(f"New Request: {request.method} {request.path}")

    app.config.from_object(Config)
    app.register_blueprint(routes_bp)
    register_error_handlers(app)

    celery.conf.update(app.config)
    app.celery = celery

    return app
