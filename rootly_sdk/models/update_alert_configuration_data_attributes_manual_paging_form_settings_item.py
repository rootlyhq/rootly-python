from typing import Literal

UpdateAlertConfigurationDataAttributesManualPagingFormSettingsItem = Literal[
    "escalation_policy", "functionality", "service", "team", "user"
]

UPDATE_ALERT_CONFIGURATION_DATA_ATTRIBUTES_MANUAL_PAGING_FORM_SETTINGS_ITEM_VALUES: set[
    UpdateAlertConfigurationDataAttributesManualPagingFormSettingsItem
] = {
    "escalation_policy",
    "functionality",
    "service",
    "team",
    "user",
}


def check_update_alert_configuration_data_attributes_manual_paging_form_settings_item(
    value: str | None,
) -> UpdateAlertConfigurationDataAttributesManualPagingFormSettingsItem | None:
    if value is None:
        return None
    if value in UPDATE_ALERT_CONFIGURATION_DATA_ATTRIBUTES_MANUAL_PAGING_FORM_SETTINGS_ITEM_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_ALERT_CONFIGURATION_DATA_ATTRIBUTES_MANUAL_PAGING_FORM_SETTINGS_ITEM_VALUES!r}"
    )
