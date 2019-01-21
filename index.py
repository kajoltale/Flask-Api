from flask import Flask, render_template, request
from DatabaseHelper import getUserInfo, createUser, getUser, alterUser, deleteUser

# Create the application.
app = Flask(__name__)


@app.route('/')
def index():
    return "Welcome"

@app.route('/api/users', methods = ['GET', 'POST'])
def getUsers():
    if request.method == 'GET':
        return getUserInfo(request)
    if request.method == 'POST':
        return createUser(request)
    else:
        return 'Invalid Request'

@app.route('/api/users/<id>', methods = ['GET', 'PUT', 'DELETE'])
def getUserWithId(id):
    if request.method == 'GET':
        return getUser(id)
    elif request.method == 'PUT':
        return alterUser(id, request)
    elif request.method == 'DELETE':
        return deleteUser(id)



if __name__ == '__main__':
    app.run(port='8091')
