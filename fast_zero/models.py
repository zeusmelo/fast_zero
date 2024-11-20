from datetime import datetime

from sqlalchemy import func
from sqlalchemy.orm import Mapped, mapped_column, registry

# registra metadados
table_registry = registry()


@table_registry.mapped_as_dataclass
class User:
    __tablename__ = 'users'  # registro escalar init false, db inicializa
    id: Mapped[int] = mapped_column(init=False, primary_key=True, autoincrement=True)
    username: Mapped[str] = mapped_column(unique=True)
    password: Mapped[str]
    email: Mapped[str] = mapped_column(unique=True)
    created_at: Mapped[datetime] = mapped_column(
        init=False, server_default=func.now()
    )
