from typing import Literal, cast

NewRetrospectiveStepDataType = Literal["retrospective_steps"]

NEW_RETROSPECTIVE_STEP_DATA_TYPE_VALUES: set[NewRetrospectiveStepDataType] = {
    "retrospective_steps",
}


def check_new_retrospective_step_data_type(value: str | None) -> NewRetrospectiveStepDataType | None:
    if value is None:
        return None
    if value in NEW_RETROSPECTIVE_STEP_DATA_TYPE_VALUES:
        return cast(NewRetrospectiveStepDataType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {NEW_RETROSPECTIVE_STEP_DATA_TYPE_VALUES!r}")
