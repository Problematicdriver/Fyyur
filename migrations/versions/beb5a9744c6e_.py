"""empty message

Revision ID: beb5a9744c6e
Revises: a57688ff42f1
Create Date: 2020-01-31 01:47:34.316576

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'beb5a9744c6e'
down_revision = 'a57688ff42f1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Show', sa.Column('artist_id', sa.Integer(), nullable=True))
    op.add_column('Show', sa.Column('id', sa.Integer(), nullable=False))
    op.add_column('Show', sa.Column('start_time', sa.DateTime(), nullable=False))
    op.add_column('Show', sa.Column('venue_id', sa.Integer(), nullable=True))
    op.drop_constraint('Show_Venue_id_fkey', 'Show', type_='foreignkey')
    op.drop_constraint('Show_Artist_id_fkey', 'Show', type_='foreignkey')
    op.create_foreign_key(None, 'Show', 'Artist', ['artist_id'], ['id'])
    op.create_foreign_key(None, 'Show', 'Venue', ['venue_id'], ['id'])
    op.drop_column('Show', 'Artist_id')
    op.drop_column('Show', 'Venue_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Show', sa.Column('Venue_id', sa.INTEGER(), autoincrement=False, nullable=False))
    op.add_column('Show', sa.Column('Artist_id', sa.INTEGER(), autoincrement=False, nullable=False))
    op.drop_constraint(None, 'Show', type_='foreignkey')
    op.drop_constraint(None, 'Show', type_='foreignkey')
    op.create_foreign_key('Show_Artist_id_fkey', 'Show', 'Artist', ['Artist_id'], ['id'])
    op.create_foreign_key('Show_Venue_id_fkey', 'Show', 'Venue', ['Venue_id'], ['id'])
    op.drop_column('Show', 'venue_id')
    op.drop_column('Show', 'start_time')
    op.drop_column('Show', 'id')
    op.drop_column('Show', 'artist_id')
    # ### end Alembic commands ###