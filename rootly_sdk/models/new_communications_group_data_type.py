from typing import Literal, cast

NewCommunicationsGroupDataType = Literal["communications_groups"]

NEW_COMMUNICATIONS_GROUP_DATA_TYPE_VALUES: set[NewCommunicationsGroupDataType] = {
    "communications_groups",
}


def check_new_communications_group_data_type(value: str | None) -> NewCommunicationsGroupDataType | None:
    if value is None:
        return None
    if value in NEW_COMMUNICATIONS_GROUP_DATA_TYPE_VALUES:
        return cast(NewCommunicationsGroupDataType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {NEW_COMMUNICATIONS_GROUP_DATA_TYPE_VALUES!r}")
