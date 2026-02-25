from typing import Literal, cast

NewSubStatusDataAttributesParentStatus = Literal["retrospective", "started"]

NEW_SUB_STATUS_DATA_ATTRIBUTES_PARENT_STATUS_VALUES: set[NewSubStatusDataAttributesParentStatus] = {
    "retrospective",
    "started",
}


def check_new_sub_status_data_attributes_parent_status(value: str | None) -> NewSubStatusDataAttributesParentStatus | None:
    if value is None:
        return None
    if value in NEW_SUB_STATUS_DATA_ATTRIBUTES_PARENT_STATUS_VALUES:
        return cast(NewSubStatusDataAttributesParentStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {NEW_SUB_STATUS_DATA_ATTRIBUTES_PARENT_STATUS_VALUES!r}"
    )
