from typing import Literal, cast

UpdatePagerdutyIncidentTaskParamsUrgency = Literal["auto", "high", "low"]

UPDATE_PAGERDUTY_INCIDENT_TASK_PARAMS_URGENCY_VALUES: set[UpdatePagerdutyIncidentTaskParamsUrgency] = {
    "auto",
    "high",
    "low",
}


def check_update_pagerduty_incident_task_params_urgency(value: str | None) -> UpdatePagerdutyIncidentTaskParamsUrgency | None:
    if value is None:
        return None
    if value in UPDATE_PAGERDUTY_INCIDENT_TASK_PARAMS_URGENCY_VALUES:
        return cast(UpdatePagerdutyIncidentTaskParamsUrgency, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_PAGERDUTY_INCIDENT_TASK_PARAMS_URGENCY_VALUES!r}"
    )
