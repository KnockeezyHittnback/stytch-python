# !!!
# WARNING: This file is autogenerated
# Only modify code within MANUAL() sections
# or your changes may be overwritten later!
# !!!

from typing import Any, Dict, Optional

from stytch.core.api_base import ApiBase
from stytch.core.http.client import AsyncClient, SyncClient
from stytch.models.biometric_service import (
    BiometricsauthenticateResponse,
    BiometricsauthenticatestartResponse,
    BiometricsregisterResponse,
    BiometricsregisterstartResponse,
)


class BiometricService:
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
        return "biometric_service"

    def BiometricsRegisterStart(
        self,
        user_id: str,
        public_key: str,
    ) -> BiometricsregisterstartResponse:
        payload: Dict[str, Any] = {
            "user_id": user_id,
            "public_key": public_key,
        }

        url = self.api_base.route_with_sub_url(
            self.sub_url, "/v1/biometrics/register/start"
        )

        res = self.sync_client.post(url, json=payload)
        return BiometricsregisterstartResponse.from_json(
            res.response.status_code, res.json
        )

    async def BiometricsRegisterStart_async(
        self,
        user_id: str,
        public_key: str,
    ) -> BiometricsregisterstartResponse:
        payload: Dict[str, Any] = {
            "user_id": user_id,
            "public_key": public_key,
        }

        url = self.api_base.route_with_sub_url(
            self.sub_url, "/v1/biometrics/register/start"
        )

        res = await self.async_client.post(url, json=payload)
        return BiometricsregisterstartResponse.from_json(res.response.status, res.json)

    def BiometricsRegister(
        self,
        biometric_registration_id: str,
        signature: str,
        session_duration_minutes: Optional[int] = None,
        session_custom_claims: Optional[Dict[str, str]] = None,
    ) -> BiometricsregisterResponse:
        payload: Dict[str, Any] = {
            "biometric_registration_id": biometric_registration_id,
            "signature": signature,
        }

        if session_duration_minutes is not None:
            payload["session_duration_minutes"] = session_duration_minutes
        if session_custom_claims is not None:
            payload["session_custom_claims"] = session_custom_claims

        url = self.api_base.route_with_sub_url(self.sub_url, "/v1/biometrics/register")

        res = self.sync_client.post(url, json=payload)
        return BiometricsregisterResponse.from_json(res.response.status_code, res.json)

    async def BiometricsRegister_async(
        self,
        biometric_registration_id: str,
        signature: str,
        session_duration_minutes: Optional[int] = None,
        session_custom_claims: Optional[Dict[str, str]] = None,
    ) -> BiometricsregisterResponse:
        payload: Dict[str, Any] = {
            "biometric_registration_id": biometric_registration_id,
            "signature": signature,
        }

        if session_duration_minutes is not None:
            payload["session_duration_minutes"] = session_duration_minutes
        if session_custom_claims is not None:
            payload["session_custom_claims"] = session_custom_claims

        url = self.api_base.route_with_sub_url(self.sub_url, "/v1/biometrics/register")

        res = await self.async_client.post(url, json=payload)
        return BiometricsregisterResponse.from_json(res.response.status, res.json)

    def BiometricsAuthenticateStart(
        self,
        public_key: str,
    ) -> BiometricsauthenticatestartResponse:
        payload: Dict[str, Any] = {
            "public_key": public_key,
        }

        url = self.api_base.route_with_sub_url(
            self.sub_url, "/v1/biometrics/authenticate/start"
        )

        res = self.sync_client.post(url, json=payload)
        return BiometricsauthenticatestartResponse.from_json(
            res.response.status_code, res.json
        )

    async def BiometricsAuthenticateStart_async(
        self,
        public_key: str,
    ) -> BiometricsauthenticatestartResponse:
        payload: Dict[str, Any] = {
            "public_key": public_key,
        }

        url = self.api_base.route_with_sub_url(
            self.sub_url, "/v1/biometrics/authenticate/start"
        )

        res = await self.async_client.post(url, json=payload)
        return BiometricsauthenticatestartResponse.from_json(
            res.response.status, res.json
        )

    def BiometricsAuthenticate(
        self,
        biometric_registration_id: str,
        signature: str,
        session_token: Optional[str] = None,
        session_duration_minutes: Optional[int] = None,
        session_jwt: Optional[str] = None,
        session_custom_claims: Optional[Dict[str, str]] = None,
    ) -> BiometricsauthenticateResponse:
        payload: Dict[str, Any] = {
            "biometric_registration_id": biometric_registration_id,
            "signature": signature,
        }

        if session_token is not None:
            payload["session_token"] = session_token
        if session_duration_minutes is not None:
            payload["session_duration_minutes"] = session_duration_minutes
        if session_jwt is not None:
            payload["session_jwt"] = session_jwt
        if session_custom_claims is not None:
            payload["session_custom_claims"] = session_custom_claims

        url = self.api_base.route_with_sub_url(
            self.sub_url, "/v1/biometrics/authenticate"
        )

        res = self.sync_client.post(url, json=payload)
        return BiometricsauthenticateResponse.from_json(
            res.response.status_code, res.json
        )

    async def BiometricsAuthenticate_async(
        self,
        biometric_registration_id: str,
        signature: str,
        session_token: Optional[str] = None,
        session_duration_minutes: Optional[int] = None,
        session_jwt: Optional[str] = None,
        session_custom_claims: Optional[Dict[str, str]] = None,
    ) -> BiometricsauthenticateResponse:
        payload: Dict[str, Any] = {
            "biometric_registration_id": biometric_registration_id,
            "signature": signature,
        }

        if session_token is not None:
            payload["session_token"] = session_token
        if session_duration_minutes is not None:
            payload["session_duration_minutes"] = session_duration_minutes
        if session_jwt is not None:
            payload["session_jwt"] = session_jwt
        if session_custom_claims is not None:
            payload["session_custom_claims"] = session_custom_claims

        url = self.api_base.route_with_sub_url(
            self.sub_url, "/v1/biometrics/authenticate"
        )

        res = await self.async_client.post(url, json=payload)
        return BiometricsauthenticateResponse.from_json(res.response.status, res.json)
