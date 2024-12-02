from fastapi_users.authentication import BearerTransport

from config import settings

bearer_transport = BearerTransport(
    tokenUrl=settings.API.bearer_token_url,
)
