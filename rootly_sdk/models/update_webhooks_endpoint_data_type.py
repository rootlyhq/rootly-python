from typing import Literal, cast

UpdateWebhooksEndpointDataType = Literal["webhooks_endpoints"]

UPDATE_WEBHOOKS_ENDPOINT_DATA_TYPE_VALUES: set[UpdateWebhooksEndpointDataType] = {
    "webhooks_endpoints",
}


def check_update_webhooks_endpoint_data_type(value: str | None) -> UpdateWebhooksEndpointDataType | None:
    if value is None:
        return None
    if value in UPDATE_WEBHOOKS_ENDPOINT_DATA_TYPE_VALUES:
        return cast(UpdateWebhooksEndpointDataType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {UPDATE_WEBHOOKS_ENDPOINT_DATA_TYPE_VALUES!r}")
