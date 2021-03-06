"""empty message

Revision ID: 5a9f086a78e7
Revises: 2dc730773935
Create Date: 2020-07-23 17:19:25.650525

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '5a9f086a78e7'
down_revision = '2dc730773935'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('authusers',
    sa.Column('id', sa.String(length=255), nullable=False),
    sa.Column('name', sa.String(length=70), nullable=False),
    sa.Column('email', sa.String(length=70), nullable=False),
    sa.Column('profile_pic', sa.String(length=70), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('home_truths',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('content', sa.Text(), nullable=False),
    sa.Column('created_at', sa.DateTime(timezone=True), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('policy',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('content', sa.Text(), nullable=False),
    sa.Column('created_at', sa.DateTime(timezone=True), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(timezone=True), nullable=False),
    sa.Column('name', sa.String(length=70), nullable=False),
    sa.Column('email', sa.String(length=70), nullable=False),
    sa.Column('password', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('profiles')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('profiles',
    sa.Column('id', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('created_at', mysql.DATETIME(), nullable=False),
    sa.Column('name', mysql.VARCHAR(length=70), nullable=False),
    sa.Column('email', mysql.VARCHAR(length=70), nullable=False),
    sa.Column('password', mysql.VARCHAR(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset=u'latin1',
    mysql_engine=u'InnoDB'
    )
    op.drop_table('users')
    op.drop_table('policy')
    op.drop_table('home_truths')
    op.drop_table('authusers')
    # ### end Alembic commands ###
