"""empty message

Revision ID: 5560fb7c06c7
Revises: 
Create Date: 2020-10-11 17:27:00.090143

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5560fb7c06c7'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('sensors',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('s_type', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('tasks',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.Text(), nullable=False),
    sa.Column('s_type', sa.String(length=500), nullable=False),
    sa.Column('condition', sa.String(length=500), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('password', sa.String(length=255), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('conditions',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('condition', sa.String(length=500), nullable=False),
    sa.Column('c_type', sa.Integer(), nullable=True),
    sa.Column('sensor_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['sensor_id'], ['sensors.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('configurations',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('task_id', sa.Integer(), nullable=True),
    sa.Column('notifications', sa.Boolean(), nullable=False),
    sa.Column('repeat', sa.Integer(), nullable=False),
    sa.Column('added_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['task_id'], ['tasks.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('configurations')
    op.drop_table('conditions')
    op.drop_table('users')
    op.drop_table('tasks')
    op.drop_table('sensors')
    # ### end Alembic commands ###