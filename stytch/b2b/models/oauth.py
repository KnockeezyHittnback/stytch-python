# !!!
# WARNING: This file is autogenerated
# Only modify code within MANUAL() sections
# or your changes may be overwritten later!
# !!!

from __future__ import annotations

import datetime
import enum
from typing import List, Optional

import pydantic

from stytch.b2b.models.organizations import Member, Organization
from stytch.b2b.models.sessions import MemberSession
from stytch.core.response_base import ResponseBase


class AuthenticateRequestLocale(enum.Enum):
    EN = "en"
    ES = "es"
    PTBR = "pt-br"


class ProviderValues(pydantic.BaseModel):
    """
    Fields:
      - access_token: The `access_token` that you may use to access the User's data in the provider's API.
      - scopes: The OAuth scopes included for a given provider. See each provider's section above to see which scopes are included by default and how to add custom scopes.
      - refresh_token: The `refresh_token` that you may use to refresh a User's session within the provider's API.
      - expires_at: (no documentation yet)
      - id_token: The `id_token` returned by the OAuth provider. ID Tokens are JWTs that contain structured information about a user. The exact content of each ID Token varies from provider to provider. ID Tokens are returned from OAuth providers that conform to the [OpenID Connect](https://openid.net/foundation/) specification, which is based on OAuth.
    """  # noqa

    access_token: str
    scopes: List[str]
    refresh_token: Optional[str] = None
    expires_at: Optional[datetime.datetime] = None
    id_token: Optional[str] = None


class AuthenticateResponse(ResponseBase):
    """Response type for `OAuth.authenticate`.
    Fields:
      - member_id: Globally unique UUID that identifies a specific Member.
      - provider_subject: (no documentation yet)
      - provider_type: (no documentation yet)
      - session_token: A secret token for a given Stytch Session.
      - session_jwt: The JSON Web Token (JWT) for a given Stytch Session.
      - member: The [Member object](https://stytch.com/docs/b2b/api/member-object).
      - organization_id: Globally unique UUID that identifies a specific Organization. The `organization_id` is critical to perform operations on an Organization, so be sure to preserve this value.
      - organization: The [Organization object](https://stytch.com/docs/b2b/api/organization-object).
      - reset_sessions: (no documentation yet)
      - member_session: The [Session object](https://stytch.com/docs/b2b/api/session-object).
      - provider_values: The `provider_values` object lists relevant identifiers, values, and scopes for a given OAuth provider. For example this object will include a provider's `access_token` that you can use to access the provider's API for a given user.

      Note that these values will vary based on the OAuth provider in question, e.g. `id_token` is only returned by Microsoft.
    """  # noqa

    member_id: str
    provider_subject: str
    provider_type: str
    session_token: str
    session_jwt: str
    member: Member
    organization_id: str
    organization: Organization
    reset_sessions: bool
    member_session: Optional[MemberSession] = None
    provider_values: Optional[ProviderValues] = None
