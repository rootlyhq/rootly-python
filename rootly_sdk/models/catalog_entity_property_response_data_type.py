from typing import Literal, cast

CatalogEntityPropertyResponseDataType = Literal["catalog_entity_properties"]

CATALOG_ENTITY_PROPERTY_RESPONSE_DATA_TYPE_VALUES: set[CatalogEntityPropertyResponseDataType] = {
    "catalog_entity_properties",
}


def check_catalog_entity_property_response_data_type(value: str | None) -> CatalogEntityPropertyResponseDataType | None:
    if value is None:
        return None
    if value in CATALOG_ENTITY_PROPERTY_RESPONSE_DATA_TYPE_VALUES:
        return cast(CatalogEntityPropertyResponseDataType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CATALOG_ENTITY_PROPERTY_RESPONSE_DATA_TYPE_VALUES!r}"
    )
