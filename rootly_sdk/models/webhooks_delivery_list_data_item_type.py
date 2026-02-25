from typing import Literal, cast

WebhooksDeliveryListDataItemType = Literal["webhooks_deliveries"]

WEBHOOKS_DELIVERY_LIST_DATA_ITEM_TYPE_VALUES: set[WebhooksDeliveryListDataItemType] = {
    "webhooks_deliveries",
}


def check_webhooks_delivery_list_data_item_type(value: str | None) -> WebhooksDeliveryListDataItemType | None:
    if value is None:
        return None
    if value in WEBHOOKS_DELIVERY_LIST_DATA_ITEM_TYPE_VALUES:
        return cast(WebhooksDeliveryListDataItemType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {WEBHOOKS_DELIVERY_LIST_DATA_ITEM_TYPE_VALUES!r}")
