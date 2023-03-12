from flask import Flask

# create an instance of the Flask class with the name of the current module
app = Flask(__name__)

# define a route for the path '/' with methods 'GET' and 'POST'
@app.route("/", methods=["GET", "POST"])
def index():
    return "starting machine learning project"

# run the application in debug mode if this file is executed directly
if __name__ == "__main__":
    app.run(debug=True)

