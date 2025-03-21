"""initial migration

Revision ID: 562bdff3b083
Revises: 
Create Date: 2025-03-18 10:04:16.422819

"""
import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '562bdff3b083'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('email', sa.String(length=512), nullable=False),
    sa.Column('password', sa.String(length=512), nullable=False),
    sa.Column('id', mysql.CHAR(length=36), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    # ### end Alembic commands ###
