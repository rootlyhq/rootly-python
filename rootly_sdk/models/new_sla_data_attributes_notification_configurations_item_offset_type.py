from typing import Literal, cast

NewSlaDataAttributesNotificationConfigurationsItemOffsetType = Literal["after_due", "before_due", "when_due"]

NEW_SLA_DATA_ATTRIBUTES_NOTIFICATION_CONFIGURATIONS_ITEM_OFFSET_TYPE_VALUES: set[
    NewSlaDataAttributesNotificationConfigurationsItemOffsetType
] = {
    "after_due",
    "before_due",
    "when_due",
}


def check_new_sla_data_attributes_notification_configurations_item_offset_type(
    value: str | None,
) -> NewSlaDataAttributesNotificationConfigurationsItemOffsetType | None:
    if value is None:
        return None
    if value in NEW_SLA_DATA_ATTRIBUTES_NOTIFICATION_CONFIGURATIONS_ITEM_OFFSET_TYPE_VALUES:
        return cast(NewSlaDataAttributesNotificationConfigurationsItemOffsetType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {NEW_SLA_DATA_ATTRIBUTES_NOTIFICATION_CONFIGURATIONS_ITEM_OFFSET_TYPE_VALUES!r}"
    )
