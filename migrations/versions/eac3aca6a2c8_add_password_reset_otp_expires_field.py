"""add password_reset_otp_expires field

Revision ID: eac3aca6a2c8
Revises: 7c16ee96b7df
Create Date: 2020-07-11 23:05:43.456430

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'eac3aca6a2c8'
down_revision = '7c16ee96b7df'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user_table', sa.Column('password_reset_otp_expires', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user_table', 'password_reset_otp_expires')
    # ### end Alembic commands ###
