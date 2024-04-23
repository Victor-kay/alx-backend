#!/usr/bin/env python3
"""
This module initializes a basic Flask web application with Babel integration.
"""

from flask import Flask, render_template, request, redirect, session
from flask_babel import Babel, _
from flask_session import Session

app = Flask(__name__)

# Babel configuration
class Config:
    """
    Config class to set up Babel configurations.
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"
    SESSION_TYPE = 'filesystem'

app.config.from_object(Config)

babel = Babel(app)
Session(app)

@babel.localeselector
def get_locale():
    """
    Determine the best match for the user's preferred language.
    
    Returns:
        str: Best match locale.
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])

@app.route('/')
def index() -> str:
    """
    Render the index.html template.

    Returns:
        str: Rendered HTML content.
    """
    return render_template('2-index.html')

@app.route('/set_locale', methods=['POST'])
def set_locale():
    """
    Set the locale based on POST request data.

    Returns:
        str: Redirect to the index page.
    """
    locale = request.form['locale']
    session['locale'] = locale
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run
