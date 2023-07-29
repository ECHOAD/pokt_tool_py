from flask import Flask, redirect
from flask_cors import CORS
import os

from flask_swagger_ui import get_swaggerui_blueprint

from .nodes import nodes


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True, template_folder="../templates")

    if test_config is None:
        app.config.from_mapping(
            SECRET_KEY=os.environ.get
            ('SECRET_KEY')
        )
    else:
        app.config.from_mapping(test_config)

    CORS(app, resources={r"/api/*": {"origins": "*"}})

    SWAGGER_URL = '/api/v1/docs'
    API_URL = '/static/swagger.json'

    swaggerui_blueprint = get_swaggerui_blueprint(
        SWAGGER_URL,
        API_URL,
        config={
            'app_name': "Node Fleet StartPort API"
        }
    )

    app.register_blueprint(swaggerui_blueprint)  # blueprint for swagger
    app.register_blueprint(nodes)

    @app.route("/")
    def index():
        return redirect(location='/api/v1/docs')

    return app
