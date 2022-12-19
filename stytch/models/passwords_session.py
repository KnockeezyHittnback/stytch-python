#!/usr/bin/env python3

from typing import Optional

from stytch.core.models import ResponseBase, StytchSession


class ResetResponse(ResponseBase):
    user_id: str
    session: Optional[StytchSession]