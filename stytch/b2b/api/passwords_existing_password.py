# !!!
# WARNING: This file is autogenerated
# Only modify code within MANUAL() sections
# or your changes may be overwritten later!
# !!!

from typing import Any, Dict, Optional

from stytch.b2b.models.passwords_existing_password import ResetResponse
from stytch.core.api_base import ApiBase
from stytch.core.http.client import AsyncClient, SyncClient


class ExistingPassword:
    def __init__(
        self,
        api_base: ApiBase,
        sync_client: SyncClient,
        async_client: AsyncClient,
    ) -> None:
        self.api_base = api_base
        self.sync_client = sync_client
        self.async_client = async_client

    @property
    def sub_url(self) -> str:
        return "passwords/existing_password"

    def reset(
        self,
        organization_id: str,
        email_address: str,
        existing_password: str,
        new_password: str,
        session_token: Optional[str] = None,
        session_jwt: Optional[str] = None,
        session_duration_minutes: Optional[int] = None,
        session_custom_claims: Optional[Dict[str, Any]] = None,
    ) -> ResetResponse:
        """Reset the member’s password using their existing password.

        Parameters:

        - `organization_id`: Globally unique UUID that identifies a specific Organization. The organization_id is critical to perform operations on an Organization, so be sure to preserve this value.

        - `email_address`: The email of the Member

        - `existing_password`: The member's current password that they supplied.

        - `new__password`: The member's elected new password.

        - `session_token`: A secret token for a given Stytch Session. Read more about session_token in our Session Management guide.

        - `session_jwt`: The JSON Web Token (JWT) for a given Stytch Session. Read more about session_token in our Session Management guide.

        - `session_duration_minutes`: The Session lifetime of this many minutes from now; minimum of 5 and a maximum of 129600 minutes (90 days). Note that a successful authentication will continue to extend the Session this many minutes.

        - `session_custom_claims`: Add a custom claims map to the Session being authenticated. Claims are only created if a Session is initialized by providing a value in Session duration minutes. Claims will be included on the Session object and in the JWT. To update a key in an existing Session, supply a new value. To delete a key, supply a null value.
          Custom claims made with reserved claims ("iss", "sub", "aud", "exp", "nbf", "iat", "jti") will be ignored. Total custom claims size cannot exceed four kilobytes

        - `code_verifier`: A base64url encoded one time secret used to validate that the request starts and ends on the same device.
        """  # noqa

        payload: Dict[str, Any] = {
            "organization_id": organization_id,
            "email_address": email_address,
            "existing_password": existing_password,
            "new_password": new_password,
        }

        if session_token is not None:
            payload["session_token"] = session_token
        if session_jwt is not None:
            payload["session_jwt"] = session_jwt
        if session_duration_minutes is not None:
            payload["session_duration_minutes"] = session_duration_minutes
        if session_custom_claims is not None:
            payload["session_custom_claims"] = session_custom_claims

        url = self.api_base.route_with_sub_url(self.sub_url, "reset")

        res = self.sync_client.post(url, json=payload)
        return ResetResponse.from_json(res.response.status_code, res.json)

    async def reset_async(
        self,
        organization_id: str,
        email_address: str,
        existing_password: str,
        new_password: str,
        session_token: Optional[str] = None,
        session_jwt: Optional[str] = None,
        session_duration_minutes: Optional[int] = None,
        session_custom_claims: Optional[Dict[str, Any]] = None,
    ) -> ResetResponse:
        """Reset the member’s password using their existing password.

        Parameters:

        - `organization_id`: Globally unique UUID that identifies a specific Organization. The organization_id is critical to perform operations on an Organization, so be sure to preserve this value.

        - `email_address`: The email of the Member

        - `existing_password`: The member's current password that they supplied.

        - `new__password`: The member's elected new password.

        - `session_token`: A secret token for a given Stytch Session. Read more about session_token in our Session Management guide.

        - `session_jwt`: The JSON Web Token (JWT) for a given Stytch Session. Read more about session_token in our Session Management guide.

        - `session_duration_minutes`: The Session lifetime of this many minutes from now; minimum of 5 and a maximum of 129600 minutes (90 days). Note that a successful authentication will continue to extend the Session this many minutes.

        - `session_custom_claims`: Add a custom claims map to the Session being authenticated. Claims are only created if a Session is initialized by providing a value in Session duration minutes. Claims will be included on the Session object and in the JWT. To update a key in an existing Session, supply a new value. To delete a key, supply a null value.
          Custom claims made with reserved claims ("iss", "sub", "aud", "exp", "nbf", "iat", "jti") will be ignored. Total custom claims size cannot exceed four kilobytes

        - `code_verifier`: A base64url encoded one time secret used to validate that the request starts and ends on the same device.
        """  # noqa

        payload: Dict[str, Any] = {
            "organization_id": organization_id,
            "email_address": email_address,
            "existing_password": existing_password,
            "new_password": new_password,
        }

        if session_token is not None:
            payload["session_token"] = session_token
        if session_jwt is not None:
            payload["session_jwt"] = session_jwt
        if session_duration_minutes is not None:
            payload["session_duration_minutes"] = session_duration_minutes
        if session_custom_claims is not None:
            payload["session_custom_claims"] = session_custom_claims

        url = self.api_base.route_with_sub_url(self.sub_url, "reset")

        res = await self.async_client.post(url, json=payload)
        return ResetResponse.from_json(res.response.status, res.json)
