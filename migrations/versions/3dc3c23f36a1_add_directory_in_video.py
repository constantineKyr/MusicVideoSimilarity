"""add directory in Video

Revision ID: 3dc3c23f36a1
Revises: 99751f48a936
Create Date: 2020-01-11 19:00:50.154261

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3dc3c23f36a1'
down_revision = '99751f48a936'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('video', sa.Column('directory', sa.String(length=250), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('video', 'directory')
    # ### end Alembic commands ###
