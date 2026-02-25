from typing import Literal, cast

RetrospectiveProcessGroupStepResponseDataType = Literal["retrospective_process_group_steps"]

RETROSPECTIVE_PROCESS_GROUP_STEP_RESPONSE_DATA_TYPE_VALUES: set[RetrospectiveProcessGroupStepResponseDataType] = {
    "retrospective_process_group_steps",
}


def check_retrospective_process_group_step_response_data_type(
    value: str | None,
) -> RetrospectiveProcessGroupStepResponseDataType | None:
    if value is None:
        return None
    if value in RETROSPECTIVE_PROCESS_GROUP_STEP_RESPONSE_DATA_TYPE_VALUES:
        return cast(RetrospectiveProcessGroupStepResponseDataType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {RETROSPECTIVE_PROCESS_GROUP_STEP_RESPONSE_DATA_TYPE_VALUES!r}"
    )
