# !!!
# WARNING: This file is autogenerated
# Only modify code within MANUAL() sections
# or your changes may be overwritten later!
# !!!

from typing import Any, Dict, Optional

from stytch.core.api_base import ApiBase
from stytch.core.http.client import AsyncClient, SyncClient
from stytch.models.crypto_wallet_service import (
    CryptowalletsauthenticateResponse,
    CryptowalletsauthenticatestartResponse,
)


class CryptoWalletService:
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
        return "crypto_wallet_service"

    def CryptoWalletsAuthenticateStart(
        self,
        crypto_wallet_type: str,
        crypto_wallet_address: str,
        user_id: Optional[str] = None,
        session_token: Optional[str] = None,
        session_jwt: Optional[str] = None,
    ) -> CryptowalletsauthenticatestartResponse:
        payload: Dict[str, Any] = {
            "crypto_wallet_type": crypto_wallet_type,
            "crypto_wallet_address": crypto_wallet_address,
        }

        if user_id is not None:
            payload["user_id"] = user_id
        if session_token is not None:
            payload["session_token"] = session_token
        if session_jwt is not None:
            payload["session_jwt"] = session_jwt

        url = self.api_base.route_with_sub_url(
            self.sub_url, "/v1/crypto_wallets/authenticate/start"
        )

        res = self.sync_client.post(url, json=payload)
        return CryptowalletsauthenticatestartResponse.from_json(
            res.response.status_code, res.json
        )

    async def CryptoWalletsAuthenticateStart_async(
        self,
        crypto_wallet_type: str,
        crypto_wallet_address: str,
        user_id: Optional[str] = None,
        session_token: Optional[str] = None,
        session_jwt: Optional[str] = None,
    ) -> CryptowalletsauthenticatestartResponse:
        payload: Dict[str, Any] = {
            "crypto_wallet_type": crypto_wallet_type,
            "crypto_wallet_address": crypto_wallet_address,
        }

        if user_id is not None:
            payload["user_id"] = user_id
        if session_token is not None:
            payload["session_token"] = session_token
        if session_jwt is not None:
            payload["session_jwt"] = session_jwt

        url = self.api_base.route_with_sub_url(
            self.sub_url, "/v1/crypto_wallets/authenticate/start"
        )

        res = await self.async_client.post(url, json=payload)
        return CryptowalletsauthenticatestartResponse.from_json(
            res.response.status, res.json
        )

    def CryptoWalletsAuthenticate(
        self,
        crypto_wallet_type: str,
        crypto_wallet_address: str,
        signature: str,
        session_token: Optional[str] = None,
        session_duration_minutes: Optional[int] = None,
        session_jwt: Optional[str] = None,
        session_custom_claims: Optional[Dict[str, str]] = None,
    ) -> CryptowalletsauthenticateResponse:
        payload: Dict[str, Any] = {
            "crypto_wallet_type": crypto_wallet_type,
            "crypto_wallet_address": crypto_wallet_address,
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
            self.sub_url, "/v1/crypto_wallets/authenticate"
        )

        res = self.sync_client.post(url, json=payload)
        return CryptowalletsauthenticateResponse.from_json(
            res.response.status_code, res.json
        )

    async def CryptoWalletsAuthenticate_async(
        self,
        crypto_wallet_type: str,
        crypto_wallet_address: str,
        signature: str,
        session_token: Optional[str] = None,
        session_duration_minutes: Optional[int] = None,
        session_jwt: Optional[str] = None,
        session_custom_claims: Optional[Dict[str, str]] = None,
    ) -> CryptowalletsauthenticateResponse:
        payload: Dict[str, Any] = {
            "crypto_wallet_type": crypto_wallet_type,
            "crypto_wallet_address": crypto_wallet_address,
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
            self.sub_url, "/v1/crypto_wallets/authenticate"
        )

        res = await self.async_client.post(url, json=payload)
        return CryptowalletsauthenticateResponse.from_json(
            res.response.status, res.json
        )
