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

from stytch.core.response_base import ResponseBase
from stytch.shared.method_options import Authorization


class SearchQueryOperator(str, enum.Enum):
    OR = "OR"
    AND = "AND"


class ActiveSCIMConnection(pydantic.BaseModel):
    connection_id: str
    display_name: str
    bearer_token_last_four: str
    bearer_token_expires_at: Optional[datetime.datetime] = None


class ActiveSSOConnection(pydantic.BaseModel):
    """
    Fields:
      - connection_id: Globally unique UUID that identifies a specific SSO `connection_id` for a Member.
      - display_name: A human-readable display name for the connection.
    """  # noqa

    connection_id: str
    display_name: str


class DeleteRequestOptions(pydantic.BaseModel):
    """
    Fields:
      - authorization: Optional authorization object.
    Pass in an active Stytch Member session token or session JWT and the request
    will be run using that member's permissions.
    """  # noqa

    authorization: Optional[Authorization] = None

    def add_headers(self, headers: Dict[str, str]) -> Dict[str, str]:
        if self.authorization is not None:
            headers = self.authorization.add_headers(headers)
        return headers


class EmailImplicitRoleAssignment(pydantic.BaseModel):
    """
    Fields:
      - domain: Email domain that grants the specified Role.
      - role_id: The unique identifier of the RBAC Role, provided by the developer and intended to be human-readable.

      Reserved `role_id`s that are predefined by Stytch include:

      * `stytch_member`
      * `stytch_admin`

      Check out the [guide on Stytch default Roles](https://stytch.com/docs/b2b/guides/rbac/stytch-defaults) for a more detailed explanation.


    """  # noqa

    domain: str
    role_id: str


class MemberRoleSource(pydantic.BaseModel):
    """
    Fields:
      - type: The type of role assignment. The possible values are:

      `direct_assignment` – an explicitly assigned Role.

      Directly assigned roles can be updated by passing in the `roles` argument to the
      [Update Member](https://stytch.com/docs/b2b/api/update-member) endpoint.

      `email_assignment` – an implicit Role granted by the Member's email domain, regardless of their login method.

      Email implicit role assignments can be updated by passing in the `rbac_email_implicit_role_assignments` argument to
      the [Update Organization](https://stytch.com/docs/b2b/api/update-organization) endpoint.

      `sso_connection` – an implicit Role granted by the Member's SSO connection. This is currently only available
      for SAML connections and not for OIDC. If the Member has a SAML Member registration with the given connection, this
      role assignment will appear in the list. However, for authorization check purposes (in
      [sessions authenticate](https://stytch.com/docs/b2b/api/authenticate-session) or in any endpoint that enforces RBAC with session
      headers), the Member will only be granted the Role if their session contains an authentication factor with the
      specified SAML connection.

      SAML connection implicit role assignments can be updated by passing in the
      `saml_connection_implicit_role_assignments` argument to the
      [Update SAML connection](https://stytch.com/docs/b2b/api/update-saml-connection) endpoint.

      `sso_connection_group` – an implicit Role granted by the Member's SSO connection and group. This is currently only
      available for SAML connections and not for OIDC. If the Member has a SAML Member registration with the given
      connection, and belongs to a specific group within the IdP, this role assignment will appear in the list. However,
      for authorization check purposes (in [sessions authenticate](https://stytch.com/docs/b2b/api/authenticate-session) or in any endpoint
      that enforces RBAC with session headers), the Member will only be granted the role if their session contains an
      authentication factor with the specified SAML connection.

      SAML group implicit role assignments can be updated by passing in the `saml_group_implicit_role_assignments`
      argument to the [Update SAML connection](https://stytch.com/docs/b2b/api/update-saml-connection) endpoint.

      - details: An object containing additional metadata about the source assignment. The fields will vary depending
      on the role assignment type as follows:

      `direct_assignment` – no additional details.

      `email_assignment` – will contain the email domain that granted the assignment.

      `sso_connection` – will contain the `connection_id` of the SAML connection that granted the assignment.

      `sso_connection_group` – will contain the `connection_id` of the SAML connection and the name of the `group`
      that granted the assignment.

    """  # noqa

    type: str
    details: Optional[Dict[str, Any]] = None


class MemberRole(pydantic.BaseModel):
    """
    Fields:
      - role_id: The unique identifier of the RBAC Role, provided by the developer and intended to be human-readable.

      Reserved `role_id`s that are predefined by Stytch include:

      * `stytch_member`
      * `stytch_admin`

      Check out the [guide on Stytch default Roles](https://stytch.com/docs/b2b/guides/rbac/stytch-defaults) for a more detailed explanation.


      - sources: A list of sources for this role assignment. A role assignment can come from multiple sources - for example, the Role could be both explicitly assigned and implicitly granted from the Member's email domain.
    """  # noqa

    role_id: str
    sources: List[MemberRoleSource]


class OAuthRegistration(pydantic.BaseModel):
    """
    Fields:
      - provider_type: Denotes the OAuth identity provider that the user has authenticated with, e.g. Google, Microsoft, GitHub etc.
      - provider_subject: The unique identifier for the User within a given OAuth provider. Also commonly called the `sub` or "Subject field" in OAuth protocols.
      - member_oauth_registration_id: The unique ID of an OAuth registration.
      - profile_picture_url: If available, the `profile_picture_url` is a URL of the User's profile picture set in OAuth identity the provider that the User has authenticated with, e.g. Google profile picture.
      - locale: If available, the `locale` is the Member's locale set in the OAuth identity provider that the user has authenticated with.
    """  # noqa

    provider_type: str
    provider_subject: str
    member_oauth_registration_id: str
    profile_picture_url: Optional[str] = None
    locale: Optional[str] = None


class Organization(pydantic.BaseModel):
    """
    Fields:
      - organization_id: Globally unique UUID that identifies a specific Organization. The `organization_id` is critical to perform operations on an Organization, so be sure to preserve this value.
      - organization_name: The name of the Organization. Must be between 1 and 128 characters in length.
      - organization_logo_url: The image URL of the Organization logo.
      - organization_slug: The unique URL slug of the Organization. The slug only accepts alphanumeric characters and the following reserved characters: `-` `.` `_` `~`. Must be between 2 and 128 characters in length.
      - sso_jit_provisioning: The authentication setting that controls the JIT provisioning of Members when authenticating via SSO. The accepted values are:

      `ALL_ALLOWED` – new Members will be automatically provisioned upon successful authentication via any of the Organization's `sso_active_connections`.

      `RESTRICTED` – only new Members with SSO logins that comply with `sso_jit_provisioning_allowed_connections` can be provisioned upon authentication.

      `NOT_ALLOWED` – disable JIT provisioning via SSO.

      - sso_jit_provisioning_allowed_connections: An array of `connection_id`s that reference [SAML Connection objects](https://stytch.com/docs/b2b/api/saml-connection-object).
      Only these connections will be allowed to JIT provision Members via SSO when `sso_jit_provisioning` is set to `RESTRICTED`.
      - sso_active_connections: An array of active [SAML Connection references](https://stytch.com/docs/b2b/api/saml-connection-object).
      - email_allowed_domains: An array of email domains that allow invites or JIT provisioning for new Members. This list is enforced when either `email_invites` or `email_jit_provisioning` is set to `RESTRICTED`.


        Common domains such as `gmail.com` are not allowed. See the [common email domains resource](https://stytch.com/docs/b2b/api/common-email-domains) for the full list.
      - email_jit_provisioning: The authentication setting that controls how a new Member can be provisioned by authenticating via Email Magic Link or OAuth. The accepted values are:

      `RESTRICTED` – only new Members with verified emails that comply with `email_allowed_domains` can be provisioned upon authentication via Email Magic Link or OAuth.

      `NOT_ALLOWED` – disable JIT provisioning via Email Magic Link and OAuth.

      - email_invites: The authentication setting that controls how a new Member can be invited to an organization by email. The accepted values are:

      `ALL_ALLOWED` – any new Member can be invited to join via email.

      `RESTRICTED` – only new Members with verified emails that comply with `email_allowed_domains` can be invited via email.

      `NOT_ALLOWED` – disable email invites.

      - auth_methods: The setting that controls which authentication methods can be used by Members of an Organization. The accepted values are:

      `ALL_ALLOWED` – the default setting which allows all authentication methods to be used.

      `RESTRICTED` – only methods that comply with `allowed_auth_methods` can be used for authentication. This setting does not apply to Members with `is_breakglass` set to `true`.

      - allowed_auth_methods: An array of allowed authentication methods. This list is enforced when `auth_methods` is set to `RESTRICTED`.
      The list's accepted values are: `sso`, `magic_link`, `password`, `google_oauth`, and `microsoft_oauth`.

      - mfa_policy: (no documentation yet)
      - rbac_email_implicit_role_assignments: Implicit role assignments based off of email domains.
      For each domain-Role pair, all Members whose email addresses have the specified email domain will be granted the
      associated Role, regardless of their login method. See the [RBAC guide](https://stytch.com/docs/b2b/guides/rbac/role-assignment)
      for more information about role assignment.
      - mfa_methods: The setting that controls which MFA methods can be used by Members of an Organization. The accepted values are:

      `ALL_ALLOWED` – the default setting which allows all authentication methods to be used.

      `RESTRICTED` – only methods that comply with `allowed_mfa_methods` can be used for authentication. This setting does not apply to Members with `is_breakglass` set to `true`.

      - allowed_mfa_methods: An array of allowed MFA authentication methods. This list is enforced when `mfa_methods` is set to `RESTRICTED`.
      The list's accepted values are: `sms_otp` and `totp`.

      - scim_active_connections: (no documentation yet)
      - trusted_metadata: An arbitrary JSON object for storing application-specific data or identity-provider-specific data.
      - sso_default_connection_id: The default connection used for SSO when there are multiple active connections.
    """  # noqa

    organization_id: str
    organization_name: str
    organization_logo_url: str
    organization_slug: str
    sso_jit_provisioning: str
    sso_jit_provisioning_allowed_connections: List[str]
    sso_active_connections: List[ActiveSSOConnection]
    email_allowed_domains: List[str]
    email_jit_provisioning: str
    email_invites: str
    auth_methods: str
    allowed_auth_methods: List[str]
    mfa_policy: str
    rbac_email_implicit_role_assignments: List[EmailImplicitRoleAssignment]
    mfa_methods: str
    allowed_mfa_methods: List[str]
    scim_active_connections: List[ActiveSCIMConnection]
    trusted_metadata: Optional[Dict[str, Any]] = None
    sso_default_connection_id: Optional[str] = None


class ResultsMetadata(pydantic.BaseModel):
    """
    Fields:
      - total: The total number of results returned by your search query.
      - next_cursor: The `next_cursor` string is returned when your search result contains more than one page of results. This value is passed into your next search call in the `cursor` field.
    """  # noqa

    total: int
    next_cursor: Optional[str] = None


class SSORegistration(pydantic.BaseModel):
    """
    Fields:
      - connection_id: Globally unique UUID that identifies a specific SSO `connection_id` for a Member.
      - external_id: The ID of the member given by the identity provider.
      - registration_id: The unique ID of an SSO Registration.
      - sso_attributes: An object for storing SSO attributes brought over from the identity provider.
    """  # noqa

    connection_id: str
    external_id: str
    registration_id: str
    sso_attributes: Optional[Dict[str, Any]] = None


class Member(pydantic.BaseModel):
    """
    Fields:
      - organization_id: Globally unique UUID that identifies a specific Organization. The `organization_id` is critical to perform operations on an Organization, so be sure to preserve this value.
      - member_id: Globally unique UUID that identifies a specific Member. The `member_id` is critical to perform operations on a Member, so be sure to preserve this value.
      - email_address: The email address of the Member.
      - status: The status of the Member. The possible values are: `pending`, `invited`, `active`, or `deleted`.
      - name: The name of the Member.
      - sso_registrations: An array of registered [SAML Connection](saml-connection-object) objects the Member has authenticated with.
      - is_breakglass: Identifies the Member as a break glass user - someone who has permissions to authenticate into an Organization by bypassing the Organization's settings. A break glass account is typically used for emergency purposes to gain access outside of normal authentication procedures. Refer to the [Organization object](organization-object) and its `auth_methods` and `allowed_auth_methods` fields for more details.
      - member_password_id: Globally unique UUID that identifies a Member's password.
      - oauth_registrations: A list of OAuth registrations for this member.
      - email_address_verified: Whether or not the Member's email address is verified.
      - mfa_phone_number_verified: Whether or not the Member's phone number is verified.
      - is_admin: Whether or not the Member has the `stytch_admin` Role. This Role is automatically granted to Members
      who create an Organization through the [discovery flow](https://stytch.com/docs/b2b/api/create-organization-via-discovery). See the
      [RBAC guide](https://stytch.com/docs/b2b/guides/rbac/stytch-defaults) for more details on this Role.
      - totp_registration_id: (no documentation yet)
      - mfa_enrolled: Sets whether the Member is enrolled in MFA. If true, the Member must complete an MFA step whenever they wish to log in to their Organization. If false, the Member only needs to complete an MFA step if the Organization's MFA policy is set to `REQUIRED_FOR_ALL`.
      - mfa_phone_number: The Member's phone number. A Member may only have one phone number.
      - default_mfa_method: (no documentation yet)
      - roles: Explicit or implicit Roles assigned to this Member, along with details about the role assignment source.
       See the [RBAC guide](https://stytch.com/docs/b2b/guides/rbac/role-assignment) for more information about role assignment.
      - trusted_metadata: An arbitrary JSON object for storing application-specific data or identity-provider-specific data.
      - untrusted_metadata: An arbitrary JSON object of application-specific data. These fields can be edited directly by the
      frontend SDK, and should not be used to store critical information. See the [Metadata resource](https://stytch.com/docs/b2b/api/metadata)
      for complete field behavior details.
    """  # noqa

    organization_id: str
    member_id: str
    email_address: str
    status: str
    name: str
    sso_registrations: List[SSORegistration]
    is_breakglass: bool
    member_password_id: str
    oauth_registrations: List[OAuthRegistration]
    email_address_verified: bool
    mfa_phone_number_verified: bool
    is_admin: bool
    totp_registration_id: str
    mfa_enrolled: bool
    mfa_phone_number: str
    default_mfa_method: str
    roles: List[MemberRole]
    trusted_metadata: Optional[Dict[str, Any]] = None
    untrusted_metadata: Optional[Dict[str, Any]] = None


class SearchQuery(pydantic.BaseModel):
    """
    Fields:
      - operator: The action to perform on the operands. The accepted value are:

      `AND` – all the operand values provided must match.

      `OR` – the operator will return any matches to at least one of the operand values you supply.
      - operands: An array of operand objects that contains all of the filters and values to apply to your search query.
    """  # noqa

    operator: SearchQueryOperator
    operands: List[Dict[str, Any]]


class UpdateRequestOptions(pydantic.BaseModel):
    """
    Fields:
      - authorization: Optional authorization object.
    Pass in an active Stytch Member session token or session JWT and the request
    will be run using that member's permissions.
    """  # noqa

    authorization: Optional[Authorization] = None

    def add_headers(self, headers: Dict[str, str]) -> Dict[str, str]:
        if self.authorization is not None:
            headers = self.authorization.add_headers(headers)
        return headers


class CreateResponse(ResponseBase):
    """Response type for `Organizations.create`.
    Fields:
      - organization: The [Organization object](https://stytch.com/docs/b2b/api/organization-object).
    """  # noqa

    organization: Organization


class DeleteResponse(ResponseBase):
    """Response type for `Organizations.delete`.
    Fields:
      - organization_id: Globally unique UUID that identifies a specific Organization. The `organization_id` is critical to perform operations on an Organization, so be sure to preserve this value.
    """  # noqa

    organization_id: str


class GetResponse(ResponseBase):
    """Response type for `Organizations.get`.
    Fields:
      - organization: The [Organization object](https://stytch.com/docs/b2b/api/organization-object).
    """  # noqa

    organization: Organization


class MetricsResponse(ResponseBase):
    member_count: int


class SearchResponse(ResponseBase):
    """Response type for `Organizations.search`.
    Fields:
      - organizations: An array of [Organization objects](https://stytch.com/docs/b2b/api/organization-object).
      - results_metadata: The search `results_metadata` object contains metadata relevant to your specific query like `total` and `next_cursor`.
    """  # noqa

    organizations: List[Organization]
    results_metadata: ResultsMetadata


class UpdateResponse(ResponseBase):
    """Response type for `Organizations.update`.
    Fields:
      - organization: The [Organization object](https://stytch.com/docs/b2b/api/organization-object).
    """  # noqa

    organization: Organization
