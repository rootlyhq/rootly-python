from typing import Literal, cast

UpdateRetrospectiveProcessGroupDataType = Literal["retrospective_process_groups"]

UPDATE_RETROSPECTIVE_PROCESS_GROUP_DATA_TYPE_VALUES: set[UpdateRetrospectiveProcessGroupDataType] = {
    "retrospective_process_groups",
}


def check_update_retrospective_process_group_data_type(
    value: str | None,
) -> UpdateRetrospectiveProcessGroupDataType | None:
    if value is None:
        return None
    if value in UPDATE_RETROSPECTIVE_PROCESS_GROUP_DATA_TYPE_VALUES:
        return cast(UpdateRetrospectiveProcessGroupDataType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_RETROSPECTIVE_PROCESS_GROUP_DATA_TYPE_VALUES!r}"
    )
