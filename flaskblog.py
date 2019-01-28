from flask import Flask

# name of the module = __name__
# where the flask looks for the flask files
app = Flask(__name__)

# this is the url
# urls are the app.route

@app.route("/")
@app.route("/home")
def home():
    return "hi World!"

@app.route("/about")
def about():
    return "about World!"































# create a python file with the from flask import FLASK
# in the terminal export FLASK_APP=your flask title
# do flask run
# to turn on debug mode - export FLASK_DEBUG=1

if __name__ == '__main__':
    app.run(debug=True)
