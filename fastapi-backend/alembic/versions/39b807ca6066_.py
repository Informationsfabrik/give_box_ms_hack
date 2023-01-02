"""Create initial schema.

Revision ID: 39b807ca6066
Revises:
Create Date: 2022-09-26 15:27:03.539930

"""
import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision = "39b807ca6066"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "Users",
        sa.Column("id", sa.Integer(), nullable=False, primary_key=True, index=True),
        sa.Column("email", sa.String()),
        sa.Column("password", sa.String()),
        sa.Column("firstname", sa.String()),
        sa.Column("lastname", sa.String()),
        sa.Column("street", sa.String()),
        sa.Column("house_number", sa.Integer()),
        sa.Column("zip_code", sa.Integer()),
        sa.Column("city", sa.String()),
    )

    op.create_table(
        "GiveBoxes",
        sa.Column("id", sa.Integer(), nullable=False, primary_key=True, index=True),
        sa.Column("longitude", sa.Float()),
        sa.Column("latitude", sa.Float()),
        sa.Column("opening_hours", sa.String()),
        sa.Column("is_temporary", sa.Boolean()),
        sa.Column("title", sa.String()),
        sa.Column("description", sa.String()),
        sa.Column("extern_link", sa.String()),
        sa.Column("last_confirmation_date", sa.DateTime(), nullable=True),
        sa.Column("maintainer_info", sa.String()),
        sa.Column("maintenance_needed", sa.Boolean()),
        sa.Column("image_id", sa.String()),
        sa.Column("content", sa.JSON(), default={}, nullable=True, none_as_null=True),
        sa.Column("street", sa.String()),
        sa.Column("house_number", sa.Integer()),
        sa.Column("zip_code", sa.Integer()),
        sa.Column("city", sa.String()),
    )
    op.create_table(
        "Comments",
        sa.Column("id", sa.Integer(), nullable=False, primary_key=True, index=True),
        sa.Column("box_id", sa.Integer(), sa.ForeignKey("GiveBoxes.id")),
        sa.Column("user_id", sa.Integer(), sa.ForeignKey("Users.id")),
        sa.Column("text", sa.String()),
        sa.Column("timestamp", sa.DateTime()),
    )

    op.create_table(
        "Images",
        sa.Column("id", sa.Integer(), nullable=False, primary_key=True, index=True),
        sa.Column("box_id", sa.Integer(), sa.ForeignKey("GiveBoxes.id")),
        sa.Column("path", sa.String()),
        sa.Column("is_title_image", sa.Boolean()),
    )

    op.create_table(
        "user_givebox_association",
        sa.Column("user_id", sa.Integer(), sa.ForeignKey("Users.id")),
        sa.Column("box_id", sa.Integer(), sa.ForeignKey("GiveBoxes.id")),
    )


def downgrade() -> None:
    op.drop_table("Users")
    op.drop_table("GiveBoxes")
    op.drop_table("Comments")
    op.drop_table("Images")
    op.drop_table("user_givebox_association")
