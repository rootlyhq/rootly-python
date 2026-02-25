from typing import Literal, cast

PagePagerdutyOnCallRespondersTaskParamsTaskType = Literal["page_pagerduty_on_call_responders"]

PAGE_PAGERDUTY_ON_CALL_RESPONDERS_TASK_PARAMS_TASK_TYPE_VALUES: set[PagePagerdutyOnCallRespondersTaskParamsTaskType] = {
    "page_pagerduty_on_call_responders",
}


def check_page_pagerduty_on_call_responders_task_params_task_type(
    value: str | None,
) -> PagePagerdutyOnCallRespondersTaskParamsTaskType | None:
    if value is None:
        return None
    if value in PAGE_PAGERDUTY_ON_CALL_RESPONDERS_TASK_PARAMS_TASK_TYPE_VALUES:
        return cast(PagePagerdutyOnCallRespondersTaskParamsTaskType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PAGE_PAGERDUTY_ON_CALL_RESPONDERS_TASK_PARAMS_TASK_TYPE_VALUES!r}"
    )
