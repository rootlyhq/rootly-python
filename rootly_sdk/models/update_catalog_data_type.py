from typing import Literal, cast

UpdateCatalogDataType = Literal["catalogs"]

UPDATE_CATALOG_DATA_TYPE_VALUES: set[UpdateCatalogDataType] = {
    "catalogs",
}


def check_update_catalog_data_type(value: str | None) -> UpdateCatalogDataType | None:
    if value is None:
        return None
    if value in UPDATE_CATALOG_DATA_TYPE_VALUES:
        return cast(UpdateCatalogDataType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {UPDATE_CATALOG_DATA_TYPE_VALUES!r}")
