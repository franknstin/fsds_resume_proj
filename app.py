from flask import Flask
from housing.logger import logging

# create an instance of the Flask class with the name of the current module
app = Flask(__name__)

# define a route for the path '/' with methods 'GET' and 'POST'
@app.route("/", methods=["GET", "POST"])
def index():
    logging.info("we are testing logging module")
    return "starting machine learning project"

# run the application in debug mode if this file is executed directly
if __name__ == "__main__":
    app.run(debug=True)

