from typing import Literal

BulkUpsertServicesResponseDataItemType = Literal["services"]

BULK_UPSERT_SERVICES_RESPONSE_DATA_ITEM_TYPE_VALUES: set[BulkUpsertServicesResponseDataItemType] = {
    "services",
}


def check_bulk_upsert_services_response_data_item_type(
    value: str | None,
) -> BulkUpsertServicesResponseDataItemType | None:
    if value is None:
        return None
    if value in BULK_UPSERT_SERVICES_RESPONSE_DATA_ITEM_TYPE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {BULK_UPSERT_SERVICES_RESPONSE_DATA_ITEM_TYPE_VALUES!r}"
    )
