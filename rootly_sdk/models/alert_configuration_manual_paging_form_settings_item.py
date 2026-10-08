from typing import Literal

AlertConfigurationManualPagingFormSettingsItem = Literal[
    "escalation_policy", "functionality", "service", "team", "user"
]

ALERT_CONFIGURATION_MANUAL_PAGING_FORM_SETTINGS_ITEM_VALUES: set[AlertConfigurationManualPagingFormSettingsItem] = {
    "escalation_policy",
    "functionality",
    "service",
    "team",
    "user",
}


def check_alert_configuration_manual_paging_form_settings_item(
    value: str | None,
) -> AlertConfigurationManualPagingFormSettingsItem | None:
    if value is None:
        return None
    if value in ALERT_CONFIGURATION_MANUAL_PAGING_FORM_SETTINGS_ITEM_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ALERT_CONFIGURATION_MANUAL_PAGING_FORM_SETTINGS_ITEM_VALUES!r}"
    )
