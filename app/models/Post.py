from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
from sqlalchemy import text

from app.extensions import db
from .User import User

"""
Post <-> User
"""


class Post(db.Model):
    __tablename__ = 'user_post'

    public_id = db.Column(UUID(as_uuid=True),
                          unique=True,
                          server_default=text("uuid_generate_v4()"))
    id = db.Column(db.Integer, index=True,
                   autoincrement=True, primary_key=True)
    # ---- Relationships ---- #
    user_id = db.Column(db.Integer, db.ForeignKey(
        'user_table.id'), primary_key=True)
    # ---- Basic Post details ---- #
    body = db.Column(db.String(280), nullable=False)
    image = db.Column(db.String(300))
    # ---- Meta data ---- #
    created_at = db.Column(db.DateTime, index=True, server_default=func.now())
    updated_at = db.Column(db.DateTime, index=True,
                           server_default=func.now())  # ToDo: fix auto updation

    def to_dict(self):
        author = User.query.filter_by(id=self.user_id).first()
        data = {
            'public_id': self.public_id,
            'author': {
                'name': author.name,
                'image': author.image,
                'headline': author.headline
            },
            'body': self.body,
            'image': self.image,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }

        return data

    def from_dict(self, data):
        for field in ['user_id', 'body', 'image']:
            if field in data:
                setattr(self, field, data[field])

    def __repr__(self):
        return '<Post {}>'.format(self.id)
