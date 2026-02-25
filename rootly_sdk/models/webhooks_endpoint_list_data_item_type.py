from typing import Literal, cast

WebhooksEndpointListDataItemType = Literal["webhooks_endpoints"]

WEBHOOKS_ENDPOINT_LIST_DATA_ITEM_TYPE_VALUES: set[WebhooksEndpointListDataItemType] = {
    "webhooks_endpoints",
}


def check_webhooks_endpoint_list_data_item_type(value: str | None) -> WebhooksEndpointListDataItemType | None:
    if value is None:
        return None
    if value in WEBHOOKS_ENDPOINT_LIST_DATA_ITEM_TYPE_VALUES:
        return cast(WebhooksEndpointListDataItemType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {WEBHOOKS_ENDPOINT_LIST_DATA_ITEM_TYPE_VALUES!r}")
