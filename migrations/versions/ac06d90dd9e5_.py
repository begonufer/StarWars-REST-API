"""empty message

Revision ID: ac06d90dd9e5
Revises: ebd1044bc588
Create Date: 2023-09-09 09:10:52.106472

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ac06d90dd9e5'
down_revision = 'ebd1044bc588'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('character', schema=None) as batch_op:
        batch_op.drop_constraint('character_element_id_fkey', type_='foreignkey')
        batch_op.drop_column('element_id')

    with op.batch_alter_table('favorites', schema=None) as batch_op:
        batch_op.add_column(sa.Column('planet_id', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('character_id', sa.Integer(), nullable=True))
        batch_op.drop_constraint('favorites_characters_fkey', type_='foreignkey')
        batch_op.drop_constraint('favorites_planets_fkey', type_='foreignkey')
        batch_op.create_foreign_key(None, 'character', ['character_id'], ['id'])
        batch_op.create_foreign_key(None, 'planet', ['planet_id'], ['id'])
        batch_op.drop_column('planets')
        batch_op.drop_column('characters')

    with op.batch_alter_table('planet', schema=None) as batch_op:
        batch_op.drop_constraint('planet_element_id_fkey', type_='foreignkey')
        batch_op.drop_column('element_id')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('planet', schema=None) as batch_op:
        batch_op.add_column(sa.Column('element_id', sa.INTEGER(), autoincrement=False, nullable=True))
        batch_op.create_foreign_key('planet_element_id_fkey', 'elements', ['element_id'], ['id'])

    with op.batch_alter_table('favorites', schema=None) as batch_op:
        batch_op.add_column(sa.Column('characters', sa.INTEGER(), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('planets', sa.INTEGER(), autoincrement=False, nullable=True))
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.create_foreign_key('favorites_planets_fkey', 'planet', ['planets'], ['id'])
        batch_op.create_foreign_key('favorites_characters_fkey', 'character', ['characters'], ['id'])
        batch_op.drop_column('character_id')
        batch_op.drop_column('planet_id')

    with op.batch_alter_table('character', schema=None) as batch_op:
        batch_op.add_column(sa.Column('element_id', sa.INTEGER(), autoincrement=False, nullable=True))
        batch_op.create_foreign_key('character_element_id_fkey', 'elements', ['element_id'], ['id'])

    # ### end Alembic commands ###
