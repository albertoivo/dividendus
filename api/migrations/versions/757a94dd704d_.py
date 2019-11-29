"""empty message

Revision ID: 757a94dd704d
Revises: 79f586e0654f
Create Date: 2019-11-28 18:42:29.677086

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '757a94dd704d'
down_revision = '79f586e0654f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    # ### end Alembic commands ###