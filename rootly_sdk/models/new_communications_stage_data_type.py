from typing import Literal, cast

NewCommunicationsStageDataType = Literal["communications_stages"]

NEW_COMMUNICATIONS_STAGE_DATA_TYPE_VALUES: set[NewCommunicationsStageDataType] = {
    "communications_stages",
}


def check_new_communications_stage_data_type(value: str | None) -> NewCommunicationsStageDataType | None:
    if value is None:
        return None
    if value in NEW_COMMUNICATIONS_STAGE_DATA_TYPE_VALUES:
        return cast(NewCommunicationsStageDataType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {NEW_COMMUNICATIONS_STAGE_DATA_TYPE_VALUES!r}")
