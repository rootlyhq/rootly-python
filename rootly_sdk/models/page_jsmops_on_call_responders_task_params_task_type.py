from typing import Literal, cast

PageJsmopsOnCallRespondersTaskParamsTaskType = Literal["page_jsmops_on_call_responders"]

PAGE_JSMOPS_ON_CALL_RESPONDERS_TASK_PARAMS_TASK_TYPE_VALUES: set[PageJsmopsOnCallRespondersTaskParamsTaskType] = {
    "page_jsmops_on_call_responders",
}


def check_page_jsmops_on_call_responders_task_params_task_type(
    value: str | None,
) -> PageJsmopsOnCallRespondersTaskParamsTaskType | None:
    if value is None:
        return None
    if value in PAGE_JSMOPS_ON_CALL_RESPONDERS_TASK_PARAMS_TASK_TYPE_VALUES:
        return cast(PageJsmopsOnCallRespondersTaskParamsTaskType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PAGE_JSMOPS_ON_CALL_RESPONDERS_TASK_PARAMS_TASK_TYPE_VALUES!r}"
    )
