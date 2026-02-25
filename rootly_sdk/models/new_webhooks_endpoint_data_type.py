from typing import Literal, cast

NewWebhooksEndpointDataType = Literal["webhooks_endpoints"]

NEW_WEBHOOKS_ENDPOINT_DATA_TYPE_VALUES: set[NewWebhooksEndpointDataType] = {
    "webhooks_endpoints",
}


def check_new_webhooks_endpoint_data_type(value: str | None) -> NewWebhooksEndpointDataType | None:
    if value is None:
        return None
    if value in NEW_WEBHOOKS_ENDPOINT_DATA_TYPE_VALUES:
        return cast(NewWebhooksEndpointDataType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {NEW_WEBHOOKS_ENDPOINT_DATA_TYPE_VALUES!r}")
