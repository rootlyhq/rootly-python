from typing import Literal, cast

WebhooksDeliveryResponseDataType = Literal["webhooks_deliveries"]

WEBHOOKS_DELIVERY_RESPONSE_DATA_TYPE_VALUES: set[WebhooksDeliveryResponseDataType] = {
    "webhooks_deliveries",
}


def check_webhooks_delivery_response_data_type(value: str | None) -> WebhooksDeliveryResponseDataType | None:
    if value is None:
        return None
    if value in WEBHOOKS_DELIVERY_RESPONSE_DATA_TYPE_VALUES:
        return cast(WebhooksDeliveryResponseDataType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {WEBHOOKS_DELIVERY_RESPONSE_DATA_TYPE_VALUES!r}")
