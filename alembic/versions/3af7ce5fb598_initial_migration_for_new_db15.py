"""Initial migration for new DB15

Revision ID: 3af7ce5fb598
Revises: 0a1a37dc8d9d
Create Date: 2025-02-21 16:47:08.524091

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3af7ce5fb598'
down_revision: Union[str, None] = '0a1a37dc8d9d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###
