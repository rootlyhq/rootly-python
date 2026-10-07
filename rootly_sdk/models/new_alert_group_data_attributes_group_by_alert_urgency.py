from typing import Literal

NewAlertGroupDataAttributesGroupByAlertUrgency = Literal[0, 1]

NEW_ALERT_GROUP_DATA_ATTRIBUTES_GROUP_BY_ALERT_URGENCY_VALUES: set[NewAlertGroupDataAttributesGroupByAlertUrgency] = {
    0,
    1,
}


def check_new_alert_group_data_attributes_group_by_alert_urgency(
    value: int,
) -> NewAlertGroupDataAttributesGroupByAlertUrgency:
    if value in NEW_ALERT_GROUP_DATA_ATTRIBUTES_GROUP_BY_ALERT_URGENCY_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {NEW_ALERT_GROUP_DATA_ATTRIBUTES_GROUP_BY_ALERT_URGENCY_VALUES!r}"
    )
