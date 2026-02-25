from typing import Literal, cast

WebhooksEndpointResponseDataType = Literal["webhooks_endpoints"]

WEBHOOKS_ENDPOINT_RESPONSE_DATA_TYPE_VALUES: set[WebhooksEndpointResponseDataType] = {
    "webhooks_endpoints",
}


def check_webhooks_endpoint_response_data_type(value: str | None) -> WebhooksEndpointResponseDataType | None:
    if value is None:
        return None
    if value in WEBHOOKS_ENDPOINT_RESPONSE_DATA_TYPE_VALUES:
        return cast(WebhooksEndpointResponseDataType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {WEBHOOKS_ENDPOINT_RESPONSE_DATA_TYPE_VALUES!r}")
