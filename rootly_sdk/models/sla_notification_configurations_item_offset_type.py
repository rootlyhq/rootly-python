from typing import Literal, cast

SlaNotificationConfigurationsItemOffsetType = Literal["after_due", "before_due", "when_due"]

SLA_NOTIFICATION_CONFIGURATIONS_ITEM_OFFSET_TYPE_VALUES: set[SlaNotificationConfigurationsItemOffsetType] = {
    "after_due",
    "before_due",
    "when_due",
}


def check_sla_notification_configurations_item_offset_type(
    value: str | None,
) -> SlaNotificationConfigurationsItemOffsetType | None:
    if value is None:
        return None
    if value in SLA_NOTIFICATION_CONFIGURATIONS_ITEM_OFFSET_TYPE_VALUES:
        return cast(SlaNotificationConfigurationsItemOffsetType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {SLA_NOTIFICATION_CONFIGURATIONS_ITEM_OFFSET_TYPE_VALUES!r}"
    )
