from typing import Literal, cast

NewSubStatusDataType = Literal["sub_statuses"]

NEW_SUB_STATUS_DATA_TYPE_VALUES: set[NewSubStatusDataType] = {
    "sub_statuses",
}


def check_new_sub_status_data_type(value: str | None) -> NewSubStatusDataType | None:
    if value is None:
        return None
    if value in NEW_SUB_STATUS_DATA_TYPE_VALUES:
        return cast(NewSubStatusDataType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {NEW_SUB_STATUS_DATA_TYPE_VALUES!r}")
