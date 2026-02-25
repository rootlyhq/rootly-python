from typing import Literal, cast

NewCatalogEntityPropertyDataType = Literal["catalog_entity_properties"]

NEW_CATALOG_ENTITY_PROPERTY_DATA_TYPE_VALUES: set[NewCatalogEntityPropertyDataType] = {
    "catalog_entity_properties",
}


def check_new_catalog_entity_property_data_type(value: str | None) -> NewCatalogEntityPropertyDataType | None:
    if value is None:
        return None
    if value in NEW_CATALOG_ENTITY_PROPERTY_DATA_TYPE_VALUES:
        return cast(NewCatalogEntityPropertyDataType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {NEW_CATALOG_ENTITY_PROPERTY_DATA_TYPE_VALUES!r}")
