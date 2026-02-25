from typing import Literal, cast

CustomFieldShownItem = Literal[
    "incident_form",
    "incident_mitigation_form",
    "incident_mitigation_slack_form",
    "incident_post_mortem",
    "incident_post_mortem_form",
    "incident_resolution_form",
    "incident_resolution_slack_form",
    "incident_slack_form",
]

CUSTOM_FIELD_SHOWN_ITEM_VALUES: set[CustomFieldShownItem] = {
    "incident_form",
    "incident_mitigation_form",
    "incident_mitigation_slack_form",
    "incident_post_mortem",
    "incident_post_mortem_form",
    "incident_resolution_form",
    "incident_resolution_slack_form",
    "incident_slack_form",
}


def check_custom_field_shown_item(value: str | None) -> CustomFieldShownItem | None:
    if value is None:
        return None
    if value in CUSTOM_FIELD_SHOWN_ITEM_VALUES:
        return cast(CustomFieldShownItem, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CUSTOM_FIELD_SHOWN_ITEM_VALUES!r}")
