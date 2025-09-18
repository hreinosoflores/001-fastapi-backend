"""create todos table

Revision ID: 8a2f771c5602
Revises: 
Create Date: 2025-09-18 11:53:40.742919

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8a2f771c5602'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.execute("""
    create table todos(
        id bigserial primary key,
        name text,
        completed boolean not null default false
    )
    """)


def downgrade():
    op.execute("drop table todos;")
