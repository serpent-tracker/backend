"""Add matings model and references to snake model

Revision ID: 5784d8c72650
Revises: 8a020dbf530e
Create Date: 2020-04-30 10:21:40.614424

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5784d8c72650'
down_revision = '8a020dbf530e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('mating',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('event', sa.String(), nullable=True),
    sa.Column('event_date', sa.DateTime(), nullable=True),
    sa.Column('snake_id', sa.Integer(), nullable=True),
    sa.Column('mate_id', sa.Integer(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['mate_id'], ['snake.id'], ),
    sa.ForeignKeyConstraint(['snake_id'], ['snake.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_mating_id'), 'mating', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_mating_id'), table_name='mating')
    op.drop_table('mating')
    # ### end Alembic commands ###
