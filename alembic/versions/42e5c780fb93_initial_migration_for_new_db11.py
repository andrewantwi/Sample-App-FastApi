"""Initial migration for new DB11

Revision ID: 42e5c780fb93
Revises: 63c0312effc1
Create Date: 2025-02-20 16:32:46.466993

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '42e5c780fb93'
down_revision: Union[str, None] = '63c0312effc1'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('cart_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'users', 'carts', ['cart_id'], ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'users', type_='foreignkey')
    op.drop_column('users', 'cart_id')
    # ### end Alembic commands ###
