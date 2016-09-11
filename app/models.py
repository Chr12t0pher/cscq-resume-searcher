from app import db


class Comments(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    reddit_id = db.Column(db.String(8), unique=True)
    reddit_post_id = db.Column(db.String(8))
    reddit_user = db.Column(db.String(32))
    text = db.Column(db.String(2048))
    html = db.Column(db.String(2048))
    url = db.Column(db.String(128))
    keywords = db.relationship("Keywords", backref="comments", lazy="dynamic")


class Keywords(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    post_id = db.Column(db.Integer, db.ForeignKey("comments.id"))
    keyword = db.Column(db.String(32))
