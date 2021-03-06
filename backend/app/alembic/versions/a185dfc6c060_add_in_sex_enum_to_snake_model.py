"""Add in sex enum to Snake model

Revision ID: a185dfc6c060
Revises: e47796461a4d
Create Date: 2020-04-27 23:46:06.200954

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a185dfc6c060'
down_revision = 'e47796461a4d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('snake', sa.Column('sex', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('snake', 'sex')
    # ### end Alembic commands ###
