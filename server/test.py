from app import db
from app.models import User, Message
print("deleting all users and messages")
users = User.query.all()
messages = Message.query.all()
for u in users:
    db.session.delete(u)

for m in messages:
    db.session.delete(m)

db.session.commit()

print("adding users Ashley and Julie")
u1 = User(username='Ashley')
u2 = User(username='Julie')
db.session.add(u1)
db.session.add(u2)
db.session.commit()

print("two users should print below without passwords")
users = User.query.all()
for u in users:
    print(u.id, u.username, u.password_hash)

print("adding password 'foobar' to Ashley's account")
ashley = User.query.get(1)
julie = User.query.get(2)
ashley.set_password('foobar')
users = User.query.all()
for u in users:
    print(u.id, u.username, u.password_hash)

print("Ashley has password 'blahblah'?")
print(ashley.validate_password('blahblah'))

print("Ashley has password 'foobar'?")
print(ashley.validate_password('foobar'))

print("adding one message from Ashley")
message = Message(message="Let's go out.", sender=ashley, recipient=julie)
db.session.add(message)
db.session.commit()

print("adding one response from Julie")
message = Message(message="Okie dokie.", sender=julie, recipient=ashley)
db.session.add(message)
db.session.commit()

print("two messages should print below")
messages = Message.query.all()
for m in messages:
    print(m.sender.username, "->", m.recipient.username, ":", m.message)

exit()
