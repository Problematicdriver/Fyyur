"""empty message

Revision ID: 792b5cd9e178
Revises: 3cf1d4bd03b3
Create Date: 2020-02-03 03:43:39.891041

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '792b5cd9e178'
down_revision = '3cf1d4bd03b3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('Artist', 'seeking_description')
    op.drop_column('Artist', 'seeking_venue')
    op.drop_column('Artist', 'website')
    op.drop_column('Venue', 'seeking_description')
    op.drop_column('Venue', 'seeking_talent')
    op.drop_column('Venue', 'website')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Venue', sa.Column('website', sa.VARCHAR(length=120), autoincrement=False, nullable=True))
    op.add_column('Venue', sa.Column('seeking_talent', sa.BOOLEAN(), autoincrement=False, nullable=True))
    op.add_column('Venue', sa.Column('seeking_description', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.add_column('Artist', sa.Column('website', sa.VARCHAR(length=120), autoincrement=False, nullable=True))
    op.add_column('Artist', sa.Column('seeking_venue', sa.BOOLEAN(), autoincrement=False, nullable=True))
    op.add_column('Artist', sa.Column('seeking_description', sa.VARCHAR(), autoincrement=False, nullable=True))
    # ### end Alembic commands ###