from typing import Literal, cast

CatalogEntityPropertyKey = Literal["catalog_entity", "text"]

CATALOG_ENTITY_PROPERTY_KEY_VALUES: set[CatalogEntityPropertyKey] = {
    "catalog_entity",
    "text",
}


def check_catalog_entity_property_key(value: str | None) -> CatalogEntityPropertyKey | None:
    if value is None:
        return None
    if value in CATALOG_ENTITY_PROPERTY_KEY_VALUES:
        return cast(CatalogEntityPropertyKey, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CATALOG_ENTITY_PROPERTY_KEY_VALUES!r}")
