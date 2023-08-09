# !!!
# WARNING: This file is autogenerated
# Only modify code within MANUAL() sections
# or your changes may be overwritten later!
# !!!

from __future__ import annotations

import enum
from typing import List

from stytch.consumer.models.m2m import (
    M2MClient,
    M2MClientWithClientSecret,
    ResultsMetadata,
)
from stytch.core.response_base import ResponseBase


class UpdateRequestStatus(enum.Enum):
    ACTIVE = "active"
    INACTIVE = "inactive"


class CreateResponse(ResponseBase):
    """Response type for `Clients.create`.
    Fields:
      - m2m_client: The M2M Client created by this API call.
    """  # noqa

    m2m_client: M2MClientWithClientSecret


class DeleteResponse(ResponseBase):
    """Response type for `Clients.delete`.
    Fields:
      - client_id: The ID of the client.
    """  # noqa

    client_id: str


class GetResponse(ResponseBase):
    """Response type for `Clients.get`.
    Fields:
      - m2m_client: The M2M Client affected by this operation.
    """  # noqa

    m2m_client: M2MClient


class SearchResponse(ResponseBase):
    """Response type for `Clients.search`.
    Fields:
      - m2m_clients: An array of M2M Clients that match your search query.
      - results_metadata: The search `results_metadata` object contains metadata relevant to your specific query like total and `next_cursor`.
    """  # noqa

    m2m_clients: List[M2MClient]
    results_metadata: ResultsMetadata


class UpdateResponse(ResponseBase):
    """Response type for `Clients.update`.
    Fields:
      - m2m_client: The M2M Client affected by this operation.
    """  # noqa

    m2m_client: M2MClient
