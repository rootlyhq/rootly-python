from enum import Enum


class NewStatusPageDataType(str, Enum):
    STATUS_PAGES = "status_pages"

    def __str__(self) -> str:
        return str(self.value)
