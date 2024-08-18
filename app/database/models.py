from database.config import Base

from sqlalchemy.orm import Mapped, mapped_column


from sqlalchemy import TIMESTAMP
import datetime
from sqlalchemy.sql import func


class Users(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=True)
    telegram_id: Mapped[int] = mapped_column(nullable=True, unique=True)
    created_at: Mapped[datetime.datetime] = mapped_column(
        TIMESTAMP(timezone=True),
        server_default=func.now(),
        nullable=False
    )
    updated_at: Mapped[datetime.datetime] = mapped_column(
        TIMESTAMP(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False
    )


