from flask import render_template
from app import app

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
