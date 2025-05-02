from sqlalchemy import String
from datetime import datetime
from applications.database.base_models import Base
from sqlalchemy.orm import Mapper, mapped_column
from sqlalchemy.sql import func
import uuid

class User(Base):
    __tablename__ = 'users'

    id: Mapper[int] = mapped_column(primary_key=True)
    created_at: Mapper[datetime] = mapped_column(default=func.now())
    update_at: Mapper[datetime] = mapped_column(default=func.now(), onupdate=func.now())
    uuid_data: Mapper[uuid.UUID] = mapped_column(default=uuid.uuid4)


    name: Mapper[str] = mapped_column(String[100], index=True)
    email: Mapper[str] = mapped_column(unique=True)
    hashed_password = Mapper[str] = mapped_column(nullable=False)

