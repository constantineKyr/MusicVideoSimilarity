"""add genre column to video

Revision ID: 5b4c73da0ebd
Revises: 9838f01ccec8
Create Date: 2020-02-08 11:30:23.738921

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5b4c73da0ebd'
down_revision = '9838f01ccec8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('video', sa.Column('genre', sa.String(length=64), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('video', 'genre')
    # ### end Alembic commands ###