# !!!
# WARNING: This file is autogenerated
# Only modify code within MANUAL() sections
# or your changes may be overwritten later!
# !!!

from __future__ import annotations

import datetime
import enum
from typing import Any, Dict, List, Optional

import pydantic

from stytch.b2b.models.organizations import Member, Organization
from stytch.b2b.models.sessions import MemberSession
from stytch.core.response_base import ResponseBase


class AuthenticateRequestLocale(enum.Enum):
    EN = "en"
    ES = "es"
    PTBR = "pt-br"


class OIDCConnection(pydantic.BaseModel):
    organization_id: str
    connection_id: str
    status: str
    display_name: str
    redirect_url: str
    client_id: str
    client_secret: str
    issuer: str
    authorization_url: str
    token_url: str
    userinfo_url: str
    jwks_url: str


class X509Certificate(pydantic.BaseModel):
    certificate_id: str
    certificate: str
    issuer: str
    created_at: Optional[datetime.datetime] = None
    expires_at: Optional[datetime.datetime] = None


class SAMLConnection(pydantic.BaseModel):
    organization_id: str
    connection_id: str
    status: str
    idp_entity_id: str
    display_name: str
    idp_sso_url: str
    acs_url: str
    audience_uri: str
    signing_certificates: List[X509Certificate]
    verification_certificates: List[X509Certificate]
    attribute_mapping: Optional[Dict[str, Any]] = None


class AuthenticateResponse(ResponseBase):
    """Response type for `SSO.authenticate`.
    Fields:
      - member_id: Globally unique UUID that identifies a specific Member.
      - organization_id: Globally unique UUID that identifies a specific Organization. The `organization_id` is critical to perform operations on an Organization, so be sure to preserve this value.
      - member: The [Member object](https://stytch.com/docs/b2b/api/member-object).
      - session_token: A secret token for a given Stytch Session.
      - session_jwt: The JSON Web Token (JWT) for a given Stytch Session.
      - reset_session: Indicates if all Sessions linked to the Member need to be reset. You should check this field if you aren't using
        Stytch's Session product. If you are using Stytch's Session product, we revoke the Member’s other Sessions for you.
      - organization: The [Organization object](https://stytch.com/docs/b2b/api/organization-object).
      - member_session: The [Session object](https://stytch.com/docs/b2b/api/session-object).
    """  # noqa

    member_id: str
    organization_id: str
    member: Member
    session_token: str
    session_jwt: str
    reset_session: bool
    organization: Organization
    member_session: Optional[MemberSession] = None


class DeleteConnectionResponse(ResponseBase):
    """Response type for `SSO.delete_connection`.
    Fields:
      - connection_id: The `connection_id` that was deleted as part of the delete request.
    """  # noqa

    connection_id: str


class GetConnectionsResponse(ResponseBase):
    """Response type for `SSO.get_connections`.
    Fields:
      - saml_connections: The list of [SAML Connections](https://stytch.com/docs/b2b/api/saml-connection-object) owned by this organization.
      - oidc_connections: The list of [OIDC Connections](https://stytch.com/docs/b2b/api/oidc-connection-object) owned by this organization.
    """  # noqa

    saml_connections: List[SAMLConnection]
    oidc_connections: List[OIDCConnection]
