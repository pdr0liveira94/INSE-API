"""This module is to configure app to connect with database."""
import os
from flask_mysqldb import MySQL
from app import app

DEBUG = True
# Database settings
app.config["MYSQL_HOST"] = "localhost" # IP Address
app.config["MYSQL_USER"] = "root" # DB User
app.config["MYSQL_PASSWORD"] = "root" # User Password
app.config["MYSQL_DB"] = "inse" # DB Name

app.config['JSON_AS_ASCII'] = True
mysql = MySQL(app)


