from email.message import EmailMessage

from starlite_users.service import BaseUserService

from app.lib import email, settings

from .model import User


class UserService(BaseUserService):
    async def send_verification_token(self, user: User, token: str) -> None:
        """Sends an email with a user verification token.

        Args:
            user: The user to verify.
            token: The JWT to include in the message.
        """
        message = EmailMessage()
        message["From"] = settings.email.SENDER
        message["To"] = user.email
        message["Subject"] = settings.auth.VERIFY_EMAIL_SUBJECT
        message.set_content("")
        async with email.client:
            await email.client.send_message(message)
