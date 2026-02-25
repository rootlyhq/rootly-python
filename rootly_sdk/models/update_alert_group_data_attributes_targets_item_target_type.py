from typing import Literal, cast

UpdateAlertGroupDataAttributesTargetsItemTargetType = Literal["EscalationPolicy", "Group", "Service"]

UPDATE_ALERT_GROUP_DATA_ATTRIBUTES_TARGETS_ITEM_TARGET_TYPE_VALUES: set[
    UpdateAlertGroupDataAttributesTargetsItemTargetType
] = {
    "EscalationPolicy",
    "Group",
    "Service",
}


def check_update_alert_group_data_attributes_targets_item_target_type(
    value: str | None,
) -> UpdateAlertGroupDataAttributesTargetsItemTargetType | None:
    if value is None:
        return None
    if value in UPDATE_ALERT_GROUP_DATA_ATTRIBUTES_TARGETS_ITEM_TARGET_TYPE_VALUES:
        return cast(UpdateAlertGroupDataAttributesTargetsItemTargetType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_ALERT_GROUP_DATA_ATTRIBUTES_TARGETS_ITEM_TARGET_TYPE_VALUES!r}"
    )
