from typing import Literal

AlertGroupTargetsItemTargetType = Literal["EscalationPolicy", "Functionality", "Group", "Service"]

ALERT_GROUP_TARGETS_ITEM_TARGET_TYPE_VALUES: set[AlertGroupTargetsItemTargetType] = {
    "EscalationPolicy",
    "Functionality",
    "Group",
    "Service",
}


def check_alert_group_targets_item_target_type(value: str | None) -> AlertGroupTargetsItemTargetType | None:
    if value is None:
        return None
    if value in ALERT_GROUP_TARGETS_ITEM_TARGET_TYPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ALERT_GROUP_TARGETS_ITEM_TARGET_TYPE_VALUES!r}")
