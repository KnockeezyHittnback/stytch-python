# !!!
# WARNING: This file is autogenerated
# Only modify code within MANUAL() sections
# or your changes may be overwritten later!
# !!!

from __future__ import annotations

from typing import Any, Dict, Optional, Union

from stytch.consumer.models.attribute import Attributes
from stytch.consumer.models.magic_links_email import (
    InviteRequestLocale,
    InviteResponse,
    LoginOrCreateRequestLocale,
    LoginOrCreateResponse,
    RevokeInviteResponse,
    SendRequestLocale,
    SendResponse,
)
from stytch.consumer.models.users import Name
from stytch.core.api_base import ApiBase
from stytch.core.http.client import AsyncClient, SyncClient


class Email:
    def __init__(
        self, api_base: ApiBase, sync_client: SyncClient, async_client: AsyncClient
    ) -> None:
        self.api_base = api_base
        self.sync_client = sync_client
        self.async_client = async_client

    def send(
        self,
        email: str,
        login_template_id: Optional[str] = None,
        attributes: Optional[Attributes] = None,
        login_magic_link_url: Optional[str] = None,
        signup_magic_link_url: Optional[str] = None,
        login_expiration_minutes: Optional[int] = None,
        signup_expiration_minutes: Optional[int] = None,
        code_challenge: Optional[str] = None,
        user_id: Optional[str] = None,
        session_token: Optional[str] = None,
        session_jwt: Optional[str] = None,
        locale: Optional[Union[SendRequestLocale, str]] = None,
        signup_template_id: Optional[str] = None,
    ) -> SendResponse:
        """Send a magic link to an existing Stytch user using their email address. If you'd like to create a user and send them a magic link by email with one request, use our [log in or create endpoint](https://stytch.com/docs/api/log-in-or-create-user-by-email).

        ### Add an email to an existing user
        This endpoint also allows you to add a new email address to an existing Stytch User. Including a `user_id`, `session_token`, or `session_jwt` in your Send Magic Link by email request will add the new, unverified email address to the existing Stytch User. If the user successfully authenticates within 5 minutes, the new email address will be marked as verified and remain permanently on the existing Stytch User. Otherwise, it will be removed from the User object, and any subsequent login requests using that email address will create a new User.

        ### Next steps
        The user is emailed a magic link which redirects them to the provided [redirect URL](https://stytch.com/docs/guides/magic-links/email-magic-links/redirect-routing). Collect the `token` from the URL query parameters, and call [Authenticate magic link](https://stytch.com/docs/api/authenticate-magic-link) to complete authentication.

        Fields:
          - email: The email address of the User to send the Magic Link to.
          - login_template_id: Use a custom template for login emails. By default, it will use your default email template. The template must be a template using our built-in customizations or a custom HTML email for Magic links - Login.
          - attributes: Provided attributes help with fraud detection.
          - login_magic_link_url: The URL the end user clicks from the login Email Magic Link. This should be a URL that your app receives and parses and subsequently send an API request to authenticate the Magic Link and log in the User. If this value is not passed, the default login redirect URL that you set in your Dashboard is used. If you have not set a default login redirect URL, an error is returned.
          - signup_magic_link_url: The URL the end user clicks from the sign-up Email Magic Link. This should be a URL that your app receives and parses and subsequently send an API request to authenticate the Magic Link and sign-up the User. If this value is not passed, the default sign-up redirect URL that you set in your Dashboard is used. If you have not set a default sign-up redirect URL, an error is returned.
          - login_expiration_minutes: Set the expiration for the login email magic link, in minutes. By default, it expires in 1 hour. The minimum expiration is 5 minutes and the maximum is 7 days (10080 mins).
          - signup_expiration_minutes: Set the expiration for the sign-up email magic link, in minutes. By default, it expires in 1 week. The minimum expiration is 5 minutes and the maximum is 7 days (10080 mins).
          - code_challenge: A base64url encoded SHA256 hash of a one time secret used to validate that the request starts and ends on the same device.
          - user_id: The unique ID of a specific User.
          - session_token: The `session_token` of the user to associate the email with.
          - session_jwt: The `session_jwt` of the user to associate the email with.
          - locale: Used to determine which language to use when sending the user this delivery method. Parameter is a [IETF BCP 47 language tag](https://www.w3.org/International/articles/language-tags/), e.g. `"en"`.

        Currently supported languages are English (`"en"`), Spanish (`"es"`), and Brazilian Portuguese (`"pt-br"`); if no value is provided, the copy defaults to English.

        Request support for additional languages [here](https://docs.google.com/forms/d/e/1FAIpQLScZSpAu_m2AmLXRT3F3kap-s_mcV6UTBitYn6CdyWP0-o7YjQ/viewform?usp=sf_link")!

          - signup_template_id: Use a custom template for sign-up emails. By default, it will use your default email template. The template must be a template using our built-in customizations or a custom HTML email for Magic links - Sign-up.
        """  # noqa
        headers: Dict[str, str] = {}
        data: Dict[str, Any] = {
            "email": email,
        }
        if login_template_id is not None:
            data["login_template_id"] = login_template_id
        if attributes is not None:
            data["attributes"] = attributes.dict()
        if login_magic_link_url is not None:
            data["login_magic_link_url"] = login_magic_link_url
        if signup_magic_link_url is not None:
            data["signup_magic_link_url"] = signup_magic_link_url
        if login_expiration_minutes is not None:
            data["login_expiration_minutes"] = login_expiration_minutes
        if signup_expiration_minutes is not None:
            data["signup_expiration_minutes"] = signup_expiration_minutes
        if code_challenge is not None:
            data["code_challenge"] = code_challenge
        if user_id is not None:
            data["user_id"] = user_id
        if session_token is not None:
            data["session_token"] = session_token
        if session_jwt is not None:
            data["session_jwt"] = session_jwt
        if locale is not None:
            data["locale"] = locale
        if signup_template_id is not None:
            data["signup_template_id"] = signup_template_id

        url = self.api_base.url_for("/v1/magic_links/email/send", data)
        res = self.sync_client.post(url, data, headers)
        return SendResponse.from_json(res.response.status_code, res.json)

    async def send_async(
        self,
        email: str,
        login_template_id: Optional[str] = None,
        attributes: Optional[Attributes] = None,
        login_magic_link_url: Optional[str] = None,
        signup_magic_link_url: Optional[str] = None,
        login_expiration_minutes: Optional[int] = None,
        signup_expiration_minutes: Optional[int] = None,
        code_challenge: Optional[str] = None,
        user_id: Optional[str] = None,
        session_token: Optional[str] = None,
        session_jwt: Optional[str] = None,
        locale: Optional[SendRequestLocale] = None,
        signup_template_id: Optional[str] = None,
    ) -> SendResponse:
        """Send a magic link to an existing Stytch user using their email address. If you'd like to create a user and send them a magic link by email with one request, use our [log in or create endpoint](https://stytch.com/docs/api/log-in-or-create-user-by-email).

        ### Add an email to an existing user
        This endpoint also allows you to add a new email address to an existing Stytch User. Including a `user_id`, `session_token`, or `session_jwt` in your Send Magic Link by email request will add the new, unverified email address to the existing Stytch User. If the user successfully authenticates within 5 minutes, the new email address will be marked as verified and remain permanently on the existing Stytch User. Otherwise, it will be removed from the User object, and any subsequent login requests using that email address will create a new User.

        ### Next steps
        The user is emailed a magic link which redirects them to the provided [redirect URL](https://stytch.com/docs/guides/magic-links/email-magic-links/redirect-routing). Collect the `token` from the URL query parameters, and call [Authenticate magic link](https://stytch.com/docs/api/authenticate-magic-link) to complete authentication.

        Fields:
          - email: The email address of the User to send the Magic Link to.
          - login_template_id: Use a custom template for login emails. By default, it will use your default email template. The template must be a template using our built-in customizations or a custom HTML email for Magic links - Login.
          - attributes: Provided attributes help with fraud detection.
          - login_magic_link_url: The URL the end user clicks from the login Email Magic Link. This should be a URL that your app receives and parses and subsequently send an API request to authenticate the Magic Link and log in the User. If this value is not passed, the default login redirect URL that you set in your Dashboard is used. If you have not set a default login redirect URL, an error is returned.
          - signup_magic_link_url: The URL the end user clicks from the sign-up Email Magic Link. This should be a URL that your app receives and parses and subsequently send an API request to authenticate the Magic Link and sign-up the User. If this value is not passed, the default sign-up redirect URL that you set in your Dashboard is used. If you have not set a default sign-up redirect URL, an error is returned.
          - login_expiration_minutes: Set the expiration for the login email magic link, in minutes. By default, it expires in 1 hour. The minimum expiration is 5 minutes and the maximum is 7 days (10080 mins).
          - signup_expiration_minutes: Set the expiration for the sign-up email magic link, in minutes. By default, it expires in 1 week. The minimum expiration is 5 minutes and the maximum is 7 days (10080 mins).
          - code_challenge: A base64url encoded SHA256 hash of a one time secret used to validate that the request starts and ends on the same device.
          - user_id: The unique ID of a specific User.
          - session_token: The `session_token` of the user to associate the email with.
          - session_jwt: The `session_jwt` of the user to associate the email with.
          - locale: Used to determine which language to use when sending the user this delivery method. Parameter is a [IETF BCP 47 language tag](https://www.w3.org/International/articles/language-tags/), e.g. `"en"`.

        Currently supported languages are English (`"en"`), Spanish (`"es"`), and Brazilian Portuguese (`"pt-br"`); if no value is provided, the copy defaults to English.

        Request support for additional languages [here](https://docs.google.com/forms/d/e/1FAIpQLScZSpAu_m2AmLXRT3F3kap-s_mcV6UTBitYn6CdyWP0-o7YjQ/viewform?usp=sf_link")!

          - signup_template_id: Use a custom template for sign-up emails. By default, it will use your default email template. The template must be a template using our built-in customizations or a custom HTML email for Magic links - Sign-up.
        """  # noqa
        headers: Dict[str, str] = {}
        data: Dict[str, Any] = {
            "email": email,
        }
        if login_template_id is not None:
            data["login_template_id"] = login_template_id
        if attributes is not None:
            data["attributes"] = attributes.dict()
        if login_magic_link_url is not None:
            data["login_magic_link_url"] = login_magic_link_url
        if signup_magic_link_url is not None:
            data["signup_magic_link_url"] = signup_magic_link_url
        if login_expiration_minutes is not None:
            data["login_expiration_minutes"] = login_expiration_minutes
        if signup_expiration_minutes is not None:
            data["signup_expiration_minutes"] = signup_expiration_minutes
        if code_challenge is not None:
            data["code_challenge"] = code_challenge
        if user_id is not None:
            data["user_id"] = user_id
        if session_token is not None:
            data["session_token"] = session_token
        if session_jwt is not None:
            data["session_jwt"] = session_jwt
        if locale is not None:
            data["locale"] = locale
        if signup_template_id is not None:
            data["signup_template_id"] = signup_template_id

        url = self.api_base.url_for("/v1/magic_links/email/send", data)
        res = await self.async_client.post(url, data, headers)
        return SendResponse.from_json(res.response.status, res.json)

    def login_or_create(
        self,
        email: str,
        login_magic_link_url: Optional[str] = None,
        signup_magic_link_url: Optional[str] = None,
        login_expiration_minutes: Optional[int] = None,
        signup_expiration_minutes: Optional[int] = None,
        login_template_id: Optional[str] = None,
        signup_template_id: Optional[str] = None,
        attributes: Optional[Attributes] = None,
        create_user_as_pending: Optional[bool] = None,
        code_challenge: Optional[str] = None,
        locale: Optional[Union[LoginOrCreateRequestLocale, str]] = None,
    ) -> LoginOrCreateResponse:
        """Send either a login or signup Magic Link to the User based on if the email is associated with a User already. A new or pending User will receive a signup Magic Link. An active User will receive a login Magic Link. For more information on how to control the status your Users are created in see the `create_user_as_pending` flag.

        ### Next steps
        The User is emailed a Magic Link which redirects them to the provided [redirect URL](https://stytch.com/docs/guides/magic-links/email-magic-links/redirect-routing). Collect the `token` from the URL query parameters and call [Authenticate Magic Link](https://stytch.com/docs/api/authenticate-magic-link) to complete authentication.

        Fields:
          - email: The email address of the end user.
          - login_magic_link_url: The URL the end user clicks from the login Email Magic Link. This should be a URL that your app receives and parses and subsequently send an API request to authenticate the Magic Link and log in the User. If this value is not passed, the default login redirect URL that you set in your Dashboard is used. If you have not set a default login redirect URL, an error is returned.
          - signup_magic_link_url: The URL the end user clicks from the sign-up Email Magic Link. This should be a URL that your app receives and parses and subsequently send an API request to authenticate the Magic Link and sign-up the User. If this value is not passed, the default sign-up redirect URL that you set in your Dashboard is used. If you have not set a default sign-up redirect URL, an error is returned.
          - login_expiration_minutes: Set the expiration for the login email magic link, in minutes. By default, it expires in 1 hour. The minimum expiration is 5 minutes and the maximum is 7 days (10080 mins).
          - signup_expiration_minutes: Set the expiration for the sign-up email magic link, in minutes. By default, it expires in 1 week. The minimum expiration is 5 minutes and the maximum is 7 days (10080 mins).
          - login_template_id: Use a custom template for login emails. By default, it will use your default email template. The template must be a template using our built-in customizations or a custom HTML email for Magic links - Login.
          - signup_template_id: Use a custom template for sign-up emails. By default, it will use your default email template. The template must be a template using our built-in customizations or a custom HTML email for Magic links - Sign-up.
          - attributes: Provided attributes help with fraud detection.
          - create_user_as_pending: Flag for whether or not to save a user as pending vs active in Stytch. Defaults to false.
                If true, users will be saved with status pending in Stytch's backend until authenticated.
                If false, users will be created as active. An example usage of
                a true flag would be to require users to verify their phone by entering the OTP code before creating
                an account for them.
          - code_challenge: A base64url encoded SHA256 hash of a one time secret used to validate that the request starts and ends on the same device.
          - locale: Used to determine which language to use when sending the user this delivery method. Parameter is a [IETF BCP 47 language tag](https://www.w3.org/International/articles/language-tags/), e.g. `"en"`.

        Currently supported languages are English (`"en"`), Spanish (`"es"`), and Brazilian Portuguese (`"pt-br"`); if no value is provided, the copy defaults to English.

        Request support for additional languages [here](https://docs.google.com/forms/d/e/1FAIpQLScZSpAu_m2AmLXRT3F3kap-s_mcV6UTBitYn6CdyWP0-o7YjQ/viewform?usp=sf_link")!

        """  # noqa
        headers: Dict[str, str] = {}
        data: Dict[str, Any] = {
            "email": email,
        }
        if login_magic_link_url is not None:
            data["login_magic_link_url"] = login_magic_link_url
        if signup_magic_link_url is not None:
            data["signup_magic_link_url"] = signup_magic_link_url
        if login_expiration_minutes is not None:
            data["login_expiration_minutes"] = login_expiration_minutes
        if signup_expiration_minutes is not None:
            data["signup_expiration_minutes"] = signup_expiration_minutes
        if login_template_id is not None:
            data["login_template_id"] = login_template_id
        if signup_template_id is not None:
            data["signup_template_id"] = signup_template_id
        if attributes is not None:
            data["attributes"] = attributes.dict()
        if create_user_as_pending is not None:
            data["create_user_as_pending"] = create_user_as_pending
        if code_challenge is not None:
            data["code_challenge"] = code_challenge
        if locale is not None:
            data["locale"] = locale

        url = self.api_base.url_for("/v1/magic_links/email/login_or_create", data)
        res = self.sync_client.post(url, data, headers)
        return LoginOrCreateResponse.from_json(res.response.status_code, res.json)

    async def login_or_create_async(
        self,
        email: str,
        login_magic_link_url: Optional[str] = None,
        signup_magic_link_url: Optional[str] = None,
        login_expiration_minutes: Optional[int] = None,
        signup_expiration_minutes: Optional[int] = None,
        login_template_id: Optional[str] = None,
        signup_template_id: Optional[str] = None,
        attributes: Optional[Attributes] = None,
        create_user_as_pending: Optional[bool] = None,
        code_challenge: Optional[str] = None,
        locale: Optional[LoginOrCreateRequestLocale] = None,
    ) -> LoginOrCreateResponse:
        """Send either a login or signup Magic Link to the User based on if the email is associated with a User already. A new or pending User will receive a signup Magic Link. An active User will receive a login Magic Link. For more information on how to control the status your Users are created in see the `create_user_as_pending` flag.

        ### Next steps
        The User is emailed a Magic Link which redirects them to the provided [redirect URL](https://stytch.com/docs/guides/magic-links/email-magic-links/redirect-routing). Collect the `token` from the URL query parameters and call [Authenticate Magic Link](https://stytch.com/docs/api/authenticate-magic-link) to complete authentication.

        Fields:
          - email: The email address of the end user.
          - login_magic_link_url: The URL the end user clicks from the login Email Magic Link. This should be a URL that your app receives and parses and subsequently send an API request to authenticate the Magic Link and log in the User. If this value is not passed, the default login redirect URL that you set in your Dashboard is used. If you have not set a default login redirect URL, an error is returned.
          - signup_magic_link_url: The URL the end user clicks from the sign-up Email Magic Link. This should be a URL that your app receives and parses and subsequently send an API request to authenticate the Magic Link and sign-up the User. If this value is not passed, the default sign-up redirect URL that you set in your Dashboard is used. If you have not set a default sign-up redirect URL, an error is returned.
          - login_expiration_minutes: Set the expiration for the login email magic link, in minutes. By default, it expires in 1 hour. The minimum expiration is 5 minutes and the maximum is 7 days (10080 mins).
          - signup_expiration_minutes: Set the expiration for the sign-up email magic link, in minutes. By default, it expires in 1 week. The minimum expiration is 5 minutes and the maximum is 7 days (10080 mins).
          - login_template_id: Use a custom template for login emails. By default, it will use your default email template. The template must be a template using our built-in customizations or a custom HTML email for Magic links - Login.
          - signup_template_id: Use a custom template for sign-up emails. By default, it will use your default email template. The template must be a template using our built-in customizations or a custom HTML email for Magic links - Sign-up.
          - attributes: Provided attributes help with fraud detection.
          - create_user_as_pending: Flag for whether or not to save a user as pending vs active in Stytch. Defaults to false.
                If true, users will be saved with status pending in Stytch's backend until authenticated.
                If false, users will be created as active. An example usage of
                a true flag would be to require users to verify their phone by entering the OTP code before creating
                an account for them.
          - code_challenge: A base64url encoded SHA256 hash of a one time secret used to validate that the request starts and ends on the same device.
          - locale: Used to determine which language to use when sending the user this delivery method. Parameter is a [IETF BCP 47 language tag](https://www.w3.org/International/articles/language-tags/), e.g. `"en"`.

        Currently supported languages are English (`"en"`), Spanish (`"es"`), and Brazilian Portuguese (`"pt-br"`); if no value is provided, the copy defaults to English.

        Request support for additional languages [here](https://docs.google.com/forms/d/e/1FAIpQLScZSpAu_m2AmLXRT3F3kap-s_mcV6UTBitYn6CdyWP0-o7YjQ/viewform?usp=sf_link")!

        """  # noqa
        headers: Dict[str, str] = {}
        data: Dict[str, Any] = {
            "email": email,
        }
        if login_magic_link_url is not None:
            data["login_magic_link_url"] = login_magic_link_url
        if signup_magic_link_url is not None:
            data["signup_magic_link_url"] = signup_magic_link_url
        if login_expiration_minutes is not None:
            data["login_expiration_minutes"] = login_expiration_minutes
        if signup_expiration_minutes is not None:
            data["signup_expiration_minutes"] = signup_expiration_minutes
        if login_template_id is not None:
            data["login_template_id"] = login_template_id
        if signup_template_id is not None:
            data["signup_template_id"] = signup_template_id
        if attributes is not None:
            data["attributes"] = attributes.dict()
        if create_user_as_pending is not None:
            data["create_user_as_pending"] = create_user_as_pending
        if code_challenge is not None:
            data["code_challenge"] = code_challenge
        if locale is not None:
            data["locale"] = locale

        url = self.api_base.url_for("/v1/magic_links/email/login_or_create", data)
        res = await self.async_client.post(url, data, headers)
        return LoginOrCreateResponse.from_json(res.response.status, res.json)

    def invite(
        self,
        email: str,
        invite_template_id: Optional[str] = None,
        attributes: Optional[Attributes] = None,
        name: Optional[Name] = None,
        invite_magic_link_url: Optional[str] = None,
        invite_expiration_minutes: Optional[int] = None,
        locale: Optional[Union[InviteRequestLocale, str]] = None,
    ) -> InviteResponse:
        """Create a User and send an invite Magic Link to the provided `email`. The User will be created with a `pending` status until they click the Magic Link in the invite email.

        ### Next steps
        The User is emailed a Magic Link which redirects them to the provided [redirect URL](https://stytch.com/docs/guides/magic-links/email-magic-links/redirect-routing). Collect the `token` from the URL query parameters and call [Authenticate Magic Link](https://stytch.com/docs/api/authenticate-magic-link) to complete authentication.

        Fields:
          - email: The email address of the User to send the invite Magic Link to.
          - invite_template_id: Use a custom template for invite emails. By default, it will use your default email template. The template must be a template using our built-in customizations or a custom HTML email for Magic links - Invite.
          - attributes: Provided attributes help with fraud detection.
          - name: The name of the user. Each field in the name object is optional.
          - invite_magic_link_url: The URL the end user clicks from the Email Magic Link. This should be a URL that your app receives and parses and subsequently sends an API request to authenticate the Magic Link and log in the User. If this value is not passed, the default invite redirect URL that you set in your Dashboard is used. If you have not set a default sign-up redirect URL, an error is returned.
          - invite_expiration_minutes: Set the expiration for the email magic link, in minutes. By default, it expires in 1 hour. The minimum expiration is 5 minutes and the maximum is 7 days (10080 mins).
          - locale: Used to determine which language to use when sending the user this delivery method. Parameter is a [IETF BCP 47 language tag](https://www.w3.org/International/articles/language-tags/), e.g. `"en"`.

        Currently supported languages are English (`"en"`), Spanish (`"es"`), and Brazilian Portuguese (`"pt-br"`); if no value is provided, the copy defaults to English.

        Request support for additional languages [here](https://docs.google.com/forms/d/e/1FAIpQLScZSpAu_m2AmLXRT3F3kap-s_mcV6UTBitYn6CdyWP0-o7YjQ/viewform?usp=sf_link")!

        """  # noqa
        headers: Dict[str, str] = {}
        data: Dict[str, Any] = {
            "email": email,
        }
        if invite_template_id is not None:
            data["invite_template_id"] = invite_template_id
        if attributes is not None:
            data["attributes"] = attributes.dict()
        if name is not None:
            data["name"] = name.dict()
        if invite_magic_link_url is not None:
            data["invite_magic_link_url"] = invite_magic_link_url
        if invite_expiration_minutes is not None:
            data["invite_expiration_minutes"] = invite_expiration_minutes
        if locale is not None:
            data["locale"] = locale

        url = self.api_base.url_for("/v1/magic_links/email/invite", data)
        res = self.sync_client.post(url, data, headers)
        return InviteResponse.from_json(res.response.status_code, res.json)

    async def invite_async(
        self,
        email: str,
        invite_template_id: Optional[str] = None,
        attributes: Optional[Attributes] = None,
        name: Optional[Name] = None,
        invite_magic_link_url: Optional[str] = None,
        invite_expiration_minutes: Optional[int] = None,
        locale: Optional[InviteRequestLocale] = None,
    ) -> InviteResponse:
        """Create a User and send an invite Magic Link to the provided `email`. The User will be created with a `pending` status until they click the Magic Link in the invite email.

        ### Next steps
        The User is emailed a Magic Link which redirects them to the provided [redirect URL](https://stytch.com/docs/guides/magic-links/email-magic-links/redirect-routing). Collect the `token` from the URL query parameters and call [Authenticate Magic Link](https://stytch.com/docs/api/authenticate-magic-link) to complete authentication.

        Fields:
          - email: The email address of the User to send the invite Magic Link to.
          - invite_template_id: Use a custom template for invite emails. By default, it will use your default email template. The template must be a template using our built-in customizations or a custom HTML email for Magic links - Invite.
          - attributes: Provided attributes help with fraud detection.
          - name: The name of the user. Each field in the name object is optional.
          - invite_magic_link_url: The URL the end user clicks from the Email Magic Link. This should be a URL that your app receives and parses and subsequently sends an API request to authenticate the Magic Link and log in the User. If this value is not passed, the default invite redirect URL that you set in your Dashboard is used. If you have not set a default sign-up redirect URL, an error is returned.
          - invite_expiration_minutes: Set the expiration for the email magic link, in minutes. By default, it expires in 1 hour. The minimum expiration is 5 minutes and the maximum is 7 days (10080 mins).
          - locale: Used to determine which language to use when sending the user this delivery method. Parameter is a [IETF BCP 47 language tag](https://www.w3.org/International/articles/language-tags/), e.g. `"en"`.

        Currently supported languages are English (`"en"`), Spanish (`"es"`), and Brazilian Portuguese (`"pt-br"`); if no value is provided, the copy defaults to English.

        Request support for additional languages [here](https://docs.google.com/forms/d/e/1FAIpQLScZSpAu_m2AmLXRT3F3kap-s_mcV6UTBitYn6CdyWP0-o7YjQ/viewform?usp=sf_link")!

        """  # noqa
        headers: Dict[str, str] = {}
        data: Dict[str, Any] = {
            "email": email,
        }
        if invite_template_id is not None:
            data["invite_template_id"] = invite_template_id
        if attributes is not None:
            data["attributes"] = attributes.dict()
        if name is not None:
            data["name"] = name.dict()
        if invite_magic_link_url is not None:
            data["invite_magic_link_url"] = invite_magic_link_url
        if invite_expiration_minutes is not None:
            data["invite_expiration_minutes"] = invite_expiration_minutes
        if locale is not None:
            data["locale"] = locale

        url = self.api_base.url_for("/v1/magic_links/email/invite", data)
        res = await self.async_client.post(url, data, headers)
        return InviteResponse.from_json(res.response.status, res.json)

    def revoke_invite(
        self,
        email: str,
    ) -> RevokeInviteResponse:
        """Revoke a pending invite based on the `email` provided.

        Fields:
          - email: The email of the user.
        """  # noqa
        headers: Dict[str, str] = {}
        data: Dict[str, Any] = {
            "email": email,
        }

        url = self.api_base.url_for("/v1/magic_links/email/revoke_invite", data)
        res = self.sync_client.post(url, data, headers)
        return RevokeInviteResponse.from_json(res.response.status_code, res.json)

    async def revoke_invite_async(
        self,
        email: str,
    ) -> RevokeInviteResponse:
        """Revoke a pending invite based on the `email` provided.

        Fields:
          - email: The email of the user.
        """  # noqa
        headers: Dict[str, str] = {}
        data: Dict[str, Any] = {
            "email": email,
        }

        url = self.api_base.url_for("/v1/magic_links/email/revoke_invite", data)
        res = await self.async_client.post(url, data, headers)
        return RevokeInviteResponse.from_json(res.response.status, res.json)
