from typing import Literal, cast

UpdateCatalogPropertyDataAttributesCatalogType = Literal[
    "catalog", "cause", "environment", "functionality", "incident_type", "service", "team"
]

UPDATE_CATALOG_PROPERTY_DATA_ATTRIBUTES_CATALOG_TYPE_VALUES: set[UpdateCatalogPropertyDataAttributesCatalogType] = {
    "catalog",
    "cause",
    "environment",
    "functionality",
    "incident_type",
    "service",
    "team",
}


def check_update_catalog_property_data_attributes_catalog_type(
    value: str | None,
) -> UpdateCatalogPropertyDataAttributesCatalogType | None:
    if value is None:
        return None
    if value in UPDATE_CATALOG_PROPERTY_DATA_ATTRIBUTES_CATALOG_TYPE_VALUES:
        return cast(UpdateCatalogPropertyDataAttributesCatalogType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_CATALOG_PROPERTY_DATA_ATTRIBUTES_CATALOG_TYPE_VALUES!r}"
    )
