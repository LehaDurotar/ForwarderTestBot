"""First migration

Revision ID: 330668cd2e5d
Revises: 
Create Date: 2021-01-31 13:54:48.629452

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "330668cd2e5d"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "vkpostdevdata",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("idx", sa.Integer(), nullable=False),
        sa.Column("attachments", sa.Boolean(), nullable=True),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.text("now()"), nullable=True),
        sa.Column("updated_at", sa.DateTime(timezone=True), server_default=sa.text("now()"), nullable=True),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("id"),
        sa.UniqueConstraint("idx"),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("vkpostdevdata")
    # ### end Alembic commands ###
