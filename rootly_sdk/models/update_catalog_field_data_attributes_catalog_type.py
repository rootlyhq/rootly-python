from typing import Literal, cast

UpdateCatalogFieldDataAttributesCatalogType = Literal[
    "catalog", "cause", "environment", "functionality", "incident_type", "service", "team"
]

UPDATE_CATALOG_FIELD_DATA_ATTRIBUTES_CATALOG_TYPE_VALUES: set[UpdateCatalogFieldDataAttributesCatalogType] = {
    "catalog",
    "cause",
    "environment",
    "functionality",
    "incident_type",
    "service",
    "team",
}


def check_update_catalog_field_data_attributes_catalog_type(value: str | None) -> UpdateCatalogFieldDataAttributesCatalogType | None:
    if value is None:
        return None
    if value in UPDATE_CATALOG_FIELD_DATA_ATTRIBUTES_CATALOG_TYPE_VALUES:
        return cast(UpdateCatalogFieldDataAttributesCatalogType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_CATALOG_FIELD_DATA_ATTRIBUTES_CATALOG_TYPE_VALUES!r}"
    )
