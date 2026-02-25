from typing import Literal, cast

NewRetrospectiveProcessGroupDataType = Literal["retrospective_process_groups"]

NEW_RETROSPECTIVE_PROCESS_GROUP_DATA_TYPE_VALUES: set[NewRetrospectiveProcessGroupDataType] = {
    "retrospective_process_groups",
}


def check_new_retrospective_process_group_data_type(value: str | None) -> NewRetrospectiveProcessGroupDataType | None:
    if value is None:
        return None
    if value in NEW_RETROSPECTIVE_PROCESS_GROUP_DATA_TYPE_VALUES:
        return cast(NewRetrospectiveProcessGroupDataType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {NEW_RETROSPECTIVE_PROCESS_GROUP_DATA_TYPE_VALUES!r}")
