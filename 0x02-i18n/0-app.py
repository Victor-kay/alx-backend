#!/usr/bin/env python3
"""
This module initializes a basic Flask web application.
"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index() -> str:
    """
    Render the index.html template.

    Returns:
        str: Rendered HTML content.
    """
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run(debug=True)
