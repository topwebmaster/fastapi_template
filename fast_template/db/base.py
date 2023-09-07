from sqlalchemy.orm import DeclarativeBase

from fast_template.db.meta import meta


class Base(DeclarativeBase):
    """Base for all models."""

    metadata = meta
