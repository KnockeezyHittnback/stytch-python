# !!!
# WARNING: This file is autogenerated
# Only modify code within MANUAL() sections
# or your changes may be overwritten later!
# !!!

from typing import Any, Dict, Optional

from stytch.core.api_base import ApiBase
from stytch.core.http.client import AsyncClient, SyncClient
from stytch.models.multi_tenant_session_service import (
    MultitenantsessionsauthenticateResponse,
    MultitenantsessionsexchangeResponse,
    MultitenantsessionsgetResponse,
    MultitenantsessionsrevokeResponse,
)


class MultiTenantSessionService:
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
        return "multi_tenant_session_service"

    def MultiTenantSessionsGet(
        self,
        organization_id: str,
        member_id: str,
    ) -> MultitenantsessionsgetResponse:
        payload: Dict[str, Any] = {
            "organization_id": organization_id,
            "member_id": member_id,
        }

        url = self.api_base.route_with_sub_url(self.sub_url, "/v1/b2b/sessions")

        res = self.sync_client.get(url, params=payload)
        return MultitenantsessionsgetResponse.from_json(
            res.response.status_code, res.json
        )

    async def MultiTenantSessionsGet_async(
        self,
        organization_id: str,
        member_id: str,
    ) -> MultitenantsessionsgetResponse:
        payload: Dict[str, Any] = {
            "organization_id": organization_id,
            "member_id": member_id,
        }

        url = self.api_base.route_with_sub_url(self.sub_url, "/v1/b2b/sessions")

        res = await self.async_client.get(url, params=payload)
        return MultitenantsessionsgetResponse.from_json(res.response.status, res.json)

    def MultiTenantSessionsAuthenticate(
        self,
        session_token: Optional[str] = None,
        session_duration_minutes: Optional[int] = None,
        session_jwt: Optional[str] = None,
        session_custom_claims: Optional[Dict[str, str]] = None,
    ) -> MultitenantsessionsauthenticateResponse:
        payload: Dict[str, Any] = {}

        if session_token is not None:
            payload["session_token"] = session_token
        if session_duration_minutes is not None:
            payload["session_duration_minutes"] = session_duration_minutes
        if session_jwt is not None:
            payload["session_jwt"] = session_jwt
        if session_custom_claims is not None:
            payload["session_custom_claims"] = session_custom_claims

        url = self.api_base.route_with_sub_url(
            self.sub_url, "/v1/b2b/sessions/authenticate"
        )

        res = self.sync_client.post(url, json=payload)
        return MultitenantsessionsauthenticateResponse.from_json(
            res.response.status_code, res.json
        )

    async def MultiTenantSessionsAuthenticate_async(
        self,
        session_token: Optional[str] = None,
        session_duration_minutes: Optional[int] = None,
        session_jwt: Optional[str] = None,
        session_custom_claims: Optional[Dict[str, str]] = None,
    ) -> MultitenantsessionsauthenticateResponse:
        payload: Dict[str, Any] = {}

        if session_token is not None:
            payload["session_token"] = session_token
        if session_duration_minutes is not None:
            payload["session_duration_minutes"] = session_duration_minutes
        if session_jwt is not None:
            payload["session_jwt"] = session_jwt
        if session_custom_claims is not None:
            payload["session_custom_claims"] = session_custom_claims

        url = self.api_base.route_with_sub_url(
            self.sub_url, "/v1/b2b/sessions/authenticate"
        )

        res = await self.async_client.post(url, json=payload)
        return MultitenantsessionsauthenticateResponse.from_json(
            res.response.status, res.json
        )

    def MultiTenantSessionsRevoke(
        self,
        member_session_id: Optional[str] = None,
        session_token: Optional[str] = None,
        session_jwt: Optional[str] = None,
        member_id: Optional[str] = None,
    ) -> MultitenantsessionsrevokeResponse:
        payload: Dict[str, Any] = {}

        if member_session_id is not None:
            payload["member_session_id"] = member_session_id
        if session_token is not None:
            payload["session_token"] = session_token
        if session_jwt is not None:
            payload["session_jwt"] = session_jwt
        if member_id is not None:
            payload["member_id"] = member_id

        url = self.api_base.route_with_sub_url(self.sub_url, "/v1/b2b/sessions/revoke")

        res = self.sync_client.post(url, json=payload)
        return MultitenantsessionsrevokeResponse.from_json(
            res.response.status_code, res.json
        )

    async def MultiTenantSessionsRevoke_async(
        self,
        member_session_id: Optional[str] = None,
        session_token: Optional[str] = None,
        session_jwt: Optional[str] = None,
        member_id: Optional[str] = None,
    ) -> MultitenantsessionsrevokeResponse:
        payload: Dict[str, Any] = {}

        if member_session_id is not None:
            payload["member_session_id"] = member_session_id
        if session_token is not None:
            payload["session_token"] = session_token
        if session_jwt is not None:
            payload["session_jwt"] = session_jwt
        if member_id is not None:
            payload["member_id"] = member_id

        url = self.api_base.route_with_sub_url(self.sub_url, "/v1/b2b/sessions/revoke")

        res = await self.async_client.post(url, json=payload)
        return MultitenantsessionsrevokeResponse.from_json(
            res.response.status, res.json
        )

    def MultiTenantSessionsExchange(
        self,
        organization_id: str,
        session_token: Optional[str] = None,
        session_jwt: Optional[str] = None,
        session_duration_minutes: Optional[int] = None,
        session_custom_claims: Optional[Dict[str, str]] = None,
    ) -> MultitenantsessionsexchangeResponse:
        payload: Dict[str, Any] = {
            "organization_id": organization_id,
        }

        if session_token is not None:
            payload["session_token"] = session_token
        if session_jwt is not None:
            payload["session_jwt"] = session_jwt
        if session_duration_minutes is not None:
            payload["session_duration_minutes"] = session_duration_minutes
        if session_custom_claims is not None:
            payload["session_custom_claims"] = session_custom_claims

        url = self.api_base.route_with_sub_url(
            self.sub_url, "/v1/b2b/sessions/exchange"
        )

        res = self.sync_client.post(url, json=payload)
        return MultitenantsessionsexchangeResponse.from_json(
            res.response.status_code, res.json
        )

    async def MultiTenantSessionsExchange_async(
        self,
        organization_id: str,
        session_token: Optional[str] = None,
        session_jwt: Optional[str] = None,
        session_duration_minutes: Optional[int] = None,
        session_custom_claims: Optional[Dict[str, str]] = None,
    ) -> MultitenantsessionsexchangeResponse:
        payload: Dict[str, Any] = {
            "organization_id": organization_id,
        }

        if session_token is not None:
            payload["session_token"] = session_token
        if session_jwt is not None:
            payload["session_jwt"] = session_jwt
        if session_duration_minutes is not None:
            payload["session_duration_minutes"] = session_duration_minutes
        if session_custom_claims is not None:
            payload["session_custom_claims"] = session_custom_claims

        url = self.api_base.route_with_sub_url(
            self.sub_url, "/v1/b2b/sessions/exchange"
        )

        res = await self.async_client.post(url, json=payload)
        return MultitenantsessionsexchangeResponse.from_json(
            res.response.status, res.json
        )
