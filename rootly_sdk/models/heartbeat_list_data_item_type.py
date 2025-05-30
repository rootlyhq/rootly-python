from enum import Enum


class HeartbeatListDataItemType(str, Enum):
    HEARTBEATS = "heartbeats"

    def __str__(self) -> str:
        return str(self.value)
