"""empty message

Revision ID: 5c7c7966beff
Revises: 
Create Date: 2022-07-15 14:54:23.037297

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5c7c7966beff'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('transactions',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('period', sa.String(length=100), nullable=False),
    sa.Column('value', sa.Integer(), nullable=False),
    sa.Column('status', sa.String(length=50), nullable=True),
    sa.Column('unit', sa.String(length=50), nullable=True),
    sa.Column('subject', sa.String(length=50), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('transactions')
    # ### end Alembic commands ###
