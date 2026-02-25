from typing import Literal, cast

NewRetrospectiveProcessDataType = Literal["retrospective_processes"]

NEW_RETROSPECTIVE_PROCESS_DATA_TYPE_VALUES: set[NewRetrospectiveProcessDataType] = {
    "retrospective_processes",
}


def check_new_retrospective_process_data_type(value: str | None) -> NewRetrospectiveProcessDataType | None:
    if value is None:
        return None
    if value in NEW_RETROSPECTIVE_PROCESS_DATA_TYPE_VALUES:
        return cast(NewRetrospectiveProcessDataType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {NEW_RETROSPECTIVE_PROCESS_DATA_TYPE_VALUES!r}")
