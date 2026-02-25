from typing import Literal, cast

UpdateCatalogEntityPropertyDataAttributesKey = Literal["catalog_entity", "text"]

UPDATE_CATALOG_ENTITY_PROPERTY_DATA_ATTRIBUTES_KEY_VALUES: set[UpdateCatalogEntityPropertyDataAttributesKey] = {
    "catalog_entity",
    "text",
}


def check_update_catalog_entity_property_data_attributes_key(
    value: str | None,
) -> UpdateCatalogEntityPropertyDataAttributesKey | None:
    if value is None:
        return None
    if value in UPDATE_CATALOG_ENTITY_PROPERTY_DATA_ATTRIBUTES_KEY_VALUES:
        return cast(UpdateCatalogEntityPropertyDataAttributesKey, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_CATALOG_ENTITY_PROPERTY_DATA_ATTRIBUTES_KEY_VALUES!r}"
    )
