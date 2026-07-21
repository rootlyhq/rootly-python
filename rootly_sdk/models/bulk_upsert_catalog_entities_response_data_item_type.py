from typing import Literal, cast

BulkUpsertCatalogEntitiesResponseDataItemType = Literal["catalog_entities"]

BULK_UPSERT_CATALOG_ENTITIES_RESPONSE_DATA_ITEM_TYPE_VALUES: set[BulkUpsertCatalogEntitiesResponseDataItemType] = {
    "catalog_entities",
}


def check_bulk_upsert_catalog_entities_response_data_item_type(
    value: str | None,
) -> BulkUpsertCatalogEntitiesResponseDataItemType | None:
    if value is None:
        return None
    if value in BULK_UPSERT_CATALOG_ENTITIES_RESPONSE_DATA_ITEM_TYPE_VALUES:
        return cast(BulkUpsertCatalogEntitiesResponseDataItemType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {BULK_UPSERT_CATALOG_ENTITIES_RESPONSE_DATA_ITEM_TYPE_VALUES!r}"
    )
