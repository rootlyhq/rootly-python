from typing import Literal, cast

UpdatePagerdutyIncidentTaskParamsTaskType = Literal["update_pagerduty_incident"]

UPDATE_PAGERDUTY_INCIDENT_TASK_PARAMS_TASK_TYPE_VALUES: set[UpdatePagerdutyIncidentTaskParamsTaskType] = {
    "update_pagerduty_incident",
}


def check_update_pagerduty_incident_task_params_task_type(value: str | None) -> UpdatePagerdutyIncidentTaskParamsTaskType | None:
    if value is None:
        return None
    if value in UPDATE_PAGERDUTY_INCIDENT_TASK_PARAMS_TASK_TYPE_VALUES:
        return cast(UpdatePagerdutyIncidentTaskParamsTaskType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_PAGERDUTY_INCIDENT_TASK_PARAMS_TASK_TYPE_VALUES!r}"
    )
