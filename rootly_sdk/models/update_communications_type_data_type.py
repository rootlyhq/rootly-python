from typing import Literal, cast

UpdateCommunicationsTypeDataType = Literal["communications_types"]

UPDATE_COMMUNICATIONS_TYPE_DATA_TYPE_VALUES: set[UpdateCommunicationsTypeDataType] = {
    "communications_types",
}


def check_update_communications_type_data_type(value: str | None) -> UpdateCommunicationsTypeDataType | None:
    if value is None:
        return None
    if value in UPDATE_COMMUNICATIONS_TYPE_DATA_TYPE_VALUES:
        return cast(UpdateCommunicationsTypeDataType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {UPDATE_COMMUNICATIONS_TYPE_DATA_TYPE_VALUES!r}")
