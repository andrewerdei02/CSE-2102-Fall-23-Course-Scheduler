from flask import Flask, request, jsonify
from flask_cors import CORS
import boto3

app = Flask(__name__)
CORS(app)
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('UserData')

@app.route('/signup', methods=['POST'])
def signup():
    # signup logic
    username = request.form['username']
    password = request.form['password']

    # check if username already exists
    response = table.get_item(Key={'username': username})
    if 'Item' in response:
        return jsonify({'message': 'Username already exists.'}), 400
    
    table.put_item(Item={'username': username, 'password': password})
    return jsonify({'message': 'Account created.'}), 200
        
@app.route('/login', methods=['POST'])
def login():
    # login logic
    username = request.form['username']
    password = request.form['password']

    response = table.get_item(Key={'username': username})

    if 'Item' in response:
        user_data = response['Item']
        if user_data['password'] == password:
            return jsonify({'message': 'Login successful'}), 200
        else:
            return jsonify({'message': 'Incorrect password'}), 401
    else:
        return jsonify({'message': 'Username does not exist'}), 404

if __name__ == '__main__':
    app.run(debug=True)