from typing import Literal, cast

NewCatalogFieldDataAttributesCatalogType = Literal[
    "catalog", "cause", "environment", "functionality", "incident_type", "service", "team"
]

NEW_CATALOG_FIELD_DATA_ATTRIBUTES_CATALOG_TYPE_VALUES: set[NewCatalogFieldDataAttributesCatalogType] = {
    "catalog",
    "cause",
    "environment",
    "functionality",
    "incident_type",
    "service",
    "team",
}


def check_new_catalog_field_data_attributes_catalog_type(value: str | None) -> NewCatalogFieldDataAttributesCatalogType | None:
    if value is None:
        return None
    if value in NEW_CATALOG_FIELD_DATA_ATTRIBUTES_CATALOG_TYPE_VALUES:
        return cast(NewCatalogFieldDataAttributesCatalogType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {NEW_CATALOG_FIELD_DATA_ATTRIBUTES_CATALOG_TYPE_VALUES!r}"
    )
