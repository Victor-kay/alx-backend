# 0x02. i18n

## Description
This project aims to set up a basic Flask application with internationalization (i18n) support using Flask-Babel. The application will display content in different languages based on user preferences, URL parameters, or request headers.

## Tasks

### 0. Basic Flask app
Initialize a basic Flask app with a single route to display "Welcome to Holberton" and "Hello world".

### 1. Basic Babel setup
Install Flask-Babel and configure it with two supported languages: English and French.

### 2. Get locale from request
Implement a function to determine the user's preferred language based on the request headers.

### 3. Parametrize templates
Use Babel's `_` or `gettext` function to parametrize templates with message IDs for translation.

### 4. Force locale with URL parameter
Implement a mechanism to force a specific locale by passing a `locale` parameter in the app's URLs.

### 5. Mock logging in
Emulate a user login system by mocking a user table and implementing a `get_user` function to fetch user details.

### 6. Use user locale
Modify the locale selection logic to prioritize a user's preferred locale if available.

### 7. Infer appropriate time zone
Implement a function to infer the appropriate time zone based on user preferences or URL parameters.

### 8. Display the current time
Display the current time on the home page based on the inferred time zone.

## Files
- `0-app.py`: Basic Flask app
- `1-app.py`: Basic Babel setup
- `2-app.py`: Get locale from request
- `3-app.py`: Parametrize templates
- `4-app.py`: Force locale with URL parameter
- `5-app.py`: Mock logging in
- `6-app.py`: Use user locale
- `7-app.py`: Infer appropriate time zone
- `babel.cfg`: Babel configuration file
- `templates/0-index.html` to `templates/7-index.html`: HTML templates
- `translations/en/LC_MESSAGES/messages.po` and `translations/fr/LC_MESSAGES/messages.po`: Translation files
