#!/usr/bin/env python3
"""
This module initializes a basic Flask web application with Babel integration.
"""

from flask import Flask, render_template
from flask_babel import Babel

app = Flask(__name__)

# Babel configuration
class Config:
    """
    Config class to set up Babel configurations.
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"

app.config.from_object(Config)

babel = Babel(app)

@app.route('/')
def index() -> str:
    """
    Render the index.html template.

    Returns:
        str: Rendered HTML content.
    """
    return render_template('1-index.html')

if __name__ == '__main__':
    app.run(debug=True)
