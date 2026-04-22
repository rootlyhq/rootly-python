from typing import Literal, cast

UpdateCatalogPropertyDataAttributesKind = Literal[
    "boolean", "cause", "environment", "functionality", "group", "incident_type", "reference", "service", "text", "user"
]

UPDATE_CATALOG_PROPERTY_DATA_ATTRIBUTES_KIND_VALUES: set[UpdateCatalogPropertyDataAttributesKind] = {
    "boolean",
    "cause",
    "environment",
    "functionality",
    "group",
    "incident_type",
    "reference",
    "service",
    "text",
    "user",
}


def check_update_catalog_property_data_attributes_kind(
    value: str | None,
) -> UpdateCatalogPropertyDataAttributesKind | None:
    if value is None:
        return None
    if value in UPDATE_CATALOG_PROPERTY_DATA_ATTRIBUTES_KIND_VALUES:
        return cast(UpdateCatalogPropertyDataAttributesKind, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_CATALOG_PROPERTY_DATA_ATTRIBUTES_KIND_VALUES!r}"
    )
