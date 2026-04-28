from typing import Literal, cast

NewCatalogEntityPropertyDataAttributesKey = Literal["catalog_entity", "slack", "text"]

NEW_CATALOG_ENTITY_PROPERTY_DATA_ATTRIBUTES_KEY_VALUES: set[NewCatalogEntityPropertyDataAttributesKey] = {
    "catalog_entity",
    "slack",
    "text",
}


def check_new_catalog_entity_property_data_attributes_key(
    value: str | None,
) -> NewCatalogEntityPropertyDataAttributesKey | None:
    if value is None:
        return None
    if value in NEW_CATALOG_ENTITY_PROPERTY_DATA_ATTRIBUTES_KEY_VALUES:
        return cast(NewCatalogEntityPropertyDataAttributesKey, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {NEW_CATALOG_ENTITY_PROPERTY_DATA_ATTRIBUTES_KEY_VALUES!r}"
    )
