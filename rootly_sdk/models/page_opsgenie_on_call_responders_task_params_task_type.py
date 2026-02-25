from typing import Literal, cast

PageOpsgenieOnCallRespondersTaskParamsTaskType = Literal["page_opsgenie_on_call_responders"]

PAGE_OPSGENIE_ON_CALL_RESPONDERS_TASK_PARAMS_TASK_TYPE_VALUES: set[PageOpsgenieOnCallRespondersTaskParamsTaskType] = {
    "page_opsgenie_on_call_responders",
}


def check_page_opsgenie_on_call_responders_task_params_task_type(
    value: str | None,
) -> PageOpsgenieOnCallRespondersTaskParamsTaskType | None:
    if value is None:
        return None
    if value in PAGE_OPSGENIE_ON_CALL_RESPONDERS_TASK_PARAMS_TASK_TYPE_VALUES:
        return cast(PageOpsgenieOnCallRespondersTaskParamsTaskType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PAGE_OPSGENIE_ON_CALL_RESPONDERS_TASK_PARAMS_TASK_TYPE_VALUES!r}"
    )
