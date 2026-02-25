from typing import Literal, cast

NewRetrospectiveProcessGroupStepDataType = Literal["retrospective_process_group_steps"]

NEW_RETROSPECTIVE_PROCESS_GROUP_STEP_DATA_TYPE_VALUES: set[NewRetrospectiveProcessGroupStepDataType] = {
    "retrospective_process_group_steps",
}


def check_new_retrospective_process_group_step_data_type(
    value: str | None,
) -> NewRetrospectiveProcessGroupStepDataType | None:
    if value is None:
        return None
    if value in NEW_RETROSPECTIVE_PROCESS_GROUP_STEP_DATA_TYPE_VALUES:
        return cast(NewRetrospectiveProcessGroupStepDataType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {NEW_RETROSPECTIVE_PROCESS_GROUP_STEP_DATA_TYPE_VALUES!r}"
    )
