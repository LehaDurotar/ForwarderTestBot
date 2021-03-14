"""Add 'idx' field into Forward model

Revision ID: 0daf2979c88c
Revises: f7914a248a90
Create Date: 2021-03-14 10:35:25.754862

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "0daf2979c88c"
down_revision = "f7914a248a90"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, "blocklist", ["source_id"])
    op.add_column("forwards", sa.Column("idx", sa.String(), nullable=True))
    op.create_unique_constraint(None, "forwards", ["idx"])
    op.create_unique_constraint(None, "forwards", ["id"])
    op.create_unique_constraint(None, "subscribers", ["id"])
    op.create_unique_constraint(None, "targets", ["id"])
    op.create_unique_constraint(None, "users", ["id"])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, "users", type_="unique")
    op.drop_constraint(None, "targets", type_="unique")
    op.drop_constraint(None, "subscribers", type_="unique")
    op.drop_constraint(None, "forwards", type_="unique")
    op.drop_constraint(None, "forwards", type_="unique")
    op.drop_column("forwards", "idx")
    op.drop_constraint(None, "blocklist", type_="unique")
    # ### end Alembic commands ###