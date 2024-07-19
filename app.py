from flask import Flask, g, session, redirect, render_template, request, jsonify, Response
from Misc.functions import *
import markupsafe
import os
import logging
from logging.handlers import RotatingFileHandler

app = Flask(__name__)

# Use environment variable for secret key or configure it securely
app.secret_key = os.environ.get('SECRET_KEY', '#$ab9&^BB00_.')

# Setting DAO Class
from Models.DAO import DAO

DAO = DAO(app)

# Registering blueprints
from routes.user import create_user_view
from routes.book import create_book_view
from routes.admin import create_admin_view

# Create and register the user, book, and admin blueprints
user_view = create_user_view(DAO)
book_view = create_book_view(DAO)
admin_view = create_admin_view(DAO)

app.register_blueprint(user_view)
app.register_blueprint(book_view)
app.register_blueprint(admin_view)

# Registering custom functions to be used within templates
app.jinja_env.globals.update(
    ago=ago,
    str=str,
)


if __name__ == '__main__':
    app.run()
