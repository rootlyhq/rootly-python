from typing import Literal, cast

UpdateSlaDataAttributesNotificationConfigurationsItemOffsetType = Literal["after_due", "before_due", "when_due"]

UPDATE_SLA_DATA_ATTRIBUTES_NOTIFICATION_CONFIGURATIONS_ITEM_OFFSET_TYPE_VALUES: set[
    UpdateSlaDataAttributesNotificationConfigurationsItemOffsetType
] = {
    "after_due",
    "before_due",
    "when_due",
}


def check_update_sla_data_attributes_notification_configurations_item_offset_type(
    value: str | None,
) -> UpdateSlaDataAttributesNotificationConfigurationsItemOffsetType | None:
    if value is None:
        return None
    if value in UPDATE_SLA_DATA_ATTRIBUTES_NOTIFICATION_CONFIGURATIONS_ITEM_OFFSET_TYPE_VALUES:
        return cast(UpdateSlaDataAttributesNotificationConfigurationsItemOffsetType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_SLA_DATA_ATTRIBUTES_NOTIFICATION_CONFIGURATIONS_ITEM_OFFSET_TYPE_VALUES!r}"
    )
