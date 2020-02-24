"""make weight non nullable

Revision ID: 4241ced50e71
Revises: b9fefa1a0da0
Create Date: 2019-12-16 20:25:08.997774

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '4241ced50e71'
down_revision = 'b9fefa1a0da0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('feature', 'weight',
               existing_type=postgresql.DOUBLE_PRECISION(precision=53),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('feature', 'weight',
               existing_type=postgresql.DOUBLE_PRECISION(precision=53),
               nullable=True)
    # ### end Alembic commands ###
