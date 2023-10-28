"""Create phone number for user column

Revision ID: db3fd711d365
Revises: 
Create Date: 2023-10-29 01:50:47.798656

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'db3fd711d365'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('users',sa.Column('phone_number',sa.String(),nullable=True))


def downgrade() -> None:
    op.drop_column('users','phone_number')
