from typing import Literal, cast

NewAlertGroupDataAttributesTargetsItemTargetType = Literal["EscalationPolicy", "Group", "Service"]

NEW_ALERT_GROUP_DATA_ATTRIBUTES_TARGETS_ITEM_TARGET_TYPE_VALUES: set[
    NewAlertGroupDataAttributesTargetsItemTargetType
] = {
    "EscalationPolicy",
    "Group",
    "Service",
}


def check_new_alert_group_data_attributes_targets_item_target_type(
    value: str | None,
) -> NewAlertGroupDataAttributesTargetsItemTargetType | None:
    if value is None:
        return None
    if value in NEW_ALERT_GROUP_DATA_ATTRIBUTES_TARGETS_ITEM_TARGET_TYPE_VALUES:
        return cast(NewAlertGroupDataAttributesTargetsItemTargetType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {NEW_ALERT_GROUP_DATA_ATTRIBUTES_TARGETS_ITEM_TARGET_TYPE_VALUES!r}"
    )
