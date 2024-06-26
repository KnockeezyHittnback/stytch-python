# !!!
# WARNING: This file is autogenerated
# Only modify code within MANUAL() sections
# or your changes may be overwritten later!
# !!!

from __future__ import annotations

from typing import Any, Dict

from stytch.consumer.models.project import MetricsResponse
from stytch.core.api_base import ApiBase
from stytch.core.http.client import AsyncClient, SyncClient


class Project:
    def __init__(
        self, api_base: ApiBase, sync_client: SyncClient, async_client: AsyncClient
    ) -> None:
        self.api_base = api_base
        self.sync_client = sync_client
        self.async_client = async_client

    def metrics(
        self,
    ) -> MetricsResponse:
        headers: Dict[str, str] = {}
        data: Dict[str, Any] = {}

        url = self.api_base.url_for("/v1/projects/metrics", data)
        res = self.sync_client.get(url, data, headers)
        return MetricsResponse.from_json(res.response.status_code, res.json)

    async def metrics_async(
        self,
    ) -> MetricsResponse:
        headers: Dict[str, str] = {}
        data: Dict[str, Any] = {}

        url = self.api_base.url_for("/v1/projects/metrics", data)
        res = await self.async_client.get(url, data, headers)
        return MetricsResponse.from_json(res.response.status, res.json)
