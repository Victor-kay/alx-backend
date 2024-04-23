#!/usr/bin/env python3
"""
6-app: Flask app with user login emulation and locale priority.
"""

from flask import Flask, render_template, g, request
from flask_babel import Babel, _, gettext

app = Flask(__name__)

class Config:
    """
    Config class to set up Babel configurations.
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
    """Retrieve user information based on user ID."""
    return users.get(user_id)

@app.before_request
def before_request():
    """Execute before all other functions. Sets the user information."""
    login_as = int(request.args.get('login_as', 0))
    g.user = get_user(login_as) if login_as and login_as in users else None

@babel.localeselector
def get_locale() -> str:
    """Determines the best match for the user's preferred language."""
    forced_locale = request.args.get('locale')
    
    if forced_locale and forced_locale in app.config['LANGUAGES']:
        return forced_locale
    
    if g.user and g.user['locale'] in app.config['LANGUAGES']:
        return g.user['locale']
    
    browser_locale = request.accept_languages.best_match(app.config['LANGUAGES'])
    
    return browser_locale or app.config['BABEL_DEFAULT_LOCALE']

@app.route('/')
def index():
    """Renders the index.html template."""
    return render_template('6-index.html')

if __name__ == '__main__':
    app.run(debug=True)
