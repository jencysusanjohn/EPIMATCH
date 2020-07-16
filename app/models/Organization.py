from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
from sqlalchemy import text


from app.extensions import db

"""
Organization <-> User
"""


class Organization(db.Model):
    __tablename__ = 'user_organization'

    public_id = db.Column(UUID(as_uuid=True),
                          unique=True,
                          server_default=text("uuid_generate_v4()"))
    id = db.Column(db.Integer, index=True,
                   autoincrement=True, primary_key=True)
    # ---- Relationships ---- #
    user_id = db.Column(db.Integer, db.ForeignKey(
        'user_table.id'), primary_key=True)
    # ---- Basic Organization details ---- #
    name = db.Column(db.String(255), nullable=False)
    # ---- Meta data ---- #
    created_at = db.Column(db.DateTime, index=True, server_default=func.now())
    updated_at = db.Column(db.DateTime, index=True,
                           server_default=func.now())  # ToDo: fix auto updation

    def to_dict(self):
        data = {
            'public_id': self.public_id,
            'name': self.name,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }

        return data

    def from_dict(self, data):
        for field in ['name', 'user_id']:
            if field in data:
                setattr(self, field, data[field])

    def __repr__(self):
        return '<Organization {}>'.format(self.id)
