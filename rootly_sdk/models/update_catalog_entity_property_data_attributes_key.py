from enum import Enum


class UpdateCatalogEntityPropertyDataAttributesKey(str, Enum):
    CATALOG_ENTITY = "catalog_entity"
    TEXT = "text"

    def __str__(self) -> str:
        return str(self.value)
