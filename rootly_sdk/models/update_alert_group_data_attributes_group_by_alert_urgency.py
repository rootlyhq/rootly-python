from typing import Literal

UpdateAlertGroupDataAttributesGroupByAlertUrgency = Literal[0, 1]

UPDATE_ALERT_GROUP_DATA_ATTRIBUTES_GROUP_BY_ALERT_URGENCY_VALUES: set[
    UpdateAlertGroupDataAttributesGroupByAlertUrgency
] = {
    0,
    1,
}


def check_update_alert_group_data_attributes_group_by_alert_urgency(
    value: int,
) -> UpdateAlertGroupDataAttributesGroupByAlertUrgency:
    if value in UPDATE_ALERT_GROUP_DATA_ATTRIBUTES_GROUP_BY_ALERT_URGENCY_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_ALERT_GROUP_DATA_ATTRIBUTES_GROUP_BY_ALERT_URGENCY_VALUES!r}"
    )
