from flask import render_template, request, jsonify
from app import app
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

    #return "sender {} -> recipient {}: {}".format(sender, recipient, message)

    return jsonify(request_data)

@app.route('/messages/get/<username>')
def get_messages(username):
    # request_data = request.get_json()
    # user = request_data['user']

    # return all messages from/to user. sort them by timestamp so the correct ordering is maintained.

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

