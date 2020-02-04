"""adding attributes to the models

Revision ID: 3cf1d4bd03b3
Revises: beb5a9744c6e
Create Date: 2020-01-31 13:40:04.223150

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3cf1d4bd03b3'
down_revision = 'beb5a9744c6e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Artist', sa.Column('genres', sa.ARRAY(sa.String()), nullable=True))
    op.add_column('Artist', sa.Column('seeking_description', sa.String(), nullable=True))
    op.add_column('Artist', sa.Column('seeking_venue', sa.Boolean(), nullable=True))
    op.add_column('Artist', sa.Column('website', sa.String(length=120), nullable=True))
    op.drop_column('Artist', 'genre')
    op.add_column('Venue', sa.Column('genres', sa.ARRAY(sa.String()), nullable=False))
    op.add_column('Venue', sa.Column('seeking_description', sa.String(), nullable=True))
    op.add_column('Venue', sa.Column('seeking_talent', sa.Boolean(), nullable=True))
    op.add_column('Venue', sa.Column('website', sa.String(length=120), nullable=True))
    op.drop_column('Venue', 'genre')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Venue', sa.Column('genre', sa.VARCHAR(length=120), autoincrement=False, nullable=True))
    op.drop_column('Venue', 'website')
    op.drop_column('Venue', 'seeking_talent')
    op.drop_column('Venue', 'seeking_description')
    op.drop_column('Venue', 'genres')
    op.add_column('Artist', sa.Column('genre', sa.VARCHAR(length=120), autoincrement=False, nullable=True))
    op.drop_column('Artist', 'website')
    op.drop_column('Artist', 'seeking_venue')
    op.drop_column('Artist', 'seeking_description')
    op.drop_column('Artist', 'genres')
    # ### end Alembic commands ###
