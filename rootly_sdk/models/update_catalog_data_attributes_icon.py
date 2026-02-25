from typing import Literal, cast

UpdateCatalogDataAttributesIcon = Literal[
    "chart-bar", "cursor-arrow-ripple", "globe-alt", "light-bulb", "server-stack", "shapes", "user-group", "users"
]

UPDATE_CATALOG_DATA_ATTRIBUTES_ICON_VALUES: set[UpdateCatalogDataAttributesIcon] = {
    "chart-bar",
    "cursor-arrow-ripple",
    "globe-alt",
    "light-bulb",
    "server-stack",
    "shapes",
    "user-group",
    "users",
}


def check_update_catalog_data_attributes_icon(value: str | None) -> UpdateCatalogDataAttributesIcon | None:
    if value is None:
        return None
    if value in UPDATE_CATALOG_DATA_ATTRIBUTES_ICON_VALUES:
        return cast(UpdateCatalogDataAttributesIcon, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {UPDATE_CATALOG_DATA_ATTRIBUTES_ICON_VALUES!r}")
