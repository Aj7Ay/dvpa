import os
from flask import Flask
from flask_mongoengine import MongoEngine
from blog import config
from flask_mysqldb import MySQL

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
UPLOAD_FOLDER = os.path.join(BASE_DIR, "uploads")
ALLOWED_EXTENSIONS = {'yaml', 'json', 'yml'}
app.config['SECRET_KEY'] = config.SECRET_KEY
app.config['MYSQL_HOST'] = config.DB_HOST
app.config['MYSQL_DB'] = config.DB_NAME
app.config['MYSQL_USER'] = config.DB_USER
app.config['MYSQL_PASSWORD'] = config.DB_PASS
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

# db = MongoEngine(app)
db = MySQL(app)

def register_blueprints(app):
    from blog.views import posts
    from blog.user import user
    from blog.dashboard.routes import dashboard
    # from blog.admin import admin
    app.register_blueprint(posts)
    app.register_blueprint(user)
    app.register_blueprint(dashboard)

register_blueprints(app)

if __name__ == '__main__':
    app.run()