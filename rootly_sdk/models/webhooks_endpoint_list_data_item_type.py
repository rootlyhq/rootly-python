from enum import Enum


class WebhooksEndpointListDataItemType(str, Enum):
    WEBHOOKS_ENDPOINTS = "webhooks_endpoints"

    def __str__(self) -> str:
        return str(self.value)
