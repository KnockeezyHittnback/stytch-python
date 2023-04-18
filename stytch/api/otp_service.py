# !!!
# WARNING: This file is autogenerated
# Only modify code within MANUAL() sections
# or your changes may be overwritten later!
# !!!

from typing import Any, Dict, List, Optional, Union

import pydantic

from stytch.core.api_base import ApiBase
from stytch.core.http.client import AsyncClient, SyncClient
from stytch.models.otp_service import (
    OtpsauthenticateResponse,
    OtpsemailloginorcreateResponse,
    OtpsemailsendResponse,
    OtpssmsloginorcreateResponse,
    OtpssmssendResponse,
    OtpswhatsapploginorcreateResponse,
    OtpswhatsappsendResponse,
)


class OTPService:
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
        return "otp_service"

    def OTPsSMSSend(
        self,
        phone_number: str,
        expiration_minutes: Optional[int] = None,
        attributes: Optional[Dict[str, str]] = None,
        locale: Optional[str] = None,
        user_id: str,
        session_token: Optional[str] = None,
        session_jwt: Optional[str] = None,
    ) -> OtpssmssendResponse:

        payload: Dict[str, Any] = {
            "phone_number": phone_number,
            "user_id": user_id,
        }

        if expiration_minutes is not None:
            payload["expiration_minutes"] = expiration_minutes
        if attributes is not None:
            payload["attributes"] = attributes
        if locale is not None:
            payload["locale"] = locale
        if session_token is not None:
            payload["session_token"] = session_token
        if session_jwt is not None:
            payload["session_jwt"] = session_jwt

        url = self.api_base.route_with_sub_url(self.sub_url, "/v1/otps/sms/send")

        res = self.sync_client.post(url, json=payload)
        return OtpssmssendResponse.from_json(res.response.status_code, res.json)

    async def OTPsSMSSend_async(
      self,
      phone_number: str,
      expiration_minutes: Optional[int] = None,
      attributes: Optional[Dict[str, str]] = None,
      locale: Optional[str] = None,
      user_id: str,
      session_token: Optional[str] = None,
      session_jwt: Optional[str] = None,
    ) -> OtpssmssendResponse:

        payload: Dict[str, Any] = {
            "phone_number": phone_number,
            "user_id": user_id,
        }

        if expiration_minutes is not None:
            payload["expiration_minutes"] = expiration_minutes
        if attributes is not None:
            payload["attributes"] = attributes
        if locale is not None:
            payload["locale"] = locale
        if session_token is not None:
            payload["session_token"] = session_token
        if session_jwt is not None:
            payload["session_jwt"] = session_jwt

        url = self.api_base.route_with_sub_url(self.sub_url, "/v1/otps/sms/send")

        res = await self.async_client.post(url, json=payload)
        return OtpssmssendResponse.from_json(res.response.status, res.json)

    def OTPsSMSLoginOrCreate(
        self,
        phone_number: str,
        expiration_minutes: Optional[int] = None,
        attributes: Optional[Dict[str, str]] = None,
        create_user_as_pending: bool,
        locale: Optional[str] = None,
    ) -> OtpssmsloginorcreateResponse:

        payload: Dict[str, Any] = {
            "phone_number": phone_number,
            "create_user_as_pending": create_user_as_pending,
        }

        if expiration_minutes is not None:
            payload["expiration_minutes"] = expiration_minutes
        if attributes is not None:
            payload["attributes"] = attributes
        if locale is not None:
            payload["locale"] = locale

        url = self.api_base.route_with_sub_url(self.sub_url, "/v1/otps/sms/login_or_create")

        res = self.sync_client.post(url, json=payload)
        return OtpssmsloginorcreateResponse.from_json(res.response.status_code, res.json)

    async def OTPsSMSLoginOrCreate_async(
      self,
      phone_number: str,
      expiration_minutes: Optional[int] = None,
      attributes: Optional[Dict[str, str]] = None,
      create_user_as_pending: bool,
      locale: Optional[str] = None,
    ) -> OtpssmsloginorcreateResponse:

        payload: Dict[str, Any] = {
            "phone_number": phone_number,
            "create_user_as_pending": create_user_as_pending,
        }

        if expiration_minutes is not None:
            payload["expiration_minutes"] = expiration_minutes
        if attributes is not None:
            payload["attributes"] = attributes
        if locale is not None:
            payload["locale"] = locale

        url = self.api_base.route_with_sub_url(self.sub_url, "/v1/otps/sms/login_or_create")

        res = await self.async_client.post(url, json=payload)
        return OtpssmsloginorcreateResponse.from_json(res.response.status, res.json)

    def OTPsWhatsAppSend(
        self,
        phone_number: str,
        expiration_minutes: Optional[int] = None,
        attributes: Optional[Dict[str, str]] = None,
        locale: Optional[str] = None,
        user_id: str,
        session_token: Optional[str] = None,
        session_jwt: Optional[str] = None,
    ) -> OtpswhatsappsendResponse:

        payload: Dict[str, Any] = {
            "phone_number": phone_number,
            "user_id": user_id,
        }

        if expiration_minutes is not None:
            payload["expiration_minutes"] = expiration_minutes
        if attributes is not None:
            payload["attributes"] = attributes
        if locale is not None:
            payload["locale"] = locale
        if session_token is not None:
            payload["session_token"] = session_token
        if session_jwt is not None:
            payload["session_jwt"] = session_jwt

        url = self.api_base.route_with_sub_url(self.sub_url, "/v1/otps/whatsapp/send")

        res = self.sync_client.post(url, json=payload)
        return OtpswhatsappsendResponse.from_json(res.response.status_code, res.json)

    async def OTPsWhatsAppSend_async(
      self,
      phone_number: str,
      expiration_minutes: Optional[int] = None,
      attributes: Optional[Dict[str, str]] = None,
      locale: Optional[str] = None,
      user_id: str,
      session_token: Optional[str] = None,
      session_jwt: Optional[str] = None,
    ) -> OtpswhatsappsendResponse:

        payload: Dict[str, Any] = {
            "phone_number": phone_number,
            "user_id": user_id,
        }

        if expiration_minutes is not None:
            payload["expiration_minutes"] = expiration_minutes
        if attributes is not None:
            payload["attributes"] = attributes
        if locale is not None:
            payload["locale"] = locale
        if session_token is not None:
            payload["session_token"] = session_token
        if session_jwt is not None:
            payload["session_jwt"] = session_jwt

        url = self.api_base.route_with_sub_url(self.sub_url, "/v1/otps/whatsapp/send")

        res = await self.async_client.post(url, json=payload)
        return OtpswhatsappsendResponse.from_json(res.response.status, res.json)

    def OTPsWhatsAppLoginOrCreate(
        self,
        phone_number: str,
        expiration_minutes: Optional[int] = None,
        attributes: Optional[Dict[str, str]] = None,
        create_user_as_pending: bool,
        locale: Optional[str] = None,
    ) -> OtpswhatsapploginorcreateResponse:

        payload: Dict[str, Any] = {
            "phone_number": phone_number,
            "create_user_as_pending": create_user_as_pending,
        }

        if expiration_minutes is not None:
            payload["expiration_minutes"] = expiration_minutes
        if attributes is not None:
            payload["attributes"] = attributes
        if locale is not None:
            payload["locale"] = locale

        url = self.api_base.route_with_sub_url(self.sub_url, "/v1/otps/whatsapp/login_or_create")

        res = self.sync_client.post(url, json=payload)
        return OtpswhatsapploginorcreateResponse.from_json(res.response.status_code, res.json)

    async def OTPsWhatsAppLoginOrCreate_async(
      self,
      phone_number: str,
      expiration_minutes: Optional[int] = None,
      attributes: Optional[Dict[str, str]] = None,
      create_user_as_pending: bool,
      locale: Optional[str] = None,
    ) -> OtpswhatsapploginorcreateResponse:

        payload: Dict[str, Any] = {
            "phone_number": phone_number,
            "create_user_as_pending": create_user_as_pending,
        }

        if expiration_minutes is not None:
            payload["expiration_minutes"] = expiration_minutes
        if attributes is not None:
            payload["attributes"] = attributes
        if locale is not None:
            payload["locale"] = locale

        url = self.api_base.route_with_sub_url(self.sub_url, "/v1/otps/whatsapp/login_or_create")

        res = await self.async_client.post(url, json=payload)
        return OtpswhatsapploginorcreateResponse.from_json(res.response.status, res.json)

    def OTPsEmailSend(
        self,
        email: str,
        expiration_minutes: Optional[int] = None,
        attributes: Optional[Dict[str, str]] = None,
        locale: Optional[str] = None,
        user_id: str,
        session_token: Optional[str] = None,
        session_jwt: Optional[str] = None,
        login_template_id: Optional[str] = None,
        signup_template_id: Optional[str] = None,
    ) -> OtpsemailsendResponse:

        payload: Dict[str, Any] = {
            "email": email,
            "user_id": user_id,
        }

        if expiration_minutes is not None:
            payload["expiration_minutes"] = expiration_minutes
        if attributes is not None:
            payload["attributes"] = attributes
        if locale is not None:
            payload["locale"] = locale
        if session_token is not None:
            payload["session_token"] = session_token
        if session_jwt is not None:
            payload["session_jwt"] = session_jwt
        if login_template_id is not None:
            payload["login_template_id"] = login_template_id
        if signup_template_id is not None:
            payload["signup_template_id"] = signup_template_id

        url = self.api_base.route_with_sub_url(self.sub_url, "/v1/otps/email/send")

        res = self.sync_client.post(url, json=payload)
        return OtpsemailsendResponse.from_json(res.response.status_code, res.json)

    async def OTPsEmailSend_async(
      self,
      email: str,
      expiration_minutes: Optional[int] = None,
      attributes: Optional[Dict[str, str]] = None,
      locale: Optional[str] = None,
      user_id: str,
      session_token: Optional[str] = None,
      session_jwt: Optional[str] = None,
      login_template_id: Optional[str] = None,
      signup_template_id: Optional[str] = None,
    ) -> OtpsemailsendResponse:

        payload: Dict[str, Any] = {
            "email": email,
            "user_id": user_id,
        }

        if expiration_minutes is not None:
            payload["expiration_minutes"] = expiration_minutes
        if attributes is not None:
            payload["attributes"] = attributes
        if locale is not None:
            payload["locale"] = locale
        if session_token is not None:
            payload["session_token"] = session_token
        if session_jwt is not None:
            payload["session_jwt"] = session_jwt
        if login_template_id is not None:
            payload["login_template_id"] = login_template_id
        if signup_template_id is not None:
            payload["signup_template_id"] = signup_template_id

        url = self.api_base.route_with_sub_url(self.sub_url, "/v1/otps/email/send")

        res = await self.async_client.post(url, json=payload)
        return OtpsemailsendResponse.from_json(res.response.status, res.json)

    def OTPsEmailLoginOrCreate(
        self,
        email: str,
        expiration_minutes: Optional[int] = None,
        attributes: Optional[Dict[str, str]] = None,
        create_user_as_pending: bool,
        locale: Optional[str] = None,
        login_template_id: Optional[str] = None,
        signup_template_id: Optional[str] = None,
    ) -> OtpsemailloginorcreateResponse:

        payload: Dict[str, Any] = {
            "email": email,
            "create_user_as_pending": create_user_as_pending,
        }

        if expiration_minutes is not None:
            payload["expiration_minutes"] = expiration_minutes
        if attributes is not None:
            payload["attributes"] = attributes
        if locale is not None:
            payload["locale"] = locale
        if login_template_id is not None:
            payload["login_template_id"] = login_template_id
        if signup_template_id is not None:
            payload["signup_template_id"] = signup_template_id

        url = self.api_base.route_with_sub_url(self.sub_url, "/v1/otps/email/login_or_create")

        res = self.sync_client.post(url, json=payload)
        return OtpsemailloginorcreateResponse.from_json(res.response.status_code, res.json)

    async def OTPsEmailLoginOrCreate_async(
      self,
      email: str,
      expiration_minutes: Optional[int] = None,
      attributes: Optional[Dict[str, str]] = None,
      create_user_as_pending: bool,
      locale: Optional[str] = None,
      login_template_id: Optional[str] = None,
      signup_template_id: Optional[str] = None,
    ) -> OtpsemailloginorcreateResponse:

        payload: Dict[str, Any] = {
            "email": email,
            "create_user_as_pending": create_user_as_pending,
        }

        if expiration_minutes is not None:
            payload["expiration_minutes"] = expiration_minutes
        if attributes is not None:
            payload["attributes"] = attributes
        if locale is not None:
            payload["locale"] = locale
        if login_template_id is not None:
            payload["login_template_id"] = login_template_id
        if signup_template_id is not None:
            payload["signup_template_id"] = signup_template_id

        url = self.api_base.route_with_sub_url(self.sub_url, "/v1/otps/email/login_or_create")

        res = await self.async_client.post(url, json=payload)
        return OtpsemailloginorcreateResponse.from_json(res.response.status, res.json)

    def OTPsAuthenticate(
        self,
        method_id: str,
        code: str,
        attributes: Optional[Dict[str, str]] = None,
        options: Optional[Dict[str, str]] = None,
        session_token: Optional[str] = None,
        session_duration_minutes: Optional[int] = None,
        session_jwt: Optional[str] = None,
        session_custom_claims: Optional[Dict[str, str]] = None,
    ) -> OtpsauthenticateResponse:

        payload: Dict[str, Any] = {
            "method_id": method_id,
            "code": code,
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

        url = self.api_base.route_with_sub_url(self.sub_url, "/v1/otps/authenticate")

        res = self.sync_client.post(url, json=payload)
        return OtpsauthenticateResponse.from_json(res.response.status_code, res.json)

    async def OTPsAuthenticate_async(
      self,
      method_id: str,
      code: str,
      attributes: Optional[Dict[str, str]] = None,
      options: Optional[Dict[str, str]] = None,
      session_token: Optional[str] = None,
      session_duration_minutes: Optional[int] = None,
      session_jwt: Optional[str] = None,
      session_custom_claims: Optional[Dict[str, str]] = None,
    ) -> OtpsauthenticateResponse:

        payload: Dict[str, Any] = {
            "method_id": method_id,
            "code": code,
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

        url = self.api_base.route_with_sub_url(self.sub_url, "/v1/otps/authenticate")

        res = await self.async_client.post(url, json=payload)
        return OtpsauthenticateResponse.from_json(res.response.status, res.json)

