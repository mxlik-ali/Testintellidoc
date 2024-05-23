from flask import Flask

app = Flask(__name__)

@app.route('/')
def welcome():
    return 'Hello World'

@app.route('/home')
def home():
    return 'Home World'

@app.route('/page')
def page():
    return 'page World'
if __name__ =='__main__':
    app.run(debug=True)

#to auto reload the code on the server and not requiring to run flask run after every time u make chnages set env var
#$env:FLASK_ENV='development'

#to stop the making of pycache file run the command on terminal
#$env:PYTHONDONTWRITEBYTECODE=1

from controller import user_controller,product_controller
# import controller.user_controller as user_controller
# import controller.product_controller as product_controller