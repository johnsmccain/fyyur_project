"""empty message

Revision ID: 5730ba3257ad
Revises: 54aad68d69af
Create Date: 2022-05-31 18:44:02.729243

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5730ba3257ad'
down_revision = '54aad68d69af'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Artist', sa.Column('address', sa.String(length=120), nullable=True))
    op.drop_column('Artist', 'Address')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Artist', sa.Column('Address', sa.VARCHAR(length=120), autoincrement=False, nullable=True))
    op.drop_column('Artist', 'address')
    # ### end Alembic commands ###
