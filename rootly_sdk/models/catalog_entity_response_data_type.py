from typing import Literal, cast

CatalogEntityResponseDataType = Literal["catalog_entities"]

CATALOG_ENTITY_RESPONSE_DATA_TYPE_VALUES: set[CatalogEntityResponseDataType] = {
    "catalog_entities",
}


def check_catalog_entity_response_data_type(value: str | None) -> CatalogEntityResponseDataType | None:
    if value is None:
        return None
    if value in CATALOG_ENTITY_RESPONSE_DATA_TYPE_VALUES:
        return cast(CatalogEntityResponseDataType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CATALOG_ENTITY_RESPONSE_DATA_TYPE_VALUES!r}")
