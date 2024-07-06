# app.py

from flask import Flask, render_template

# Create a Flask application instance
app = Flask(__name__)

# Define a route for the homepage
@app.route('/')
def home():
    return render_template('index.html')

# Run the app if this script is executed
if __name__ == '__main__':
    app.run(debug=True)
