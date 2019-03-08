import os
from config import config_map
from flask import Flask

from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy

from blueprint import auth,admin,blog

from blueblog.extensions import bootstrap,db




def create_app(config_name=None):
    app = Flask(__name__)

    if config_name is None:
        config_name = os.getenv('FLASK_CONFIG', 'Development')
        app.config.from_object(config_map[config_name])

    register_extensions(app)
    register_logging(app)
    register_bluprint(app)
    register_commands(app)
    register_shell_context(app)
    register_template_context(app)


    return app


def register_extensions(app):
    bootstrap.init_app(app)
    db.init_app(app)

def register_logging(app):
    pass

def register_bluprint(app):
    app.register_blueprint(auth.auth_bp,url_prefix='/auth')
    app.register_blueprint(blog.blog_bp,url_prefix='/blog')
    app.register_blueprint(admin.admin_bp,url_prefix='/admin')


def register_commands(app):
    pass

def register_shell_context(app):
    pass

def register_template_context(app):
    pass


def register_errors(app):
    pass

