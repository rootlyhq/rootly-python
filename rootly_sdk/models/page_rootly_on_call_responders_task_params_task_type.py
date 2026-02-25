from typing import Literal, cast

PageRootlyOnCallRespondersTaskParamsTaskType = Literal["page_rootly_on_call_responders"]

PAGE_ROOTLY_ON_CALL_RESPONDERS_TASK_PARAMS_TASK_TYPE_VALUES: set[PageRootlyOnCallRespondersTaskParamsTaskType] = {
    "page_rootly_on_call_responders",
}


def check_page_rootly_on_call_responders_task_params_task_type(
    value: str | None,
) -> PageRootlyOnCallRespondersTaskParamsTaskType | None:
    if value is None:
        return None
    if value in PAGE_ROOTLY_ON_CALL_RESPONDERS_TASK_PARAMS_TASK_TYPE_VALUES:
        return cast(PageRootlyOnCallRespondersTaskParamsTaskType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PAGE_ROOTLY_ON_CALL_RESPONDERS_TASK_PARAMS_TASK_TYPE_VALUES!r}"
    )
