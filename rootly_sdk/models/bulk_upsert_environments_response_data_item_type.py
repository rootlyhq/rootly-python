from typing import Literal

BulkUpsertEnvironmentsResponseDataItemType = Literal["environments"]

BULK_UPSERT_ENVIRONMENTS_RESPONSE_DATA_ITEM_TYPE_VALUES: set[BulkUpsertEnvironmentsResponseDataItemType] = {
    "environments",
}


def check_bulk_upsert_environments_response_data_item_type(
    value: str | None,
) -> BulkUpsertEnvironmentsResponseDataItemType | None:
    if value is None:
        return None
    if value in BULK_UPSERT_ENVIRONMENTS_RESPONSE_DATA_ITEM_TYPE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {BULK_UPSERT_ENVIRONMENTS_RESPONSE_DATA_ITEM_TYPE_VALUES!r}"
    )
