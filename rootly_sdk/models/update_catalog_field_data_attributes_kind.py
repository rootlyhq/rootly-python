from typing import Literal, cast

UpdateCatalogFieldDataAttributesKind = Literal[
    "boolean", "cause", "environment", "functionality", "group", "incident_type", "reference", "service", "text", "user"
]

UPDATE_CATALOG_FIELD_DATA_ATTRIBUTES_KIND_VALUES: set[UpdateCatalogFieldDataAttributesKind] = {
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


def check_update_catalog_field_data_attributes_kind(value: str | None) -> UpdateCatalogFieldDataAttributesKind | None:
    if value is None:
        return None
    if value in UPDATE_CATALOG_FIELD_DATA_ATTRIBUTES_KIND_VALUES:
        return cast(UpdateCatalogFieldDataAttributesKind, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {UPDATE_CATALOG_FIELD_DATA_ATTRIBUTES_KIND_VALUES!r}")
