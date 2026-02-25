from typing import Literal, cast

RetrospectiveProcessResponseDataType = Literal["retrospective_processes"]

RETROSPECTIVE_PROCESS_RESPONSE_DATA_TYPE_VALUES: set[RetrospectiveProcessResponseDataType] = {
    "retrospective_processes",
}


def check_retrospective_process_response_data_type(value: str | None) -> RetrospectiveProcessResponseDataType | None:
    if value is None:
        return None
    if value in RETROSPECTIVE_PROCESS_RESPONSE_DATA_TYPE_VALUES:
        return cast(RetrospectiveProcessResponseDataType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {RETROSPECTIVE_PROCESS_RESPONSE_DATA_TYPE_VALUES!r}")
