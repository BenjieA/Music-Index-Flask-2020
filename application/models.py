from application import db

class Songs(db.Model):
	songID =  db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(40), nullable=False)
	artist = db.Column(db.String(40), nullable=False)
	year = db.Column(db.Integer(), nullable=False)
	#lyricUser = db.Column(db.String(), nullable=False, foreign_key=True)
	songLyric = db.Column(db.String(1000), nullable=False, unique=True)
	#remixID = db.Column(db.Integer, foreign_key=True)

	def __repr__(self):
		return ''.join([
			'Song:  ', self.title, ' ', '\r\n',
			'Artist: ', self.artist, '\r\n', 
			'Lyrics: ', self.songLyric , '\r\n',
			'Year of Release:', self.year

		])
