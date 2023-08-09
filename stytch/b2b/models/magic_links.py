# !!!
# WARNING: This file is autogenerated
# Only modify code within MANUAL() sections
# or your changes may be overwritten later!
# !!!

from __future__ import annotations

import enum
from typing import Optional

from stytch.b2b.models.mfa import MfaRequired
from stytch.b2b.models.organizations import Member, Organization
from stytch.b2b.models.sessions import MemberSession
from stytch.core.response_base import ResponseBase


class AuthenticateRequestLocale(enum.Enum):
    EN = "en"
    ES = "es"
    PTBR = "pt-br"


class AuthenticateResponse(ResponseBase):
    """Response type for `MagicLinks.authenticate`.
    Fields:
      - member_id: Globally unique UUID that identifies a specific Member.
      - method_id: The email or device involved in the authentication.
      - reset_sessions: Indicates if all Sessions linked to the Member need to be reset. You should check this field if you aren't using
        Stytch's Session product. If you are using Stytch's Session product, we revoke the Member’s other Sessions for you.
      - organization_id: Globally unique UUID that identifies a specific Organization. The `organization_id` is critical to perform operations on an Organization, so be sure to preserve this value.
      - member: The [Member object](https://stytch.com/docs/b2b/api/member-object) if one already exists, or null if one does not.
      - session_token: A secret token for a given Stytch Session.
      - session_jwt: The JSON Web Token (JWT) for a given Stytch Session.
      - member_session: The [Session object](https://stytch.com/docs/b2b/api/session-object).
      - organization: The [Organization object](https://stytch.com/docs/b2b/api/organization-object).
      - intermediate_session_token: The returned Intermediate Session Token contains an Email Magic Link factor associated with the Member's email address.
          The token can be used with the [OTP SMS Authenticate endpoint](https://stytch.com/docs/b2b/api/authenticate-otp-sms) to complete the MFA flow and log in to the Organization.
          It can also be used with the [Exchange Intermediate Session endpoint](https://stytch.com/docs/b2b/api/exchange-intermediate-session) to join a different existing Organization that allows login with Email Magic Links,
          or the [Create Organization via Discovery endpoint](https://stytch.com/docs/b2b/api/create-organization-via-discovery) to create a new Organization.
      - member_authenticated: Indicates whether the Member is fully authenticated. If false, the Member needs to complete an MFA step to log in to the Organization.
      - mfa_required: Information about the MFA requirements of the Organization and the Member's options for fulfilling MFA.
    """  # noqa

    member_id: str
    method_id: str
    reset_sessions: bool
    organization_id: str
    member: Member
    session_token: str
    session_jwt: str
    member_session: MemberSession
    organization: Organization
    intermediate_session_token: str
    member_authenticated: bool
    mfa_required: Optional[MfaRequired] = None
