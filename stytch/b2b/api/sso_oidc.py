# !!!
# WARNING: This file is autogenerated
# Only modify code within MANUAL() sections
# or your changes may be overwritten later!
# !!!

from __future__ import annotations

from typing import Any, Dict, Optional

from stytch.b2b.models.sso_oidc import (
    CreateConnectionResponse,
    UpdateConnectionResponse,
)
from stytch.core.api_base import ApiBase
from stytch.core.http.client import AsyncClient, SyncClient


class OIDC:
    def __init__(
        self,
        api_base: ApiBase,
        sync_client: SyncClient,
        async_client: AsyncClient,
    ) -> None:
        self.api_base = api_base
        self.sync_client = sync_client
        self.async_client = async_client

    def create_connection(
        self,
        organization_id: str,
        display_name: Optional[str] = None,
    ) -> CreateConnectionResponse:
        """Create a new OIDC Connection.

        Fields:
          - organization_id: Globally unique UUID that identifies a specific Organization. The `organization_id` is critical to perform operations on an Organization, so be sure to preserve this value.
          - display_name: A human-readable display name for the connection.
        """  # noqa
        data: Dict[str, Any] = {
            "organization_id": organization_id,
        }
        if display_name is not None:
            data["display_name"] = display_name

        url = self.api_base.url_for("/v1/b2b/sso/oidc/{organization_id}", data)
        res = self.sync_client.post(url, data)
        return CreateConnectionResponse.from_json(res.response.status_code, res.json)

    async def create_connection_async(
        self,
        organization_id: str,
        display_name: Optional[str] = None,
    ) -> CreateConnectionResponse:
        """Create a new OIDC Connection.

        Fields:
          - organization_id: Globally unique UUID that identifies a specific Organization. The `organization_id` is critical to perform operations on an Organization, so be sure to preserve this value.
          - display_name: A human-readable display name for the connection.
        """  # noqa
        data: Dict[str, Any] = {
            "organization_id": organization_id,
        }
        if display_name is not None:
            data["display_name"] = display_name

        url = self.api_base.url_for("/v1/b2b/sso/oidc/{organization_id}", data)
        res = await self.async_client.post(url, data)
        return CreateConnectionResponse.from_json(res.response.status, res.json)

    def update_connection(
        self,
        organization_id: str,
        connection_id: str,
        display_name: Optional[str] = None,
        client_id: Optional[str] = None,
        client_secret: Optional[str] = None,
        issuer: Optional[str] = None,
        authorization_url: Optional[str] = None,
        token_url: Optional[str] = None,
        userinfo_url: Optional[str] = None,
        jwks_url: Optional[str] = None,
    ) -> UpdateConnectionResponse:
        """Updates an existing OIDC connection.

        When the value of `issuer` changes, Stytch will attempt to retrieve the [OpenID Provider Metadata](https://openid.net/specs/openid-connect-discovery-1_0.html#ProviderMetadata) document found at `$/.well-known/openid-configuration`.
        If the metadata document can be retrieved successfully, Stytch will use it to infer the values of `authorization_url`, `token_url`, `jwks_url`, and `userinfo_url`.
        The `client_id` and `client_secret` values cannot be inferred from the metadata document, and *must* be passed in explicitly.

        If the metadata document cannot be retrieved, Stytch will still update the connection using values from the request body.

        If the metadata document can be retrieved, and values are passed in the request body, the explicit values passed in from the request body will take precedence over the values inferred from the metadata document.

        Note that a newly created connection will not become active until all of the following fields are provided:
        * `issuer`
        * `client_id`
        * `client_secret`
        * `authorization_url`
        * `token_url`
        * `userinfo_url`
        * `jwks_url`

        Fields:
          - organization_id: Globally unique UUID that identifies a specific Organization. The `organization_id` is critical to perform operations on an Organization, so be sure to preserve this value.
          - connection_id: Globally unique UUID that identifies a specific SSO `connection_id` for a Member.
          - display_name: A human-readable display name for the connection.
          - client_id: The OAuth2.0 client ID used to authenticate login attempts. This will be provided by the IdP.
          - client_secret: The secret belonging to the OAuth2.0 client used to authenticate login attempts. This will be provided by the IdP.
          - issuer: A case-sensitive `https://` URL that uniquely identifies the IdP. This will be provided by the IdP.
          - authorization_url: The location of the URL that starts an OAuth login at the IdP. This will be provided by the IdP.
          - token_url: The location of the URL that issues OAuth2.0 access tokens and OIDC ID tokens. This will be provided by the IdP.
          - userinfo_url: The location of the IDP's [UserInfo Endpoint](https://openid.net/specs/openid-connect-core-1_0.html#UserInfo). This will be provided by the IdP.
          - jwks_url: The location of the IdP's JSON Web Key Set, used to verify credentials issued by the IdP. This will be provided by the IdP.
        """  # noqa
        data: Dict[str, Any] = {
            "organization_id": organization_id,
            "connection_id": connection_id,
        }
        if display_name is not None:
            data["display_name"] = display_name
        if client_id is not None:
            data["client_id"] = client_id
        if client_secret is not None:
            data["client_secret"] = client_secret
        if issuer is not None:
            data["issuer"] = issuer
        if authorization_url is not None:
            data["authorization_url"] = authorization_url
        if token_url is not None:
            data["token_url"] = token_url
        if userinfo_url is not None:
            data["userinfo_url"] = userinfo_url
        if jwks_url is not None:
            data["jwks_url"] = jwks_url

        url = self.api_base.url_for(
            "/v1/b2b/sso/oidc/{organization_id}/connections/{connection_id}", data
        )
        res = self.sync_client.put(url, data)
        return UpdateConnectionResponse.from_json(res.response.status_code, res.json)

    async def update_connection_async(
        self,
        organization_id: str,
        connection_id: str,
        display_name: Optional[str] = None,
        client_id: Optional[str] = None,
        client_secret: Optional[str] = None,
        issuer: Optional[str] = None,
        authorization_url: Optional[str] = None,
        token_url: Optional[str] = None,
        userinfo_url: Optional[str] = None,
        jwks_url: Optional[str] = None,
    ) -> UpdateConnectionResponse:
        """Updates an existing OIDC connection.

        When the value of `issuer` changes, Stytch will attempt to retrieve the [OpenID Provider Metadata](https://openid.net/specs/openid-connect-discovery-1_0.html#ProviderMetadata) document found at `$/.well-known/openid-configuration`.
        If the metadata document can be retrieved successfully, Stytch will use it to infer the values of `authorization_url`, `token_url`, `jwks_url`, and `userinfo_url`.
        The `client_id` and `client_secret` values cannot be inferred from the metadata document, and *must* be passed in explicitly.

        If the metadata document cannot be retrieved, Stytch will still update the connection using values from the request body.

        If the metadata document can be retrieved, and values are passed in the request body, the explicit values passed in from the request body will take precedence over the values inferred from the metadata document.

        Note that a newly created connection will not become active until all of the following fields are provided:
        * `issuer`
        * `client_id`
        * `client_secret`
        * `authorization_url`
        * `token_url`
        * `userinfo_url`
        * `jwks_url`

        Fields:
          - organization_id: Globally unique UUID that identifies a specific Organization. The `organization_id` is critical to perform operations on an Organization, so be sure to preserve this value.
          - connection_id: Globally unique UUID that identifies a specific SSO `connection_id` for a Member.
          - display_name: A human-readable display name for the connection.
          - client_id: The OAuth2.0 client ID used to authenticate login attempts. This will be provided by the IdP.
          - client_secret: The secret belonging to the OAuth2.0 client used to authenticate login attempts. This will be provided by the IdP.
          - issuer: A case-sensitive `https://` URL that uniquely identifies the IdP. This will be provided by the IdP.
          - authorization_url: The location of the URL that starts an OAuth login at the IdP. This will be provided by the IdP.
          - token_url: The location of the URL that issues OAuth2.0 access tokens and OIDC ID tokens. This will be provided by the IdP.
          - userinfo_url: The location of the IDP's [UserInfo Endpoint](https://openid.net/specs/openid-connect-core-1_0.html#UserInfo). This will be provided by the IdP.
          - jwks_url: The location of the IdP's JSON Web Key Set, used to verify credentials issued by the IdP. This will be provided by the IdP.
        """  # noqa
        data: Dict[str, Any] = {
            "organization_id": organization_id,
            "connection_id": connection_id,
        }
        if display_name is not None:
            data["display_name"] = display_name
        if client_id is not None:
            data["client_id"] = client_id
        if client_secret is not None:
            data["client_secret"] = client_secret
        if issuer is not None:
            data["issuer"] = issuer
        if authorization_url is not None:
            data["authorization_url"] = authorization_url
        if token_url is not None:
            data["token_url"] = token_url
        if userinfo_url is not None:
            data["userinfo_url"] = userinfo_url
        if jwks_url is not None:
            data["jwks_url"] = jwks_url

        url = self.api_base.url_for(
            "/v1/b2b/sso/oidc/{organization_id}/connections/{connection_id}", data
        )
        res = await self.async_client.put(url, data)
        return UpdateConnectionResponse.from_json(res.response.status, res.json)