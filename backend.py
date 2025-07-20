from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory user "database" for demo
users = {}

@app.route('/signup', methods=['POST'])
def signup():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    if username in users:
        return jsonify({"message": "User already exists"}), 400

    users[username] = password
    return jsonify({"message": "User created successfully"}), 201

@app.route('/signin', methods=['POST'])
def signin():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    stored_password = users.get(username)
    if stored_password and stored_password == password:
        return jsonify({"message": "Signed in successfully"}), 200
    else:
        return jsonify({"message": "Invalid credentials"}), 401

if __name__ == '__main__':
    app.run(debug=True)
