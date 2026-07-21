from typing import Literal, cast

BulkUpsertFunctionalitiesResponseDataItemType = Literal["functionalities"]

BULK_UPSERT_FUNCTIONALITIES_RESPONSE_DATA_ITEM_TYPE_VALUES: set[BulkUpsertFunctionalitiesResponseDataItemType] = {
    "functionalities",
}


def check_bulk_upsert_functionalities_response_data_item_type(
    value: str | None,
) -> BulkUpsertFunctionalitiesResponseDataItemType | None:
    if value is None:
        return None
    if value in BULK_UPSERT_FUNCTIONALITIES_RESPONSE_DATA_ITEM_TYPE_VALUES:
        return cast(BulkUpsertFunctionalitiesResponseDataItemType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {BULK_UPSERT_FUNCTIONALITIES_RESPONSE_DATA_ITEM_TYPE_VALUES!r}"
    )
