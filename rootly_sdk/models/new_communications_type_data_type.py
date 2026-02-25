from typing import Literal, cast

NewCommunicationsTypeDataType = Literal["communications_types"]

NEW_COMMUNICATIONS_TYPE_DATA_TYPE_VALUES: set[NewCommunicationsTypeDataType] = {
    "communications_types",
}


def check_new_communications_type_data_type(value: str | None) -> NewCommunicationsTypeDataType | None:
    if value is None:
        return None
    if value in NEW_COMMUNICATIONS_TYPE_DATA_TYPE_VALUES:
        return cast(NewCommunicationsTypeDataType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {NEW_COMMUNICATIONS_TYPE_DATA_TYPE_VALUES!r}")
