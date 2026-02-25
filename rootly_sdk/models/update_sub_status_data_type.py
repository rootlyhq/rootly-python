from typing import Literal, cast

UpdateSubStatusDataType = Literal["sub_statuses"]

UPDATE_SUB_STATUS_DATA_TYPE_VALUES: set[UpdateSubStatusDataType] = {
    "sub_statuses",
}


def check_update_sub_status_data_type(value: str | None) -> UpdateSubStatusDataType | None:
    if value is None:
        return None
    if value in UPDATE_SUB_STATUS_DATA_TYPE_VALUES:
        return cast(UpdateSubStatusDataType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {UPDATE_SUB_STATUS_DATA_TYPE_VALUES!r}")
