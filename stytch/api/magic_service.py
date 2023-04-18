# !!!
# WARNING: This file is autogenerated
# Only modify code within MANUAL() sections
# or your changes may be overwritten later!
# !!!

from typing import Any, Dict, List, Optional, Union

import pydantic

from stytch.core.api_base import ApiBase
from stytch.core.http.client import AsyncClient, SyncClient
from stytch.models.magic_service import (
    AuthenticatemagicResponse,
    InvitebyemailResponse,
    MagiclinkredirectResponse,
    MagiclinksauthenticateResponse,
    MagiclinkscreateResponse,
    MagiclinksemailinviteResponse,
    MagiclinksemailloginorcreateResponse,
    MagiclinksemailrevokeinviteResponse,
    MagiclinksemailsendResponse,
    MagiclinksredirectcaptchaResponse,
    SdkmagiclinksemailloginorcreateResponse,
    SendmagicbyemailResponse,
)


class MagicService:
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
        return "magic_service"

    def SendMagicByEmail(
        self,
        email: str,
        magic_link_url: Optional[str] = None,
        expiration_minutes: Optional[int] = None,
        login_template_id: Optional[str] = None,
        attributes: Optional[Dict[str, str]] = None,
        login_magic_link_url: str,
        signup_magic_link_url: str,
        login_expiration_minutes: Optional[int] = None,
        signup_expiration_minutes: Optional[int] = None,
        code_challenge: Optional[str] = None,
        user_id: str,
        session_token: Optional[str] = None,
        session_jwt: Optional[str] = None,
        locale: Optional[str] = None,
        signup_template_id: Optional[str] = None,
    ) -> SendmagicbyemailResponse:

        payload: Dict[str, Any] = {
            "email": email,
            "login_magic_link_url": login_magic_link_url,
            "signup_magic_link_url": signup_magic_link_url,
            "user_id": user_id,
        }

        if magic_link_url is not None:
            payload["magic_link_url"] = magic_link_url
        if expiration_minutes is not None:
            payload["expiration_minutes"] = expiration_minutes
        if login_template_id is not None:
            payload["login_template_id"] = login_template_id
        if attributes is not None:
            payload["attributes"] = attributes
        if login_expiration_minutes is not None:
            payload["login_expiration_minutes"] = login_expiration_minutes
        if signup_expiration_minutes is not None:
            payload["signup_expiration_minutes"] = signup_expiration_minutes
        if code_challenge is not None:
            payload["code_challenge"] = code_challenge
        if session_token is not None:
            payload["session_token"] = session_token
        if session_jwt is not None:
            payload["session_jwt"] = session_jwt
        if locale is not None:
            payload["locale"] = locale
        if signup_template_id is not None:
            payload["signup_template_id"] = signup_template_id

        url = self.api_base.route_with_sub_url(self.sub_url, "/v1/magic_links/send_by_email")

        res = self.sync_client.post(url, json=payload)
        return SendmagicbyemailResponse.from_json(res.response.status_code, res.json)

    async def SendMagicByEmail_async(
      self,
      email: str,
      magic_link_url: Optional[str] = None,
      expiration_minutes: Optional[int] = None,
      login_template_id: Optional[str] = None,
      attributes: Optional[Dict[str, str]] = None,
      login_magic_link_url: str,
      signup_magic_link_url: str,
      login_expiration_minutes: Optional[int] = None,
      signup_expiration_minutes: Optional[int] = None,
      code_challenge: Optional[str] = None,
      user_id: str,
      session_token: Optional[str] = None,
      session_jwt: Optional[str] = None,
      locale: Optional[str] = None,
      signup_template_id: Optional[str] = None,
    ) -> SendmagicbyemailResponse:

        payload: Dict[str, Any] = {
            "email": email,
            "login_magic_link_url": login_magic_link_url,
            "signup_magic_link_url": signup_magic_link_url,
            "user_id": user_id,
        }

        if magic_link_url is not None:
            payload["magic_link_url"] = magic_link_url
        if expiration_minutes is not None:
            payload["expiration_minutes"] = expiration_minutes
        if login_template_id is not None:
            payload["login_template_id"] = login_template_id
        if attributes is not None:
            payload["attributes"] = attributes
        if login_expiration_minutes is not None:
            payload["login_expiration_minutes"] = login_expiration_minutes
        if signup_expiration_minutes is not None:
            payload["signup_expiration_minutes"] = signup_expiration_minutes
        if code_challenge is not None:
            payload["code_challenge"] = code_challenge
        if session_token is not None:
            payload["session_token"] = session_token
        if session_jwt is not None:
            payload["session_jwt"] = session_jwt
        if locale is not None:
            payload["locale"] = locale
        if signup_template_id is not None:
            payload["signup_template_id"] = signup_template_id

        url = self.api_base.route_with_sub_url(self.sub_url, "/v1/magic_links/send_by_email")

        res = await self.async_client.post(url, json=payload)
        return SendmagicbyemailResponse.from_json(res.response.status, res.json)

    def MagicLinksEmailSend(
        self,
        email: str,
        magic_link_url: Optional[str] = None,
        expiration_minutes: Optional[int] = None,
        login_template_id: Optional[str] = None,
        attributes: Optional[Dict[str, str]] = None,
        login_magic_link_url: str,
        signup_magic_link_url: str,
        login_expiration_minutes: Optional[int] = None,
        signup_expiration_minutes: Optional[int] = None,
        code_challenge: Optional[str] = None,
        user_id: str,
        session_token: Optional[str] = None,
        session_jwt: Optional[str] = None,
        locale: Optional[str] = None,
        signup_template_id: Optional[str] = None,
    ) -> MagiclinksemailsendResponse:

        payload: Dict[str, Any] = {
            "email": email,
            "login_magic_link_url": login_magic_link_url,
            "signup_magic_link_url": signup_magic_link_url,
            "user_id": user_id,
        }

        if magic_link_url is not None:
            payload["magic_link_url"] = magic_link_url
        if expiration_minutes is not None:
            payload["expiration_minutes"] = expiration_minutes
        if login_template_id is not None:
            payload["login_template_id"] = login_template_id
        if attributes is not None:
            payload["attributes"] = attributes
        if login_expiration_minutes is not None:
            payload["login_expiration_minutes"] = login_expiration_minutes
        if signup_expiration_minutes is not None:
            payload["signup_expiration_minutes"] = signup_expiration_minutes
        if code_challenge is not None:
            payload["code_challenge"] = code_challenge
        if session_token is not None:
            payload["session_token"] = session_token
        if session_jwt is not None:
            payload["session_jwt"] = session_jwt
        if locale is not None:
            payload["locale"] = locale
        if signup_template_id is not None:
            payload["signup_template_id"] = signup_template_id

        url = self.api_base.route_with_sub_url(self.sub_url, "/v1/magic_links/email/send")

        res = self.sync_client.post(url, json=payload)
        return MagiclinksemailsendResponse.from_json(res.response.status_code, res.json)

    async def MagicLinksEmailSend_async(
      self,
      email: str,
      magic_link_url: Optional[str] = None,
      expiration_minutes: Optional[int] = None,
      login_template_id: Optional[str] = None,
      attributes: Optional[Dict[str, str]] = None,
      login_magic_link_url: str,
      signup_magic_link_url: str,
      login_expiration_minutes: Optional[int] = None,
      signup_expiration_minutes: Optional[int] = None,
      code_challenge: Optional[str] = None,
      user_id: str,
      session_token: Optional[str] = None,
      session_jwt: Optional[str] = None,
      locale: Optional[str] = None,
      signup_template_id: Optional[str] = None,
    ) -> MagiclinksemailsendResponse:

        payload: Dict[str, Any] = {
            "email": email,
            "login_magic_link_url": login_magic_link_url,
            "signup_magic_link_url": signup_magic_link_url,
            "user_id": user_id,
        }

        if magic_link_url is not None:
            payload["magic_link_url"] = magic_link_url
        if expiration_minutes is not None:
            payload["expiration_minutes"] = expiration_minutes
        if login_template_id is not None:
            payload["login_template_id"] = login_template_id
        if attributes is not None:
            payload["attributes"] = attributes
        if login_expiration_minutes is not None:
            payload["login_expiration_minutes"] = login_expiration_minutes
        if signup_expiration_minutes is not None:
            payload["signup_expiration_minutes"] = signup_expiration_minutes
        if code_challenge is not None:
            payload["code_challenge"] = code_challenge
        if session_token is not None:
            payload["session_token"] = session_token
        if session_jwt is not None:
            payload["session_jwt"] = session_jwt
        if locale is not None:
            payload["locale"] = locale
        if signup_template_id is not None:
            payload["signup_template_id"] = signup_template_id

        url = self.api_base.route_with_sub_url(self.sub_url, "/v1/magic_links/email/send")

        res = await self.async_client.post(url, json=payload)
        return MagiclinksemailsendResponse.from_json(res.response.status, res.json)

    def AuthenticateMagic(
        self,
        token: str,
        attributes: Optional[Dict[str, str]] = None,
        options: Optional[Dict[str, str]] = None,
        session_token: Optional[str] = None,
        session_duration_minutes: Optional[int] = None,
        session_jwt: Optional[str] = None,
        session_custom_claims: Optional[Dict[str, Any]] = None,
        code_verifier: Optional[str] = None,
    ) -> AuthenticatemagicResponse:

        payload: Dict[str, Any] = {
            "token": token,
        }

        if attributes is not None:
            payload["attributes"] = attributes
        if options is not None:
            payload["options"] = options
        if session_token is not None:
            payload["session_token"] = session_token
        if session_duration_minutes is not None:
            payload["session_duration_minutes"] = session_duration_minutes
        if session_jwt is not None:
            payload["session_jwt"] = session_jwt
        if session_custom_claims is not None:
            payload["session_custom_claims"] = session_custom_claims
        if code_verifier is not None:
            payload["code_verifier"] = code_verifier

        url = self.api_base.route_with_sub_url(self.sub_url, "/v1/magic_links/{token}/authenticate")

        res = self.sync_client.post(url, json=payload)
        return AuthenticatemagicResponse.from_json(res.response.status_code, res.json)

    async def AuthenticateMagic_async(
      self,
      token: str,
      attributes: Optional[Dict[str, str]] = None,
      options: Optional[Dict[str, str]] = None,
      session_token: Optional[str] = None,
      session_duration_minutes: Optional[int] = None,
      session_jwt: Optional[str] = None,
      session_custom_claims: Optional[Dict[str, Any]] = None,
      code_verifier: Optional[str] = None,
    ) -> AuthenticatemagicResponse:

        payload: Dict[str, Any] = {
            "token": token,
        }

        if attributes is not None:
            payload["attributes"] = attributes
        if options is not None:
            payload["options"] = options
        if session_token is not None:
            payload["session_token"] = session_token
        if session_duration_minutes is not None:
            payload["session_duration_minutes"] = session_duration_minutes
        if session_jwt is not None:
            payload["session_jwt"] = session_jwt
        if session_custom_claims is not None:
            payload["session_custom_claims"] = session_custom_claims
        if code_verifier is not None:
            payload["code_verifier"] = code_verifier

        url = self.api_base.route_with_sub_url(self.sub_url, "/v1/magic_links/{token}/authenticate")

        res = await self.async_client.post(url, json=payload)
        return AuthenticatemagicResponse.from_json(res.response.status, res.json)

    def MagicLinksAuthenticate(
        self,
        token: str,
        attributes: Optional[Dict[str, str]] = None,
        options: Optional[Dict[str, str]] = None,
        session_token: Optional[str] = None,
        session_duration_minutes: Optional[int] = None,
        session_jwt: Optional[str] = None,
        session_custom_claims: Optional[Dict[str, Any]] = None,
        code_verifier: Optional[str] = None,
    ) -> MagiclinksauthenticateResponse:

        payload: Dict[str, Any] = {
            "token": token,
        }

        if attributes is not None:
            payload["attributes"] = attributes
        if options is not None:
            payload["options"] = options
        if session_token is not None:
            payload["session_token"] = session_token
        if session_duration_minutes is not None:
            payload["session_duration_minutes"] = session_duration_minutes
        if session_jwt is not None:
            payload["session_jwt"] = session_jwt
        if session_custom_claims is not None:
            payload["session_custom_claims"] = session_custom_claims
        if code_verifier is not None:
            payload["code_verifier"] = code_verifier

        url = self.api_base.route_with_sub_url(self.sub_url, "/v1/magic_links/authenticate")

        res = self.sync_client.post(url, json=payload)
        return MagiclinksauthenticateResponse.from_json(res.response.status_code, res.json)

    async def MagicLinksAuthenticate_async(
      self,
      token: str,
      attributes: Optional[Dict[str, str]] = None,
      options: Optional[Dict[str, str]] = None,
      session_token: Optional[str] = None,
      session_duration_minutes: Optional[int] = None,
      session_jwt: Optional[str] = None,
      session_custom_claims: Optional[Dict[str, Any]] = None,
      code_verifier: Optional[str] = None,
    ) -> MagiclinksauthenticateResponse:

        payload: Dict[str, Any] = {
            "token": token,
        }

        if attributes is not None:
            payload["attributes"] = attributes
        if options is not None:
            payload["options"] = options
        if session_token is not None:
            payload["session_token"] = session_token
        if session_duration_minutes is not None:
            payload["session_duration_minutes"] = session_duration_minutes
        if session_jwt is not None:
            payload["session_jwt"] = session_jwt
        if session_custom_claims is not None:
            payload["session_custom_claims"] = session_custom_claims
        if code_verifier is not None:
            payload["code_verifier"] = code_verifier

        url = self.api_base.route_with_sub_url(self.sub_url, "/v1/magic_links/authenticate")

        res = await self.async_client.post(url, json=payload)
        return MagiclinksauthenticateResponse.from_json(res.response.status, res.json)

    def MagicLinksEmailLoginOrCreate(
        self,
        email: str,
        login_magic_link_url: str,
        signup_magic_link_url: str,
        login_expiration_minutes: Optional[int] = None,
        signup_expiration_minutes: Optional[int] = None,
        login_template_id: Optional[str] = None,
        signup_template_id: Optional[str] = None,
        attributes: Optional[Dict[str, str]] = None,
        create_user_as_pending: bool,
        code_challenge: Optional[str] = None,
        locale: Optional[str] = None,
    ) -> MagiclinksemailloginorcreateResponse:

        payload: Dict[str, Any] = {
            "email": email,
            "login_magic_link_url": login_magic_link_url,
            "signup_magic_link_url": signup_magic_link_url,
            "create_user_as_pending": create_user_as_pending,
        }

        if login_expiration_minutes is not None:
            payload["login_expiration_minutes"] = login_expiration_minutes
        if signup_expiration_minutes is not None:
            payload["signup_expiration_minutes"] = signup_expiration_minutes
        if login_template_id is not None:
            payload["login_template_id"] = login_template_id
        if signup_template_id is not None:
            payload["signup_template_id"] = signup_template_id
        if attributes is not None:
            payload["attributes"] = attributes
        if code_challenge is not None:
            payload["code_challenge"] = code_challenge
        if locale is not None:
            payload["locale"] = locale

        url = self.api_base.route_with_sub_url(self.sub_url, "/v1/magic_links/email/login_or_create")

        res = self.sync_client.post(url, json=payload)
        return MagiclinksemailloginorcreateResponse.from_json(res.response.status_code, res.json)

    async def MagicLinksEmailLoginOrCreate_async(
      self,
      email: str,
      login_magic_link_url: str,
      signup_magic_link_url: str,
      login_expiration_minutes: Optional[int] = None,
      signup_expiration_minutes: Optional[int] = None,
      login_template_id: Optional[str] = None,
      signup_template_id: Optional[str] = None,
      attributes: Optional[Dict[str, str]] = None,
      create_user_as_pending: bool,
      code_challenge: Optional[str] = None,
      locale: Optional[str] = None,
    ) -> MagiclinksemailloginorcreateResponse:

        payload: Dict[str, Any] = {
            "email": email,
            "login_magic_link_url": login_magic_link_url,
            "signup_magic_link_url": signup_magic_link_url,
            "create_user_as_pending": create_user_as_pending,
        }

        if login_expiration_minutes is not None:
            payload["login_expiration_minutes"] = login_expiration_minutes
        if signup_expiration_minutes is not None:
            payload["signup_expiration_minutes"] = signup_expiration_minutes
        if login_template_id is not None:
            payload["login_template_id"] = login_template_id
        if signup_template_id is not None:
            payload["signup_template_id"] = signup_template_id
        if attributes is not None:
            payload["attributes"] = attributes
        if code_challenge is not None:
            payload["code_challenge"] = code_challenge
        if locale is not None:
            payload["locale"] = locale

        url = self.api_base.route_with_sub_url(self.sub_url, "/v1/magic_links/email/login_or_create")

        res = await self.async_client.post(url, json=payload)
        return MagiclinksemailloginorcreateResponse.from_json(res.response.status, res.json)

    def SDKMagicLinksEmailLoginOrCreate(
        self,
        public_token: str,
        request: None,
    ) -> SdkmagiclinksemailloginorcreateResponse:

        payload: Dict[str, Any] = {
            "public_token": public_token,
        }

        if request is not None:
            payload["request"] = request

        url = self.api_base.route_with_sub_url(self.sub_url, "/v1/sdk/magic_links/email/login_or_create")

        res = self.sync_client.post(url, json=payload)
        return SdkmagiclinksemailloginorcreateResponse.from_json(res.response.status_code, res.json)

    async def SDKMagicLinksEmailLoginOrCreate_async(
      self,
      public_token: str,
      request: None,
    ) -> SdkmagiclinksemailloginorcreateResponse:

        payload: Dict[str, Any] = {
            "public_token": public_token,
        }

        if request is not None:
            payload["request"] = request

        url = self.api_base.route_with_sub_url(self.sub_url, "/v1/sdk/magic_links/email/login_or_create")

        res = await self.async_client.post(url, json=payload)
        return SdkmagiclinksemailloginorcreateResponse.from_json(res.response.status, res.json)

    def InviteByEmail(
        self,
        email: str,
        magic_link_url: Optional[str] = None,
        expiration_minutes: Optional[int] = None,
        invite_template_id: Optional[str] = None,
        attributes: Optional[Dict[str, str]] = None,
        name: None,
        invite_magic_link_url: str,
        invite_expiration_minutes: Optional[int] = None,
        locale: Optional[str] = None,
    ) -> InvitebyemailResponse:

        payload: Dict[str, Any] = {
            "email": email,
            "invite_magic_link_url": invite_magic_link_url,
        }

        if magic_link_url is not None:
            payload["magic_link_url"] = magic_link_url
        if expiration_minutes is not None:
            payload["expiration_minutes"] = expiration_minutes
        if invite_template_id is not None:
            payload["invite_template_id"] = invite_template_id
        if attributes is not None:
            payload["attributes"] = attributes
        if name is not None:
            payload["name"] = name
        if invite_expiration_minutes is not None:
            payload["invite_expiration_minutes"] = invite_expiration_minutes
        if locale is not None:
            payload["locale"] = locale

        url = self.api_base.route_with_sub_url(self.sub_url, "/v1/magic_links/invite_by_email")

        res = self.sync_client.post(url, json=payload)
        return InvitebyemailResponse.from_json(res.response.status_code, res.json)

    async def InviteByEmail_async(
      self,
      email: str,
      magic_link_url: Optional[str] = None,
      expiration_minutes: Optional[int] = None,
      invite_template_id: Optional[str] = None,
      attributes: Optional[Dict[str, str]] = None,
      name: None,
      invite_magic_link_url: str,
      invite_expiration_minutes: Optional[int] = None,
      locale: Optional[str] = None,
    ) -> InvitebyemailResponse:

        payload: Dict[str, Any] = {
            "email": email,
            "invite_magic_link_url": invite_magic_link_url,
        }

        if magic_link_url is not None:
            payload["magic_link_url"] = magic_link_url
        if expiration_minutes is not None:
            payload["expiration_minutes"] = expiration_minutes
        if invite_template_id is not None:
            payload["invite_template_id"] = invite_template_id
        if attributes is not None:
            payload["attributes"] = attributes
        if name is not None:
            payload["name"] = name
        if invite_expiration_minutes is not None:
            payload["invite_expiration_minutes"] = invite_expiration_minutes
        if locale is not None:
            payload["locale"] = locale

        url = self.api_base.route_with_sub_url(self.sub_url, "/v1/magic_links/invite_by_email")

        res = await self.async_client.post(url, json=payload)
        return InvitebyemailResponse.from_json(res.response.status, res.json)

    def MagicLinksEmailInvite(
        self,
        email: str,
        magic_link_url: Optional[str] = None,
        expiration_minutes: Optional[int] = None,
        invite_template_id: Optional[str] = None,
        attributes: Optional[Dict[str, str]] = None,
        name: None,
        invite_magic_link_url: str,
        invite_expiration_minutes: Optional[int] = None,
        locale: Optional[str] = None,
    ) -> MagiclinksemailinviteResponse:

        payload: Dict[str, Any] = {
            "email": email,
            "invite_magic_link_url": invite_magic_link_url,
        }

        if magic_link_url is not None:
            payload["magic_link_url"] = magic_link_url
        if expiration_minutes is not None:
            payload["expiration_minutes"] = expiration_minutes
        if invite_template_id is not None:
            payload["invite_template_id"] = invite_template_id
        if attributes is not None:
            payload["attributes"] = attributes
        if name is not None:
            payload["name"] = name
        if invite_expiration_minutes is not None:
            payload["invite_expiration_minutes"] = invite_expiration_minutes
        if locale is not None:
            payload["locale"] = locale

        url = self.api_base.route_with_sub_url(self.sub_url, "/v1/magic_links/email/invite")

        res = self.sync_client.post(url, json=payload)
        return MagiclinksemailinviteResponse.from_json(res.response.status_code, res.json)

    async def MagicLinksEmailInvite_async(
      self,
      email: str,
      magic_link_url: Optional[str] = None,
      expiration_minutes: Optional[int] = None,
      invite_template_id: Optional[str] = None,
      attributes: Optional[Dict[str, str]] = None,
      name: None,
      invite_magic_link_url: str,
      invite_expiration_minutes: Optional[int] = None,
      locale: Optional[str] = None,
    ) -> MagiclinksemailinviteResponse:

        payload: Dict[str, Any] = {
            "email": email,
            "invite_magic_link_url": invite_magic_link_url,
        }

        if magic_link_url is not None:
            payload["magic_link_url"] = magic_link_url
        if expiration_minutes is not None:
            payload["expiration_minutes"] = expiration_minutes
        if invite_template_id is not None:
            payload["invite_template_id"] = invite_template_id
        if attributes is not None:
            payload["attributes"] = attributes
        if name is not None:
            payload["name"] = name
        if invite_expiration_minutes is not None:
            payload["invite_expiration_minutes"] = invite_expiration_minutes
        if locale is not None:
            payload["locale"] = locale

        url = self.api_base.route_with_sub_url(self.sub_url, "/v1/magic_links/email/invite")

        res = await self.async_client.post(url, json=payload)
        return MagiclinksemailinviteResponse.from_json(res.response.status, res.json)

    def MagicLinksEmailRevokeInvite(
        self,
        email: str,
    ) -> MagiclinksemailrevokeinviteResponse:

        payload: Dict[str, Any] = {
            "email": email,
        }


        url = self.api_base.route_with_sub_url(self.sub_url, "/v1/magic_links/email/revoke_invite")

        res = self.sync_client.post(url, json=payload)
        return MagiclinksemailrevokeinviteResponse.from_json(res.response.status_code, res.json)

    async def MagicLinksEmailRevokeInvite_async(
      self,
      email: str,
    ) -> MagiclinksemailrevokeinviteResponse:

        payload: Dict[str, Any] = {
            "email": email,
        }


        url = self.api_base.route_with_sub_url(self.sub_url, "/v1/magic_links/email/revoke_invite")

        res = await self.async_client.post(url, json=payload)
        return MagiclinksemailrevokeinviteResponse.from_json(res.response.status, res.json)

    def MagicLinkRedirect(
        self,
        public_token: str,
        token: str,
        stytch_token_type: str,
    ) -> MagiclinkredirectResponse:

        payload: Dict[str, Any] = {
            "public_token": public_token,
            "token": token,
            "stytch_token_type": stytch_token_type,
        }


        url = self.api_base.route_with_sub_url(self.sub_url, "/v1/magic_links/redirect")

        res = self.sync_client.get(url, params=payload)
        return MagiclinkredirectResponse.from_json(res.response.status_code, res.json)

    async def MagicLinkRedirect_async(
      self,
      public_token: str,
      token: str,
      stytch_token_type: str,
    ) -> MagiclinkredirectResponse:

        payload: Dict[str, Any] = {
            "public_token": public_token,
            "token": token,
            "stytch_token_type": stytch_token_type,
        }


        url = self.api_base.route_with_sub_url(self.sub_url, "/v1/magic_links/redirect")

        res = await self.async_client.get(url, params=payload)
        return MagiclinkredirectResponse.from_json(res.response.status, res.json)

    def MagicLinksRedirectCaptcha(
        self,
        public_token: str,
        redirect_url: str,
        captcha: str,
    ) -> MagiclinksredirectcaptchaResponse:

        payload: Dict[str, Any] = {
            "public_token": public_token,
            "redirect_url": redirect_url,
            "captcha": captcha,
        }


        url = self.api_base.route_with_sub_url(self.sub_url, "/v1/magic_links/redirect/captcha")

        res = self.sync_client.post(url, json=payload)
        return MagiclinksredirectcaptchaResponse.from_json(res.response.status_code, res.json)

    async def MagicLinksRedirectCaptcha_async(
      self,
      public_token: str,
      redirect_url: str,
      captcha: str,
    ) -> MagiclinksredirectcaptchaResponse:

        payload: Dict[str, Any] = {
            "public_token": public_token,
            "redirect_url": redirect_url,
            "captcha": captcha,
        }


        url = self.api_base.route_with_sub_url(self.sub_url, "/v1/magic_links/redirect/captcha")

        res = await self.async_client.post(url, json=payload)
        return MagiclinksredirectcaptchaResponse.from_json(res.response.status, res.json)

    def MagicLinksCreate(
        self,
        user_id: str,
        expiration_minutes: Optional[int] = None,
        attributes: Optional[Dict[str, str]] = None,
    ) -> MagiclinkscreateResponse:

        payload: Dict[str, Any] = {
            "user_id": user_id,
        }

        if expiration_minutes is not None:
            payload["expiration_minutes"] = expiration_minutes
        if attributes is not None:
            payload["attributes"] = attributes

        url = self.api_base.route_with_sub_url(self.sub_url, "/v1/magic_links")

        res = self.sync_client.post(url, json=payload)
        return MagiclinkscreateResponse.from_json(res.response.status_code, res.json)

    async def MagicLinksCreate_async(
      self,
      user_id: str,
      expiration_minutes: Optional[int] = None,
      attributes: Optional[Dict[str, str]] = None,
    ) -> MagiclinkscreateResponse:

        payload: Dict[str, Any] = {
            "user_id": user_id,
        }

        if expiration_minutes is not None:
            payload["expiration_minutes"] = expiration_minutes
        if attributes is not None:
            payload["attributes"] = attributes

        url = self.api_base.route_with_sub_url(self.sub_url, "/v1/magic_links")

        res = await self.async_client.post(url, json=payload)
        return MagiclinkscreateResponse.from_json(res.response.status, res.json)

