from flask import render_template, request, jsonify
from app import app
from app import db
from app.models import User, Message
from sqlalchemy import or_


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'darth-vader'}
    return '''
<html>
    <head>
        <title>Messaging App</title>
    </head>
    <body>
        <h1>Hello, ''' + user['username'] + '''!</h1>
    </body>
</html>'''

@app.route('/log')
def log():
    messages = [
        {
            'sender': {'username': 'Yoda'},
            'recipient': {'username': 'Luke'},
            'message': 'When nine hundred years old you reach, look as good you will not.'
        },
        {
            'sender': {'username': 'Luke'},
            'recipient': {'username': 'Yoda'},
            'message': 'How long have you been butchering the English language?'
        }
    ]
    return render_template('index.html', title='Log', messages=messages)

@app.route('/json-test', methods=['POST'])
def json_test():
    request_data = request.get_json()

    sender = request_data['sender']
    recipient = request_data['recipient']
    message = request_data['message']

    return jsonify(request_data)

@app.route('/messages/<username>')
def get_messages(username):

    print("username is {}".format(username))

    user = User.query.filter_by(username=username).first_or_404()

    print("user", user)
    print("user_id is {}".format(user.id))

    messages = Message.query.filter(or_((Message.sender_id == user.id) | (Message.recipient_id == user.id)))

    message_list = []

    for message in messages:
        details = {'id': message.id, 'timestamp': message.timestamp, 'sender': message.sender.username,
                   'recipient': message.recipient.username, 'message': message.message}

        message_list.append(details)

    return jsonify(message_list)

@app.route('/messages', methods=['POST'])
def create_message():
    request_data = request.get_json()

    print('sender', request_data['sender'])
    print('recipient', request_data['recipient'])
    print('messagee', request_data['message'])

    sender = User.query.filter_by(username=request_data['sender']).first_or_404()
    recipient = User.query.filter_by(username=request_data['recipient']).first_or_404()

    message = Message(message=request_data['message'], sender=sender, recipient=recipient)

    print(message)

    db.session.add(message)
    db.session.commit()

    return jsonify(request_data)

@app.route('/users', methods=['GET', 'POST'])
def process_users():

    if request.method == 'GET':
        users = User.query.all()

        user_list = []

        for user in users:
            details = {'username': user.username}
            user_list.append(details)

        return jsonify(user_list)

    request_data = request.get_json()

    print('adding user', request_data['username'])

    user = User(username=request_data['username'])

    db.session.add(user)
    db.session.commit()

    return jsonify(request_data)
