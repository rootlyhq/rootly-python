from typing import Literal, cast

NewCatalogPropertyDataType = Literal["catalog_properties"]

NEW_CATALOG_PROPERTY_DATA_TYPE_VALUES: set[NewCatalogPropertyDataType] = {
    "catalog_properties",
}


def check_new_catalog_property_data_type(value: str | None) -> NewCatalogPropertyDataType | None:
    if value is None:
        return None
    if value in NEW_CATALOG_PROPERTY_DATA_TYPE_VALUES:
        return cast(NewCatalogPropertyDataType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {NEW_CATALOG_PROPERTY_DATA_TYPE_VALUES!r}")
