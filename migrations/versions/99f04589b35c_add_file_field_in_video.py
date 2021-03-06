"""add file field in Video

Revision ID: 99f04589b35c
Revises: 1549c2996920
Create Date: 2019-12-14 07:53:50.149692

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '99f04589b35c'
down_revision = '1549c2996920'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index(op.f('ix_segment_video_id'), 'segment', ['video_id'], unique=False)
    op.add_column('video', sa.Column('file', sa.String(length=250), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('video', 'file')
    op.drop_index(op.f('ix_segment_video_id'), table_name='segment')
    # ### end Alembic commands ###
