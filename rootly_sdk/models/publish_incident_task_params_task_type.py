from typing import Literal, cast

PublishIncidentTaskParamsTaskType = Literal["publish_incident"]

PUBLISH_INCIDENT_TASK_PARAMS_TASK_TYPE_VALUES: set[PublishIncidentTaskParamsTaskType] = {
    "publish_incident",
}


def check_publish_incident_task_params_task_type(value: str | None) -> PublishIncidentTaskParamsTaskType | None:
    if value is None:
        return None
    if value in PUBLISH_INCIDENT_TASK_PARAMS_TASK_TYPE_VALUES:
        return cast(PublishIncidentTaskParamsTaskType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PUBLISH_INCIDENT_TASK_PARAMS_TASK_TYPE_VALUES!r}")
