from typing import Literal

BulkUpsertTeamsResponseDataItemType = Literal["groups"]

BULK_UPSERT_TEAMS_RESPONSE_DATA_ITEM_TYPE_VALUES: set[BulkUpsertTeamsResponseDataItemType] = {
    "groups",
}


def check_bulk_upsert_teams_response_data_item_type(value: str | None) -> BulkUpsertTeamsResponseDataItemType | None:
    if value is None:
        return None
    if value in BULK_UPSERT_TEAMS_RESPONSE_DATA_ITEM_TYPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {BULK_UPSERT_TEAMS_RESPONSE_DATA_ITEM_TYPE_VALUES!r}")
