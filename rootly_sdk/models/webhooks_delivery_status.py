from typing import Literal

WebhooksDeliveryStatus = Literal["failed", "pending", "success"]

WEBHOOKS_DELIVERY_STATUS_VALUES: set[WebhooksDeliveryStatus] = {
    "failed",
    "pending",
    "success",
}


def check_webhooks_delivery_status(value: str | None) -> WebhooksDeliveryStatus | None:
    if value is None:
        return None
    if value in WEBHOOKS_DELIVERY_STATUS_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {WEBHOOKS_DELIVERY_STATUS_VALUES!r}")
