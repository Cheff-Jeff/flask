from app import db

class User(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(20), unique=True, nullable=False)
  password = db.Column(db.String(60), nullable=False)
  IPs = db.relationship('IP', backref='owner', lazy=True)

  def __repr__(self):
    return f"User('{self.username}')"

class IP(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  ip = db.Column(db.String(255), nullable=False)
  user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

  def __repr__(self):
    return f"Post('{self.ip}')"