"""Add created_at column to Snake model

Revision ID: 680ce6942c7e
Revises: d4867f3a4c0a
Create Date: 2020-04-27 00:49:11.088849

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '680ce6942c7e'
down_revision = 'd4867f3a4c0a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('snake', sa.Column('created_at', sa.DateTime(), nullable=True))
    op.alter_column('user', 'email',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.alter_column('user', 'hashed_password',
               existing_type=sa.VARCHAR(),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('user', 'hashed_password',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.alter_column('user', 'email',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.drop_column('snake', 'created_at')
    # ### end Alembic commands ###