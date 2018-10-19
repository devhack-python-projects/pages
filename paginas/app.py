from flask import Flask


def create_app(test_config=None):
    app = Flask(__name__)
    app.config.from_mapping(
        SECRET_KEY='dev'
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py')
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    from .applications.blueprint_1 import bp as blueprint_1
    app.register_blueprint(blueprint_1)

    return app
