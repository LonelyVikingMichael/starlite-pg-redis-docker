from typing import Annotated
from uuid import UUID

from sqlalchemy import ForeignKey, Uuid
from sqlalchemy.orm import Mapped, mapped_column, relationship
from starlite.contrib.sqlalchemy.base import AuditBase, Base
from starlite.contrib.sqlalchemy.dto import SQLAlchemyDTO
from starlite.dto.factory.config import DTOConfig
from starlite_users.adapter.sqlalchemy.mixins import SQLAlchemyUserMixin, SQLAlchemyRoleMixin


class Role(SQLAlchemyRoleMixin):
    __tablename__ = "role"


class UserRole(Base):
    __tablename__ = "user_role"

    role_id: Mapped[UUID] = mapped_column(Uuid(), ForeignKey("role.id"))
    user_id: Mapped[UUID] = mapped_column(Uuid(), ForeignKey("user.id"))


class User(SQLAlchemyUserMixin, AuditBase):
    __tablename__ = "user"

    roles: Mapped[list[Role]] = relationship(Role, secondary="user_role", lazy="joined")


UserWriteDTO = SQLAlchemyDTO[Annotated[User, DTOConfig(exclude={"id"})]]
UserUpdateDTO = SQLAlchemyDTO[Annotated[User, DTOConfig(exclude={"id", "email", "roles"})]]
UserReadDTO = SQLAlchemyDTO[User]
