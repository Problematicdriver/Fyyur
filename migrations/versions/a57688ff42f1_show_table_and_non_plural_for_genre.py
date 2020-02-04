"""show table and non plural for genre

Revision ID: a57688ff42f1
Revises: b17f8ed8b1b2
Create Date: 2020-01-30 21:31:43.229549

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a57688ff42f1'
down_revision = 'b17f8ed8b1b2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Show',
    sa.Column('Artist_id', sa.Integer(), nullable=False),
    sa.Column('Venue_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['Artist_id'], ['Artist.id'], ),
    sa.ForeignKeyConstraint(['Venue_id'], ['Venue.id'], ),
    sa.PrimaryKeyConstraint('Artist_id', 'Venue_id')
    )
    op.add_column('Artist', sa.Column('genre', sa.String(length=120), nullable=True))
    op.drop_column('Artist', 'genres')
    op.add_column('Venue', sa.Column('genre', sa.String(length=120), nullable=True))
    op.drop_column('Venue', 'genres')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Venue', sa.Column('genres', sa.VARCHAR(length=120), autoincrement=False, nullable=True))
    op.drop_column('Venue', 'genre')
    op.add_column('Artist', sa.Column('genres', sa.VARCHAR(length=120), autoincrement=False, nullable=True))
    op.drop_column('Artist', 'genre')
    op.drop_table('Show')
    # ### end Alembic commands ###
