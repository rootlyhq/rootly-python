from typing import Literal, cast

UpdateCommunicationsStageDataType = Literal["communications_stages"]

UPDATE_COMMUNICATIONS_STAGE_DATA_TYPE_VALUES: set[UpdateCommunicationsStageDataType] = {
    "communications_stages",
}


def check_update_communications_stage_data_type(value: str | None) -> UpdateCommunicationsStageDataType | None:
    if value is None:
        return None
    if value in UPDATE_COMMUNICATIONS_STAGE_DATA_TYPE_VALUES:
        return cast(UpdateCommunicationsStageDataType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {UPDATE_COMMUNICATIONS_STAGE_DATA_TYPE_VALUES!r}")
