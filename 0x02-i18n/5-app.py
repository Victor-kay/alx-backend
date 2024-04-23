#!/usr/bin/env python3
"""
5-app: Flask app with user login emulation.
"""

from flask import Flask, render_template, g
from flask_babel import Babel, _, gettext

app = Flask(__name__)

class Config:
    """
    Config class to set up Babel configurations.
    
    Attributes:
        LANGUAGES (list): Supported languages for the app.
        BABEL_DEFAULT_LOCALE (str): Default locale for Babel.
        BABEL_DEFAULT_TIMEZONE (str): Default timezone for Babel.
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"

app.config.from_object(Config)

babel = Babel(app)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}

def get_user(user_id: int) -> dict:
    """
    get_user: Retrieve user information based on user ID.
    
    Args:
        user_id (int): ID of the user.
    
    Returns:
        dict: User information if found, otherwise None.
    """
    return users.get(user_id)

@app.before_request
def before_request():
    """
    before_request: Execute before all other functions.
    Sets the user information on flask.g if user is logged in.
    """
    login_as = int(request.args.get('login_as', 0))
    g.user = get_user(login_as) if login_as else None

@app.route('/')
def index():
    """
    index: Renders the index.html template.
    
    Returns:
        str: Rendered HTML content.
    """
    return render_template('5-index.html')

if __name__ == '__main__':
    app.run(debug=True)
