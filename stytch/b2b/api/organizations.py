# !!!
# WARNING: This file is autogenerated
# Only modify code within MANUAL() sections
# or your changes may be overwritten later!
# !!!

from __future__ import annotations

from typing import Any, Dict, List, Optional

from stytch.b2b.api.organizations_members import Members
from stytch.b2b.models.organizations import (
    CreateResponse,
    DeleteResponse,
    GetResponse,
    SearchQuery,
    SearchResponse,
    UpdateResponse,
)
from stytch.core.api_base import ApiBase
from stytch.core.http.client import AsyncClient, SyncClient


class Organizations:
    def __init__(
        self,
        api_base: ApiBase,
        sync_client: SyncClient,
        async_client: AsyncClient,
    ) -> None:
        self.api_base = api_base
        self.sync_client = sync_client
        self.async_client = async_client
        self.members = Members(api_base, sync_client, async_client)

    def create(
        self,
        organization_name: str,
        organization_slug: Optional[str] = None,
        organization_logo_url: Optional[str] = None,
        trusted_metadata: Optional[Dict[str, Any]] = None,
        sso_jit_provisioning: Optional[str] = None,
        email_allowed_domains: Optional[List[str]] = None,
        email_jit_provisioning: Optional[str] = None,
        email_invites: Optional[str] = None,
        auth_methods: Optional[str] = None,
        allowed_auth_methods: Optional[List[str]] = None,
        mfa_policy: Optional[str] = None,
    ) -> CreateResponse:
        """Creates an Organization. An `organization_name` and a unique `organization_slug` are required.

        By default, `email_invites` and `sso_jit_provisioning` will be set to `ALL_ALLOWED`, and `mfa_policy` will be set to `OPTIONAL` if no Organization authentication settings are explicitly defined in the request.

        *See the [Organization authentication settings](https://stytch.com/docs/b2b/api/org-auth-settings) resource to learn more about fields like `email_jit_provisioning`, `email_invites`, `sso_jit_provisioning`, etc., and their behaviors.

        Fields:
          - organization_name: The name of the Organization.
          - organization_slug: The unique URL slug of the Organization. A minimum of two characters is required. The slug only accepts alphanumeric characters and the following reserved characters: `-` `.` `_` `~`.
          - organization_logo_url: The image URL of the Organization logo.
          - trusted_metadata: An arbitrary JSON object for storing application-specific data or identity-provider-specific data.
          - sso_jit_provisioning: The authentication setting that controls the JIT provisioning of Members when authenticating via SSO. The accepted values are:

          `ALL_ALLOWED` – new Members will be automatically provisioned upon successful authentication via any of the Organization's `sso_active_connections`.

          `RESTRICTED` – only new Members with SSO logins that comply with `sso_jit_provisioning_allowed_connections` can be provisioned upon authentication.

          `NOT_ALLOWED` – disable JIT provisioning via SSO.

          - email_allowed_domains: An array of email domains that allow invites or JIT provisioning for new Members. This list is enforced when either `email_invites` or `email_jit_provisioning` is set to `RESTRICTED`.


            Common domains such as `gmail.com` are not allowed. See the [common email domains resource](https://stytch.com/docs/b2b/api/common-email-domains) for the full list.
          - email_jit_provisioning: The authentication setting that controls how a new Member can be provisioned by authenticating via Email Magic Link. The accepted values are:

          `RESTRICTED` – only new Members with verified emails that comply with `email_allowed_domains` can be provisioned upon authentication via Email Magic Link.

          `NOT_ALLOWED` – disable JIT provisioning via Email Magic Link.

          - email_invites: The authentication setting that controls how a new Member can be invited to an organization by email. The accepted values are:

          `ALL_ALLOWED` – any new Member can be invited to join via email.

          `RESTRICTED` – only new Members with verified emails that comply with `email_allowed_domains` can be invited via email.

          `NOT_ALLOWED` – disable email invites.

          - auth_methods: The setting that controls which authentication methods can be used by Members of an Organization. The accepted values are:

          `ALL_ALLOWED` – the default setting which allows all authentication methods to be used.

          `RESTRICTED` – only methods that comply with `allowed_auth_methods` can be used for authentication. This setting does not apply to Members with `is_breakglass` set to `true`.

          - allowed_auth_methods:
          An array of allowed authentication methods. This list is enforced when `auth_methods` is set to `RESTRICTED`.
          The list's accepted values are: `sso`, `magic_link`, `password`, `google_oauth`, and `microsoft_oauth`.

          - mfa_policy: The setting that controls the MFA policy for all Members in the Organization. The accepted values are:

          `REQUIRED_FOR_ALL` – All Members within the Organization will be required to complete MFA every time they wish to log in.

          `OPTIONAL` – The default value. The Organization does not require MFA by default for all Members. Members will be required to complete MFA only if their `mfa_enrolled` status is set to true.

        """  # noqa
        data: Dict[str, Any] = {
            "organization_name": organization_name,
        }
        if organization_slug is not None:
            data["organization_slug"] = organization_slug
        if organization_logo_url is not None:
            data["organization_logo_url"] = organization_logo_url
        if trusted_metadata is not None:
            data["trusted_metadata"] = trusted_metadata
        if sso_jit_provisioning is not None:
            data["sso_jit_provisioning"] = sso_jit_provisioning
        if email_allowed_domains is not None:
            data["email_allowed_domains"] = email_allowed_domains
        if email_jit_provisioning is not None:
            data["email_jit_provisioning"] = email_jit_provisioning
        if email_invites is not None:
            data["email_invites"] = email_invites
        if auth_methods is not None:
            data["auth_methods"] = auth_methods
        if allowed_auth_methods is not None:
            data["allowed_auth_methods"] = allowed_auth_methods
        if mfa_policy is not None:
            data["mfa_policy"] = mfa_policy

        url = self.api_base.url_for("/v1/b2b/organizations", data)
        res = self.sync_client.post(url, data)
        return CreateResponse.from_json(res.response.status_code, res.json)

    async def create_async(
        self,
        organization_name: str,
        organization_slug: Optional[str] = None,
        organization_logo_url: Optional[str] = None,
        trusted_metadata: Optional[Dict[str, Any]] = None,
        sso_jit_provisioning: Optional[str] = None,
        email_allowed_domains: Optional[List[str]] = None,
        email_jit_provisioning: Optional[str] = None,
        email_invites: Optional[str] = None,
        auth_methods: Optional[str] = None,
        allowed_auth_methods: Optional[List[str]] = None,
        mfa_policy: Optional[str] = None,
    ) -> CreateResponse:
        """Creates an Organization. An `organization_name` and a unique `organization_slug` are required.

        By default, `email_invites` and `sso_jit_provisioning` will be set to `ALL_ALLOWED`, and `mfa_policy` will be set to `OPTIONAL` if no Organization authentication settings are explicitly defined in the request.

        *See the [Organization authentication settings](https://stytch.com/docs/b2b/api/org-auth-settings) resource to learn more about fields like `email_jit_provisioning`, `email_invites`, `sso_jit_provisioning`, etc., and their behaviors.

        Fields:
          - organization_name: The name of the Organization.
          - organization_slug: The unique URL slug of the Organization. A minimum of two characters is required. The slug only accepts alphanumeric characters and the following reserved characters: `-` `.` `_` `~`.
          - organization_logo_url: The image URL of the Organization logo.
          - trusted_metadata: An arbitrary JSON object for storing application-specific data or identity-provider-specific data.
          - sso_jit_provisioning: The authentication setting that controls the JIT provisioning of Members when authenticating via SSO. The accepted values are:

          `ALL_ALLOWED` – new Members will be automatically provisioned upon successful authentication via any of the Organization's `sso_active_connections`.

          `RESTRICTED` – only new Members with SSO logins that comply with `sso_jit_provisioning_allowed_connections` can be provisioned upon authentication.

          `NOT_ALLOWED` – disable JIT provisioning via SSO.

          - email_allowed_domains: An array of email domains that allow invites or JIT provisioning for new Members. This list is enforced when either `email_invites` or `email_jit_provisioning` is set to `RESTRICTED`.


            Common domains such as `gmail.com` are not allowed. See the [common email domains resource](https://stytch.com/docs/b2b/api/common-email-domains) for the full list.
          - email_jit_provisioning: The authentication setting that controls how a new Member can be provisioned by authenticating via Email Magic Link. The accepted values are:

          `RESTRICTED` – only new Members with verified emails that comply with `email_allowed_domains` can be provisioned upon authentication via Email Magic Link.

          `NOT_ALLOWED` – disable JIT provisioning via Email Magic Link.

          - email_invites: The authentication setting that controls how a new Member can be invited to an organization by email. The accepted values are:

          `ALL_ALLOWED` – any new Member can be invited to join via email.

          `RESTRICTED` – only new Members with verified emails that comply with `email_allowed_domains` can be invited via email.

          `NOT_ALLOWED` – disable email invites.

          - auth_methods: The setting that controls which authentication methods can be used by Members of an Organization. The accepted values are:

          `ALL_ALLOWED` – the default setting which allows all authentication methods to be used.

          `RESTRICTED` – only methods that comply with `allowed_auth_methods` can be used for authentication. This setting does not apply to Members with `is_breakglass` set to `true`.

          - allowed_auth_methods:
          An array of allowed authentication methods. This list is enforced when `auth_methods` is set to `RESTRICTED`.
          The list's accepted values are: `sso`, `magic_link`, `password`, `google_oauth`, and `microsoft_oauth`.

          - mfa_policy: The setting that controls the MFA policy for all Members in the Organization. The accepted values are:

          `REQUIRED_FOR_ALL` – All Members within the Organization will be required to complete MFA every time they wish to log in.

          `OPTIONAL` – The default value. The Organization does not require MFA by default for all Members. Members will be required to complete MFA only if their `mfa_enrolled` status is set to true.

        """  # noqa
        data: Dict[str, Any] = {
            "organization_name": organization_name,
        }
        if organization_slug is not None:
            data["organization_slug"] = organization_slug
        if organization_logo_url is not None:
            data["organization_logo_url"] = organization_logo_url
        if trusted_metadata is not None:
            data["trusted_metadata"] = trusted_metadata
        if sso_jit_provisioning is not None:
            data["sso_jit_provisioning"] = sso_jit_provisioning
        if email_allowed_domains is not None:
            data["email_allowed_domains"] = email_allowed_domains
        if email_jit_provisioning is not None:
            data["email_jit_provisioning"] = email_jit_provisioning
        if email_invites is not None:
            data["email_invites"] = email_invites
        if auth_methods is not None:
            data["auth_methods"] = auth_methods
        if allowed_auth_methods is not None:
            data["allowed_auth_methods"] = allowed_auth_methods
        if mfa_policy is not None:
            data["mfa_policy"] = mfa_policy

        url = self.api_base.url_for("/v1/b2b/organizations", data)
        res = await self.async_client.post(url, data)
        return CreateResponse.from_json(res.response.status, res.json)

    def get(
        self,
        organization_id: str,
    ) -> GetResponse:
        """Returns an Organization specified by `organization_id`.

        Fields:
          - organization_id: Globally unique UUID that identifies a specific Organization. The `organization_id` is critical to perform operations on an Organization, so be sure to preserve this value.
        """  # noqa
        data: Dict[str, Any] = {
            "organization_id": organization_id,
        }

        url = self.api_base.url_for("/v1/b2b/organizations/{organization_id}", data)
        res = self.sync_client.get(url, data)
        return GetResponse.from_json(res.response.status_code, res.json)

    async def get_async(
        self,
        organization_id: str,
    ) -> GetResponse:
        """Returns an Organization specified by `organization_id`.

        Fields:
          - organization_id: Globally unique UUID that identifies a specific Organization. The `organization_id` is critical to perform operations on an Organization, so be sure to preserve this value.
        """  # noqa
        data: Dict[str, Any] = {
            "organization_id": organization_id,
        }

        url = self.api_base.url_for("/v1/b2b/organizations/{organization_id}", data)
        res = await self.async_client.get(url, data)
        return GetResponse.from_json(res.response.status, res.json)

    def update(
        self,
        organization_id: str,
        organization_name: Optional[str] = None,
        organization_slug: Optional[str] = None,
        organization_logo_url: Optional[str] = None,
        trusted_metadata: Optional[Dict[str, Any]] = None,
        sso_default_connection_id: Optional[str] = None,
        sso_jit_provisioning: Optional[str] = None,
        sso_jit_provisioning_allowed_connections: Optional[List[str]] = None,
        email_allowed_domains: Optional[List[str]] = None,
        email_jit_provisioning: Optional[str] = None,
        email_invites: Optional[str] = None,
        auth_methods: Optional[str] = None,
        allowed_auth_methods: Optional[List[str]] = None,
        mfa_policy: Optional[str] = None,
    ) -> UpdateResponse:
        """Updates an Organization specified by `organization_id`. An Organization must always have at least one auth setting set to either `RESTRICTED` or `ALL_ALLOWED` in order to provision new Members. test

        *See the [Organization authentication settings](https://stytch.com/docs/b2b/api/org-auth-settings) resource to learn more about fields like `email_jit_provisioning`, `email_invites`, `sso_jit_provisioning`, etc., and their behaviors.

        Fields:
          - organization_id: Globally unique UUID that identifies a specific Organization. The `organization_id` is critical to perform operations on an Organization, so be sure to preserve this value.
          - organization_name: The name of the Organization.
          - organization_slug: The unique URL slug of the Organization. A minimum of two characters is required. The slug only accepts alphanumeric characters and the following reserved characters: `-` `.` `_` `~`.
          - organization_logo_url: The image URL of the Organization logo.
          - trusted_metadata: An arbitrary JSON object for storing application-specific data or identity-provider-specific data.
          - sso_default_connection_id: The default connection used for SSO when there are multiple active connections.
          - sso_jit_provisioning: The authentication setting that controls the JIT provisioning of Members when authenticating via SSO. The accepted values are:

          `ALL_ALLOWED` – new Members will be automatically provisioned upon successful authentication via any of the Organization's `sso_active_connections`.

          `RESTRICTED` – only new Members with SSO logins that comply with `sso_jit_provisioning_allowed_connections` can be provisioned upon authentication.

          `NOT_ALLOWED` – disable JIT provisioning via SSO.

          - sso_jit_provisioning_allowed_connections: An array of `connection_id`s that reference [SAML Connection objects](https://stytch.com/docs/b2b/api/saml-connection-object).
          Only these connections will be allowed to JIT provision Members via SSO when `sso_jit_provisioning` is set to `RESTRICTED`.
          - email_allowed_domains: An array of email domains that allow invites or JIT provisioning for new Members. This list is enforced when either `email_invites` or `email_jit_provisioning` is set to `RESTRICTED`.


            Common domains such as `gmail.com` are not allowed. See the [common email domains resource](https://stytch.com/docs/b2b/api/common-email-domains) for the full list.
          - email_jit_provisioning: The authentication setting that controls how a new Member can be provisioned by authenticating via Email Magic Link. The accepted values are:

          `RESTRICTED` – only new Members with verified emails that comply with `email_allowed_domains` can be provisioned upon authentication via Email Magic Link.

          `NOT_ALLOWED` – disable JIT provisioning via Email Magic Link.

          - email_invites: The authentication setting that controls how a new Member can be invited to an organization by email. The accepted values are:

          `ALL_ALLOWED` – any new Member can be invited to join via email.

          `RESTRICTED` – only new Members with verified emails that comply with `email_allowed_domains` can be invited via email.

          `NOT_ALLOWED` – disable email invites.

          - auth_methods: The setting that controls which authentication methods can be used by Members of an Organization. The accepted values are:

          `ALL_ALLOWED` – the default setting which allows all authentication methods to be used.

          `RESTRICTED` – only methods that comply with `allowed_auth_methods` can be used for authentication. This setting does not apply to Members with `is_breakglass` set to `true`.

          - allowed_auth_methods:
          An array of allowed authentication methods. This list is enforced when `auth_methods` is set to `RESTRICTED`.
          The list's accepted values are: `sso`, `magic_link`, `password`, `google_oauth`, and `microsoft_oauth`.

          - mfa_policy: The setting that controls the MFA policy for all Members in the Organization. The accepted values are:

          `REQUIRED_FOR_ALL` – All Members within the Organization will be required to complete MFA every time they wish to log in.

          `OPTIONAL` – The default value. The Organization does not require MFA by default for all Members. Members will be required to complete MFA only if their `mfa_enrolled` status is set to true.

        """  # noqa
        data: Dict[str, Any] = {
            "organization_id": organization_id,
        }
        if organization_name is not None:
            data["organization_name"] = organization_name
        if organization_slug is not None:
            data["organization_slug"] = organization_slug
        if organization_logo_url is not None:
            data["organization_logo_url"] = organization_logo_url
        if trusted_metadata is not None:
            data["trusted_metadata"] = trusted_metadata
        if sso_default_connection_id is not None:
            data["sso_default_connection_id"] = sso_default_connection_id
        if sso_jit_provisioning is not None:
            data["sso_jit_provisioning"] = sso_jit_provisioning
        if sso_jit_provisioning_allowed_connections is not None:
            data[
                "sso_jit_provisioning_allowed_connections"
            ] = sso_jit_provisioning_allowed_connections
        if email_allowed_domains is not None:
            data["email_allowed_domains"] = email_allowed_domains
        if email_jit_provisioning is not None:
            data["email_jit_provisioning"] = email_jit_provisioning
        if email_invites is not None:
            data["email_invites"] = email_invites
        if auth_methods is not None:
            data["auth_methods"] = auth_methods
        if allowed_auth_methods is not None:
            data["allowed_auth_methods"] = allowed_auth_methods
        if mfa_policy is not None:
            data["mfa_policy"] = mfa_policy

        url = self.api_base.url_for("/v1/b2b/organizations/{organization_id}", data)
        res = self.sync_client.put(url, data)
        return UpdateResponse.from_json(res.response.status_code, res.json)

    async def update_async(
        self,
        organization_id: str,
        organization_name: Optional[str] = None,
        organization_slug: Optional[str] = None,
        organization_logo_url: Optional[str] = None,
        trusted_metadata: Optional[Dict[str, Any]] = None,
        sso_default_connection_id: Optional[str] = None,
        sso_jit_provisioning: Optional[str] = None,
        sso_jit_provisioning_allowed_connections: Optional[List[str]] = None,
        email_allowed_domains: Optional[List[str]] = None,
        email_jit_provisioning: Optional[str] = None,
        email_invites: Optional[str] = None,
        auth_methods: Optional[str] = None,
        allowed_auth_methods: Optional[List[str]] = None,
        mfa_policy: Optional[str] = None,
    ) -> UpdateResponse:
        """Updates an Organization specified by `organization_id`. An Organization must always have at least one auth setting set to either `RESTRICTED` or `ALL_ALLOWED` in order to provision new Members. test

        *See the [Organization authentication settings](https://stytch.com/docs/b2b/api/org-auth-settings) resource to learn more about fields like `email_jit_provisioning`, `email_invites`, `sso_jit_provisioning`, etc., and their behaviors.

        Fields:
          - organization_id: Globally unique UUID that identifies a specific Organization. The `organization_id` is critical to perform operations on an Organization, so be sure to preserve this value.
          - organization_name: The name of the Organization.
          - organization_slug: The unique URL slug of the Organization. A minimum of two characters is required. The slug only accepts alphanumeric characters and the following reserved characters: `-` `.` `_` `~`.
          - organization_logo_url: The image URL of the Organization logo.
          - trusted_metadata: An arbitrary JSON object for storing application-specific data or identity-provider-specific data.
          - sso_default_connection_id: The default connection used for SSO when there are multiple active connections.
          - sso_jit_provisioning: The authentication setting that controls the JIT provisioning of Members when authenticating via SSO. The accepted values are:

          `ALL_ALLOWED` – new Members will be automatically provisioned upon successful authentication via any of the Organization's `sso_active_connections`.

          `RESTRICTED` – only new Members with SSO logins that comply with `sso_jit_provisioning_allowed_connections` can be provisioned upon authentication.

          `NOT_ALLOWED` – disable JIT provisioning via SSO.

          - sso_jit_provisioning_allowed_connections: An array of `connection_id`s that reference [SAML Connection objects](https://stytch.com/docs/b2b/api/saml-connection-object).
          Only these connections will be allowed to JIT provision Members via SSO when `sso_jit_provisioning` is set to `RESTRICTED`.
          - email_allowed_domains: An array of email domains that allow invites or JIT provisioning for new Members. This list is enforced when either `email_invites` or `email_jit_provisioning` is set to `RESTRICTED`.


            Common domains such as `gmail.com` are not allowed. See the [common email domains resource](https://stytch.com/docs/b2b/api/common-email-domains) for the full list.
          - email_jit_provisioning: The authentication setting that controls how a new Member can be provisioned by authenticating via Email Magic Link. The accepted values are:

          `RESTRICTED` – only new Members with verified emails that comply with `email_allowed_domains` can be provisioned upon authentication via Email Magic Link.

          `NOT_ALLOWED` – disable JIT provisioning via Email Magic Link.

          - email_invites: The authentication setting that controls how a new Member can be invited to an organization by email. The accepted values are:

          `ALL_ALLOWED` – any new Member can be invited to join via email.

          `RESTRICTED` – only new Members with verified emails that comply with `email_allowed_domains` can be invited via email.

          `NOT_ALLOWED` – disable email invites.

          - auth_methods: The setting that controls which authentication methods can be used by Members of an Organization. The accepted values are:

          `ALL_ALLOWED` – the default setting which allows all authentication methods to be used.

          `RESTRICTED` – only methods that comply with `allowed_auth_methods` can be used for authentication. This setting does not apply to Members with `is_breakglass` set to `true`.

          - allowed_auth_methods:
          An array of allowed authentication methods. This list is enforced when `auth_methods` is set to `RESTRICTED`.
          The list's accepted values are: `sso`, `magic_link`, `password`, `google_oauth`, and `microsoft_oauth`.

          - mfa_policy: The setting that controls the MFA policy for all Members in the Organization. The accepted values are:

          `REQUIRED_FOR_ALL` – All Members within the Organization will be required to complete MFA every time they wish to log in.

          `OPTIONAL` – The default value. The Organization does not require MFA by default for all Members. Members will be required to complete MFA only if their `mfa_enrolled` status is set to true.

        """  # noqa
        data: Dict[str, Any] = {
            "organization_id": organization_id,
        }
        if organization_name is not None:
            data["organization_name"] = organization_name
        if organization_slug is not None:
            data["organization_slug"] = organization_slug
        if organization_logo_url is not None:
            data["organization_logo_url"] = organization_logo_url
        if trusted_metadata is not None:
            data["trusted_metadata"] = trusted_metadata
        if sso_default_connection_id is not None:
            data["sso_default_connection_id"] = sso_default_connection_id
        if sso_jit_provisioning is not None:
            data["sso_jit_provisioning"] = sso_jit_provisioning
        if sso_jit_provisioning_allowed_connections is not None:
            data[
                "sso_jit_provisioning_allowed_connections"
            ] = sso_jit_provisioning_allowed_connections
        if email_allowed_domains is not None:
            data["email_allowed_domains"] = email_allowed_domains
        if email_jit_provisioning is not None:
            data["email_jit_provisioning"] = email_jit_provisioning
        if email_invites is not None:
            data["email_invites"] = email_invites
        if auth_methods is not None:
            data["auth_methods"] = auth_methods
        if allowed_auth_methods is not None:
            data["allowed_auth_methods"] = allowed_auth_methods
        if mfa_policy is not None:
            data["mfa_policy"] = mfa_policy

        url = self.api_base.url_for("/v1/b2b/organizations/{organization_id}", data)
        res = await self.async_client.put(url, data)
        return UpdateResponse.from_json(res.response.status, res.json)

    def delete(
        self,
        organization_id: str,
    ) -> DeleteResponse:
        """Deletes an Organization specified by `organization_id`. All Members of the Organization will also be deleted.

        Fields:
          - organization_id: Globally unique UUID that identifies a specific Organization. The `organization_id` is critical to perform operations on an Organization, so be sure to preserve this value.
        """  # noqa
        data: Dict[str, Any] = {
            "organization_id": organization_id,
        }

        url = self.api_base.url_for("/v1/b2b/organizations/{organization_id}", data)
        res = self.sync_client.delete(url)
        return DeleteResponse.from_json(res.response.status_code, res.json)

    async def delete_async(
        self,
        organization_id: str,
    ) -> DeleteResponse:
        """Deletes an Organization specified by `organization_id`. All Members of the Organization will also be deleted.

        Fields:
          - organization_id: Globally unique UUID that identifies a specific Organization. The `organization_id` is critical to perform operations on an Organization, so be sure to preserve this value.
        """  # noqa
        data: Dict[str, Any] = {
            "organization_id": organization_id,
        }

        url = self.api_base.url_for("/v1/b2b/organizations/{organization_id}", data)
        res = await self.async_client.delete(url)
        return DeleteResponse.from_json(res.response.status, res.json)

    def search(
        self,
        cursor: Optional[str] = None,
        limit: Optional[int] = None,
        query: Optional[SearchQuery] = None,
    ) -> SearchResponse:
        """Search for Organizations. If you send a request with no body params, no filtering will be applied and the endpoint will return all Organizations. All fuzzy search filters require a minimum of three characters.

        Fields:
          - cursor: The `cursor` field allows you to paginate through your results. Each result array is limited to 1000 results. If your query returns more than 1000 results, you will need to paginate the responses using the `cursor`. If you receive a response that includes a non-null `next_cursor` in the `results_metadata` object, repeat the search call with the `next_cursor` value set to the `cursor` field to retrieve the next page of results. Continue to make search calls until the `next_cursor` in the response is null.
          - limit: The number of search results to return per page. The default limit is 100. A maximum of 1000 results can be returned by a single search request. If the total size of your result set is greater than one page size, you must paginate the response. See the `cursor` field.
          - query: The optional query object contains the operator, i.e. `AND` or `OR`, and the operands that will filter your results. Only an operator is required. If you include no operands, no filtering will be applied. If you include no query object, it will return all Organizations with no filtering applied.
        """  # noqa
        data: Dict[str, Any] = {}
        if cursor is not None:
            data["cursor"] = cursor
        if limit is not None:
            data["limit"] = limit
        if query is not None:
            data["query"] = query.dict()

        url = self.api_base.url_for("/v1/b2b/organizations/search", data)
        res = self.sync_client.post(url, data)
        return SearchResponse.from_json(res.response.status_code, res.json)

    async def search_async(
        self,
        cursor: Optional[str] = None,
        limit: Optional[int] = None,
        query: Optional[SearchQuery] = None,
    ) -> SearchResponse:
        """Search for Organizations. If you send a request with no body params, no filtering will be applied and the endpoint will return all Organizations. All fuzzy search filters require a minimum of three characters.

        Fields:
          - cursor: The `cursor` field allows you to paginate through your results. Each result array is limited to 1000 results. If your query returns more than 1000 results, you will need to paginate the responses using the `cursor`. If you receive a response that includes a non-null `next_cursor` in the `results_metadata` object, repeat the search call with the `next_cursor` value set to the `cursor` field to retrieve the next page of results. Continue to make search calls until the `next_cursor` in the response is null.
          - limit: The number of search results to return per page. The default limit is 100. A maximum of 1000 results can be returned by a single search request. If the total size of your result set is greater than one page size, you must paginate the response. See the `cursor` field.
          - query: The optional query object contains the operator, i.e. `AND` or `OR`, and the operands that will filter your results. Only an operator is required. If you include no operands, no filtering will be applied. If you include no query object, it will return all Organizations with no filtering applied.
        """  # noqa
        data: Dict[str, Any] = {}
        if cursor is not None:
            data["cursor"] = cursor
        if limit is not None:
            data["limit"] = limit
        if query is not None:
            data["query"] = query.dict()

        url = self.api_base.url_for("/v1/b2b/organizations/search", data)
        res = await self.async_client.post(url, data)
        return SearchResponse.from_json(res.response.status, res.json)
