from fastapi_users import FastAPIUsers

from authentication.backend import authentication_backend
from authentication.user_manager import get_user_manager
from models import User

fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [authentication_backend],
)