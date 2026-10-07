from typing import Literal

NewAlertGroupDataAttributesGroupByAlertTitle = Literal[0, 1]

NEW_ALERT_GROUP_DATA_ATTRIBUTES_GROUP_BY_ALERT_TITLE_VALUES: set[NewAlertGroupDataAttributesGroupByAlertTitle] = {
    0,
    1,
}


def check_new_alert_group_data_attributes_group_by_alert_title(
    value: int,
) -> NewAlertGroupDataAttributesGroupByAlertTitle:
    if value in NEW_ALERT_GROUP_DATA_ATTRIBUTES_GROUP_BY_ALERT_TITLE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {NEW_ALERT_GROUP_DATA_ATTRIBUTES_GROUP_BY_ALERT_TITLE_VALUES!r}"
    )
