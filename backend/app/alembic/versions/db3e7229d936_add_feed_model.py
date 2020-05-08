"""Add feed model

Revision ID: db3e7229d936
Revises: 845437c1292a
Create Date: 2020-04-28 19:01:22.438357

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'db3e7229d936'
down_revision = '845437c1292a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('feed',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('prey', sa.String(), nullable=True),
    sa.Column('prey_type', sa.String(), nullable=True),
    sa.Column('prey_size', sa.String(), nullable=True),
    sa.Column('feed_date', sa.DateTime(), nullable=True),
    sa.Column('count', sa.Integer(), nullable=True),
    sa.Column('snake_id', sa.Integer(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['snake_id'], ['snake.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_feed_id'), 'feed', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_feed_id'), table_name='feed')
    op.drop_table('feed')
    # ### end Alembic commands ###