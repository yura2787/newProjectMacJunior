from sqlalchemy import String
from datetime import datetime
from applications.database.base_model import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.sql import func
import uuid

class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True)
    created_at: Mapped[datetime] = mapped_column(default=func.now())
    update_at: Mapped[datetime] = mapped_column(default=func.now(), onupdate=func.now())
    uuid_data: Mapped[uuid.UUID] = mapped_column(default=uuid.uuid4)


    name: Mapped[str] = mapped_column(String[100], index=True)
    email: Mapped[str] = mapped_column(unique=True)
    hashed_password: Mapped[str] = mapped_column(nullable=False)

