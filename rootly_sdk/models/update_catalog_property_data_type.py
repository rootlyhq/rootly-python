from typing import Literal, cast

UpdateCatalogPropertyDataType = Literal["catalog_properties"]

UPDATE_CATALOG_PROPERTY_DATA_TYPE_VALUES: set[UpdateCatalogPropertyDataType] = {
    "catalog_properties",
}


def check_update_catalog_property_data_type(value: str | None) -> UpdateCatalogPropertyDataType | None:
    if value is None:
        return None
    if value in UPDATE_CATALOG_PROPERTY_DATA_TYPE_VALUES:
        return cast(UpdateCatalogPropertyDataType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {UPDATE_CATALOG_PROPERTY_DATA_TYPE_VALUES!r}")
