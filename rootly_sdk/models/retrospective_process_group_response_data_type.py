from typing import Literal

RetrospectiveProcessGroupResponseDataType = Literal["retrospective_process_groups"]

RETROSPECTIVE_PROCESS_GROUP_RESPONSE_DATA_TYPE_VALUES: set[RetrospectiveProcessGroupResponseDataType] = {
    "retrospective_process_groups",
}


def check_retrospective_process_group_response_data_type(
    value: str | None,
) -> RetrospectiveProcessGroupResponseDataType | None:
    if value is None:
        return None
    if value in RETROSPECTIVE_PROCESS_GROUP_RESPONSE_DATA_TYPE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {RETROSPECTIVE_PROCESS_GROUP_RESPONSE_DATA_TYPE_VALUES!r}"
    )
