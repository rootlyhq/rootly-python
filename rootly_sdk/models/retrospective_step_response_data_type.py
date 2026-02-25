from typing import Literal, cast

RetrospectiveStepResponseDataType = Literal["retrospective_steps"]

RETROSPECTIVE_STEP_RESPONSE_DATA_TYPE_VALUES: set[RetrospectiveStepResponseDataType] = {
    "retrospective_steps",
}


def check_retrospective_step_response_data_type(value: str | None) -> RetrospectiveStepResponseDataType | None:
    if value is None:
        return None
    if value in RETROSPECTIVE_STEP_RESPONSE_DATA_TYPE_VALUES:
        return cast(RetrospectiveStepResponseDataType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {RETROSPECTIVE_STEP_RESPONSE_DATA_TYPE_VALUES!r}")
