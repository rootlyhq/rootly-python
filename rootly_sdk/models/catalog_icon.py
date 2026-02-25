from typing import Literal, cast

CatalogIcon = Literal[
    "chart-bar", "cursor-arrow-ripple", "globe-alt", "light-bulb", "server-stack", "shapes", "user-group", "users"
]

CATALOG_ICON_VALUES: set[CatalogIcon] = {
    "chart-bar",
    "cursor-arrow-ripple",
    "globe-alt",
    "light-bulb",
    "server-stack",
    "shapes",
    "user-group",
    "users",
}


def check_catalog_icon(value: str | None) -> CatalogIcon | None:
    if value is None:
        return None
    if value in CATALOG_ICON_VALUES:
        return cast(CatalogIcon, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CATALOG_ICON_VALUES!r}")
