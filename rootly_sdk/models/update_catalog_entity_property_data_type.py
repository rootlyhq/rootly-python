from typing import Literal, cast

UpdateCatalogEntityPropertyDataType = Literal["catalog_entity_properties"]

UPDATE_CATALOG_ENTITY_PROPERTY_DATA_TYPE_VALUES: set[UpdateCatalogEntityPropertyDataType] = {
    "catalog_entity_properties",
}


def check_update_catalog_entity_property_data_type(value: str | None) -> UpdateCatalogEntityPropertyDataType | None:
    if value is None:
        return None
    if value in UPDATE_CATALOG_ENTITY_PROPERTY_DATA_TYPE_VALUES:
        return cast(UpdateCatalogEntityPropertyDataType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {UPDATE_CATALOG_ENTITY_PROPERTY_DATA_TYPE_VALUES!r}")
