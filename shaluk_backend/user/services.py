import dataclasses
import datetime
import jwt
from typing import TYPE_CHECKING
from django.conf import settings
from . import models

if TYPE_CHECKING:
    from .models import User


@dataclasses.dataclass
class UserDataClass:
    first_name: str
    last_name: str
    email: str
    address: str
    phone_number: str
    password: str = None
    id: int = None

    @classmethod
    def from_instance(cls, user: "User") -> "UserDataClass":
        return cls(
            first_name=user.first_name,
            last_name=user.last_name,
            email=user.email,
            address=user.address,
            phone_number=user.phone_number,
            id=user.id,
        )


def create_user(user_dc: "UserDataClass") -> "UserDataClass":
    instance = models.User(
        first_name=user_dc.first_name, last_name=user_dc.last_name, email=user_dc.email, address=user_dc.address, phone_number=user_dc.phone_number
    )
    if user_dc.password is not None:
        instance.set_password(user_dc.password)

    instance.save()

    return UserDataClass.from_instance(instance)


def user_email_selector(email: str) -> "User":
    user = models.User.objects.filter(email=email).first()

    return user


def create_token(user_id: int, is_superuser: bool) -> str:
    payload = dict(
        id=user_id,
        is_superuser = is_superuser,
        exp=datetime.datetime.utcnow() + datetime.timedelta(hours=24),
        iat=datetime.datetime.utcnow(),
    )
    token = jwt.encode(payload, settings.JWT_SECRET, algorithm="HS256")

    return token