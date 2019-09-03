from app import db
from app.models import User, Message
users = User.query.all()
messages = Message.query.all()
for u in users:
	db.session.delete(u)

for m in messages:
	db.session.delete(m)	

db.session.commit()
u1 = User(username='Ashley')
u2 = User(username='Julie')
db.session.add(u1)
db.session.add(u2)
db.session.commit()
users = User.query.all()
print(users)
ashley = User.query.get(1)
julie = User.query.get(2)
message = Message(message="Let's go out.", sender=ashley, recipient=julie)
db.session.add(message)
db.session.commit()
message = Message(message="Okie dokie.", sender=julie, recipient=ashley)
db.session.add(message)
db.session.commit()
messages = Message.query.all()
for m in messages:
	print(m.sender.username, "->", m.recipient.username, ":", m.message)

exit()
