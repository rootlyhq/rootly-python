from enum import Enum


class UpdateRetrospectiveProcessGroupDataType(str, Enum):
    RETROSPECTIVE_PROCESS_GROUPS = "retrospective_process_groups"

    def __str__(self) -> str:
        return str(self.value)
