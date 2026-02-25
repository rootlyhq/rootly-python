from typing import Literal, cast

NewCatalogDataAttributesIcon = Literal[
    "chart-bar", "cursor-arrow-ripple", "globe-alt", "light-bulb", "server-stack", "shapes", "user-group", "users"
]

NEW_CATALOG_DATA_ATTRIBUTES_ICON_VALUES: set[NewCatalogDataAttributesIcon] = {
    "chart-bar",
    "cursor-arrow-ripple",
    "globe-alt",
    "light-bulb",
    "server-stack",
    "shapes",
    "user-group",
    "users",
}


def check_new_catalog_data_attributes_icon(value: str | None) -> NewCatalogDataAttributesIcon | None:
    if value is None:
        return None
    if value in NEW_CATALOG_DATA_ATTRIBUTES_ICON_VALUES:
        return cast(NewCatalogDataAttributesIcon, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {NEW_CATALOG_DATA_ATTRIBUTES_ICON_VALUES!r}")
