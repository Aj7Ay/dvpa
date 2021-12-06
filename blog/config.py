import os

# Host & Databases
DB_HOST = os.environ['DB_HOST']
DB_NAME = os.environ['DB_NAME']
DB_USER = os.environ['DB_USER']
DB_PASS = os.environ['DB_PASS']

MONGODB_SETTINGS = 'flaskblog_db'
SECRET_KEY = 'flaskblog_secret_key'

# Debugging & Reloader
debugger = True
reloader = True

# Admin authentication
# url for: /admin/
username = 'admin'
password = 'secret'

# Disqus Configuration
disqus_shortname = 'blogpythonlearning'

# Post pagination per-page
per_page = 5