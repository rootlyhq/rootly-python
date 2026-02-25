from typing import Literal, cast

AlertGroupTargetsItemTargetType = Literal["EscalationPolicy", "Group", "Service"]

ALERT_GROUP_TARGETS_ITEM_TARGET_TYPE_VALUES: set[AlertGroupTargetsItemTargetType] = {
    "EscalationPolicy",
    "Group",
    "Service",
}


def check_alert_group_targets_item_target_type(value: str | None) -> AlertGroupTargetsItemTargetType | None:
    if value is None:
        return None
    if value in ALERT_GROUP_TARGETS_ITEM_TARGET_TYPE_VALUES:
        return cast(AlertGroupTargetsItemTargetType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ALERT_GROUP_TARGETS_ITEM_TARGET_TYPE_VALUES!r}")
