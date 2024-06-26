"""add foreign key to Review

Revision ID: 865f6e885e83
Revises: ccf675fbd5b5
Create Date: 2024-04-07 11:16:32.003591

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '865f6e885e83'
down_revision = 'ccf675fbd5b5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('reviews', sa.Column('employee_id', sa.Integer(), nullable=True))
    op.create_foreign_key(op.f('fk_reviews_employee_id_employees'), 'reviews', 'employees', ['employee_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(op.f('fk_reviews_employee_id_employees'), 'reviews', type_='foreignkey')
    op.drop_column('reviews', 'employee_id')
    # ### end Alembic commands ###
