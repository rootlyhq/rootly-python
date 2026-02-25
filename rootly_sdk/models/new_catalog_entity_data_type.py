from typing import Literal, cast

NewCatalogEntityDataType = Literal["catalog_entities"]

NEW_CATALOG_ENTITY_DATA_TYPE_VALUES: set[NewCatalogEntityDataType] = {
    "catalog_entities",
}


def check_new_catalog_entity_data_type(value: str | None) -> NewCatalogEntityDataType | None:
    if value is None:
        return None
    if value in NEW_CATALOG_ENTITY_DATA_TYPE_VALUES:
        return cast(NewCatalogEntityDataType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {NEW_CATALOG_ENTITY_DATA_TYPE_VALUES!r}")
