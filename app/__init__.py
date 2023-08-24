import os
from flask import Flask


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='your-secret-key-here',
        DATABASE=os.path.join(app.instance_path, 'app.db')
    )

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    from .db import init_app
    init_app(app)

    from . import auth
    app.register_blueprint(auth.bp)

    return app
