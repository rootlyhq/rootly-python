from typing import Literal, cast

UpdateRetrospectiveProcessGroupStepDataType = Literal["retrospective_process_group_steps"]

UPDATE_RETROSPECTIVE_PROCESS_GROUP_STEP_DATA_TYPE_VALUES: set[UpdateRetrospectiveProcessGroupStepDataType] = {
    "retrospective_process_group_steps",
}


def check_update_retrospective_process_group_step_data_type(
    value: str | None,
) -> UpdateRetrospectiveProcessGroupStepDataType | None:
    if value is None:
        return None
    if value in UPDATE_RETROSPECTIVE_PROCESS_GROUP_STEP_DATA_TYPE_VALUES:
        return cast(UpdateRetrospectiveProcessGroupStepDataType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_RETROSPECTIVE_PROCESS_GROUP_STEP_DATA_TYPE_VALUES!r}"
    )
