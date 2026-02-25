from typing import Literal, cast

UpdatePagerdutyIncidentTaskParamsStatus = Literal["acknowledged", "auto", "resolved"]

UPDATE_PAGERDUTY_INCIDENT_TASK_PARAMS_STATUS_VALUES: set[UpdatePagerdutyIncidentTaskParamsStatus] = {
    "acknowledged",
    "auto",
    "resolved",
}


def check_update_pagerduty_incident_task_params_status(value: str | None) -> UpdatePagerdutyIncidentTaskParamsStatus | None:
    if value is None:
        return None
    if value in UPDATE_PAGERDUTY_INCIDENT_TASK_PARAMS_STATUS_VALUES:
        return cast(UpdatePagerdutyIncidentTaskParamsStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_PAGERDUTY_INCIDENT_TASK_PARAMS_STATUS_VALUES!r}"
    )
