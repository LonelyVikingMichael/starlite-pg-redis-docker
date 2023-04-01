from starlite_users.config import StarliteUsersConfig, AuthHandlerConfig, RegisterHandlerConfig, VerificationHandlerConfig, PasswordResetHandlerConfig

from .. import settings
from .model import Role, User, UserReadDTO, UserUpdateDTO, UserWriteDTO
from .service import UserService

startlite_users_config = StarliteUsersConfig(
    auth_backend=settings.auth.BACKEND,
    secret=settings.api.SECRET_KEY,
    user_model=User,
    user_service_class=UserService,
    user_create_dto=UserWriteDTO,
    user_read_dto=UserReadDTO,
    user_update_dto=UserUpdateDTO,
    role_model=Role,
    auth_handler_config=AuthHandlerConfig(),
    password_reset_handler_config=PasswordResetHandlerConfig(),
    register_handler_config=RegisterHandlerConfig(),
    verification_handler_config=VerificationHandlerConfig(),
)
