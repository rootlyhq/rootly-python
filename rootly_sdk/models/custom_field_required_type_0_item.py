from typing import Literal, cast

CustomFieldRequiredType0Item = Literal[
    "incident_form",
    "incident_mitigation_form",
    "incident_mitigation_slack_form",
    "incident_post_mortem_form",
    "incident_resolution_form",
    "incident_resolution_slack_form",
    "incident_slack_form",
]

CUSTOM_FIELD_REQUIRED_TYPE_0_ITEM_VALUES: set[CustomFieldRequiredType0Item] = {
    "incident_form",
    "incident_mitigation_form",
    "incident_mitigation_slack_form",
    "incident_post_mortem_form",
    "incident_resolution_form",
    "incident_resolution_slack_form",
    "incident_slack_form",
}


def check_custom_field_required_type_0_item(value: str | None) -> CustomFieldRequiredType0Item | None:
    if value is None:
        return None
    if value in CUSTOM_FIELD_REQUIRED_TYPE_0_ITEM_VALUES:
        return cast(CustomFieldRequiredType0Item, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CUSTOM_FIELD_REQUIRED_TYPE_0_ITEM_VALUES!r}")
