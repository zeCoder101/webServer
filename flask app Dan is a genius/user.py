from flask_login import UserMixin

class User(UserMixin):
	def __init__(self, id, name, password):
		self.id = id
		self.name = name
		self.password = password


def get_id(username):
	users = [o for o in UserDB if o["id"] == username]
	if users:
		user = users[0]
		return User(user["id"], user["name"], user["pwd"])
	return None


UserDB = [
	{"id": "zeCoder", "name": "zeCoder", "pwd": "zeCoder#zeBest101"},
	{"id": "darkjedi", "name": "Dan", "pwd": "llamas4EVAR!"},
	{"id": "nicobuster", "name": "Daddy!", "pwd": "GlOuPsInOu"},
	{"id": "emma", "name": "lil sis", "pwd": "emma"},
	{"id": "fireKing66", "name": "Sean", "pwd": "jeSuismeilleur_enPython"}
]
