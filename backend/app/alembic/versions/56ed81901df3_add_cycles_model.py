"""Add cycles model

Revision ID: 56ed81901df3
Revises: 5784d8c72650
Create Date: 2020-04-30 11:32:52.454711

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '56ed81901df3'
down_revision = '5784d8c72650'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('cycle',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('cycle_type', sa.String(), nullable=True),
    sa.Column('cycle_date', sa.DateTime(), nullable=True),
    sa.Column('snake_id', sa.Integer(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['snake_id'], ['snake.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_cycle_id'), 'cycle', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_cycle_id'), table_name='cycle')
    op.drop_table('cycle')
    # ### end Alembic commands ###