"""${message}

Revision ID: ${up_revision}
Revises: ${down_revision | comma,n}
Create Date: ${create_date}

"""
from alembic import op
import sqlalchemy as sa
${imports if imports else ""}

# revision identifiers, used by Alembic.
revision = ${repr(up_revision)}
down_revision = ${repr(down_revision)}
branch_labels = ${repr(branch_labels)}
depends_on = ${repr(depends_on)}


triggers = [
    """
    CREATE OR REPLACE FUNCTION trigger_set_timestamp()
    RETURNS TRIGGER AS $$
    BEGIN
        NEW.updated_at = NOW() AT TIME ZONE 'UTC'; -- UTC_TIMESTAMP() can't be used in a postgres DB.
        RETURN NEW;
    END;
    $$ LANGUAGE plpgsql;
    """,
    """
    CREATE OR REPLACE TRIGGER set_timestamp
    BEFORE UPDATE ON sun -- sun is a database table name
    FOR EACH ROW
    EXECUTE PROCEDURE trigger_set_timestamp()
    """
]


def upgrade() -> None:
    ${upgrades if upgrades else "pass"}

    for trigger in triggers:
        op.execute(trigger)


def downgrade() -> None:
    ${downgrades if downgrades else "pass"}
