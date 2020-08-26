from flask import Flask, jsonify, request, Response
from flask_pymongo import PyMongo

app = Flask(__name__)
app.secret_key = 'myawesomesecretkey'

app.config['MONGO_URI'] = 'mongodb+srv://ulisessdev:googlemx@cluster0-ikksp.mongodb.net/test?retryWrites=true&w=majority'
mongo = PyMongo(app)


@app.route('/users', methods=['GET'])
def craete_user():
    username = request.json['username']
    age = request.json['age']
    if username and age:
        id = mongo.db.users.insert(
            {'username': username, 'age': age})
        response = jsonify({
            '_id': str(id),
            'username': username,
            'age': age
        })
        response.status_code = 201
        return response
    else:
        return not_found()

if __name__ == "__main__":
    app.run(debug=True)