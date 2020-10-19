import os

from flask import Flask


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)

    if test_config is not None:
        # load the test config if passed in
        app.config.from_mapping(test_config)    

    # a route for testing
    @app.route('/health')
    def hello():
        return 'I am healthy!'

    from . import wallclock
    app.register_blueprint(wallclock.bp)

    return app