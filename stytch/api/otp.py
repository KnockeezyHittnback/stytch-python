from typing import Dict, Optional

from .base import _validate_attributes, Base

class OTP(Base):
    def __init__(self, client):
        super().__init__(client)
        self.sms = SMS(client)

    @property
    def otp_url(self):
        return self.get_url("otps")

    def authenticate(
        self,
        method_id: str,
        code: str,
        attributes: Optional[Dict] = None,
        options: Optional[Dict] = None
    ):
        attributes = _validate_attributes(attributes)
        options = self._validate_options(options)
        data = {
            "method_id": method_id,
            "code": code,
        }
        if attributes:
            data["attributes"] = attributes
        if options:
            data["options"] = options

        return self._post(
            "{0}/authenticate".format(
                self.otp_url,
            ),
            data=data,
        )

class SMS(Base):
    @property
    def otp_url(self):
        return self.get_url("otps")

    def send(
        self,
        phone_number: str,
        expiration_minutes: Optional[int] = None,
        attributes: Optional[Dict] = None,
    ):
        attributes = _validate_attributes(attributes)
        data = {
            "phone_number": phone_number,
        }
        if expiration_minutes:
            data["expiration_minutes"] = expiration_minutes
        if attributes:
            data["attributes"] = attributes

        return self._post(
            "{0}/sms/send".format(
                self.otp_url,
            ),
            data=data,
        )

    def login_or_create(
        self,
        phone_number: str,
        expiration_minutes: Optional[int] = None,
        attributes: Optional[Dict] = None,
        create_user_as_pending: Optional[bool] = False
    ):
        attributes = _validate_attributes(attributes)
        data = {
            "phone_number": phone_number,
            "create_user_as_pending": create_user_as_pending,
        }
        if expiration_minutes:
            data["expiration_minutes"] = expiration_minutes
        if attributes:
            data["attributes"] = attributes

        return self._post(
            "{0}/sms/login_or_create".format(
                self.otp_url,
            ),
            data=data,
        )