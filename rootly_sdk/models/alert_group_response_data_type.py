from typing import Literal, cast

AlertGroupResponseDataType = Literal["alert_groups"]

ALERT_GROUP_RESPONSE_DATA_TYPE_VALUES: set[AlertGroupResponseDataType] = {
    "alert_groups",
}


def check_alert_group_response_data_type(value: str | None) -> AlertGroupResponseDataType | None:
    if value is None:
        return None
    if value in ALERT_GROUP_RESPONSE_DATA_TYPE_VALUES:
        return cast(AlertGroupResponseDataType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ALERT_GROUP_RESPONSE_DATA_TYPE_VALUES!r}")
