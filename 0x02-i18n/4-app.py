#!/usr/bin/env python3
"""
4-app: Flask app with forced locale functionality.
"""

from flask import Flask, render_template, request, redirect, session, url_for
from flask_babel import Babel, _, gettext

app = Flask(__name__)

class Config:
    """
    Config class to set up Babel configurations and session type.
    
    Attributes:
        LANGUAGES (list): Supported languages for the app.
        BABEL_DEFAULT_LOCALE (str): Default locale for Babel.
        BABEL_DEFAULT_TIMEZONE (str): Default timezone for Babel.
        SESSION_TYPE (str): Type of session to use.
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"
    SESSION_TYPE = 'filesystem'

app.config.from_object(Config)

babel = Babel(app)

@babel.localeselector
def get_locale() -> str:
    """
    get_locale: Determines the best match for the user's preferred language.
    If locale parameter is present and supported, it will force that locale.
    
    Returns:
        str: Best match locale.
    """
    forced_locale = request.args.get('locale')
    
    if forced_locale and forced_locale in app.config['LANGUAGES']:
        return forced_locale
    
    return request.accept_languages.best_match(app.config['LANGUAGES'])

@app.route('/')
def index() -> str:
    """
    index: Renders the index.html template.
    
    Returns:
        str: Rendered HTML content.
    """
    return render_template('4-index.html')

@app.route('/set_locale', methods=['POST'])
def set_locale() -> redirect:
    """
    set_locale: Sets the locale based on POST request data.
    
    Returns:
        redirect: Redirect to the index page.
    """
    locale = request.form['locale']
    session['locale'] = locale
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
