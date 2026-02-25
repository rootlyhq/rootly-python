from typing import Literal, cast

UpdateRetrospectiveProcessDataType = Literal["retrospective_processes"]

UPDATE_RETROSPECTIVE_PROCESS_DATA_TYPE_VALUES: set[UpdateRetrospectiveProcessDataType] = {
    "retrospective_processes",
}


def check_update_retrospective_process_data_type(value: str | None) -> UpdateRetrospectiveProcessDataType | None:
    if value is None:
        return None
    if value in UPDATE_RETROSPECTIVE_PROCESS_DATA_TYPE_VALUES:
        return cast(UpdateRetrospectiveProcessDataType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {UPDATE_RETROSPECTIVE_PROCESS_DATA_TYPE_VALUES!r}")
