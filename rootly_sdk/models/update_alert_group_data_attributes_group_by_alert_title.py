from typing import Literal

UpdateAlertGroupDataAttributesGroupByAlertTitle = Literal[0, 1]

UPDATE_ALERT_GROUP_DATA_ATTRIBUTES_GROUP_BY_ALERT_TITLE_VALUES: set[UpdateAlertGroupDataAttributesGroupByAlertTitle] = {
    0,
    1,
}


def check_update_alert_group_data_attributes_group_by_alert_title(
    value: int,
) -> UpdateAlertGroupDataAttributesGroupByAlertTitle:
    if value in UPDATE_ALERT_GROUP_DATA_ATTRIBUTES_GROUP_BY_ALERT_TITLE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_ALERT_GROUP_DATA_ATTRIBUTES_GROUP_BY_ALERT_TITLE_VALUES!r}"
    )
