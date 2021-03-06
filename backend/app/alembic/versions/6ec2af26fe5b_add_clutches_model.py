"""Add clutches model

Revision ID: 6ec2af26fe5b
Revises: 8efede552a27
Create Date: 2020-04-30 21:12:10.611258

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6ec2af26fe5b'
down_revision = '8efede552a27'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('clutch',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('custom_id', sa.Integer(), nullable=True),
    sa.Column('clutch_type', sa.String(), nullable=True),
    sa.Column('laid_date', sa.DateTime(), nullable=True),
    sa.Column('due_date', sa.DateTime(), nullable=True),
    sa.Column('egg_count', sa.Integer(), nullable=True),
    sa.Column('good_egg_count', sa.Integer(), nullable=True),
    sa.Column('bad_egg_count', sa.Integer(), nullable=True),
    sa.Column('snake_id', sa.Integer(), nullable=True),
    sa.Column('father_id', sa.Integer(), nullable=True),
    sa.Column('notes', sa.String(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['father_id'], ['snake.id'], ),
    sa.ForeignKeyConstraint(['snake_id'], ['snake.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_clutch_custom_id'), 'clutch', ['custom_id'], unique=False)
    op.create_index(op.f('ix_clutch_id'), 'clutch', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_clutch_id'), table_name='clutch')
    op.drop_index(op.f('ix_clutch_custom_id'), table_name='clutch')
    op.drop_table('clutch')
    # ### end Alembic commands ###
