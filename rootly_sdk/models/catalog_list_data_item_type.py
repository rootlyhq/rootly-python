from enum import Enum


class CatalogListDataItemType(str, Enum):
    CATALOGS = "catalogs"

    def __str__(self) -> str:
        return str(self.value)
