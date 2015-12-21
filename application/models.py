from application import db

class Goat(db.Model):
    __tablename__ = 'goats'

    id = db.Column(db.Integer, primary_key=True, index=True)
    url = db.Column(db.String(500), unique=True)
    votes = db.Column(db.Integer, unique=False)
    
    def __init__(self, url, votes):
        self.url = url
        self.votes = votes

    def __repr__(self):
        return "<Goat(url='%s', votes='%s')>" % (self.url, self.votes)

class Submission(db.Model):
	__tablename__ = 'submissions'

	id = db.Column(db.Integer, primary_key=True, index=True)
	url = db.Column(db.String(500), unique=True)

	def __init__(self, url):
		self.url = url

	def __repr__(self):
		return "<Goat submission {}, url={}>".format(self.id, self.url)