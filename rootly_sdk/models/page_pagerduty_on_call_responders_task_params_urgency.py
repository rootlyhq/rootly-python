from typing import Literal, cast

PagePagerdutyOnCallRespondersTaskParamsUrgency = Literal["auto", "high", "low"]

PAGE_PAGERDUTY_ON_CALL_RESPONDERS_TASK_PARAMS_URGENCY_VALUES: set[PagePagerdutyOnCallRespondersTaskParamsUrgency] = {
    "auto",
    "high",
    "low",
}


def check_page_pagerduty_on_call_responders_task_params_urgency(
    value: str | None,
) -> PagePagerdutyOnCallRespondersTaskParamsUrgency | None:
    if value is None:
        return None
    if value in PAGE_PAGERDUTY_ON_CALL_RESPONDERS_TASK_PARAMS_URGENCY_VALUES:
        return cast(PagePagerdutyOnCallRespondersTaskParamsUrgency, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PAGE_PAGERDUTY_ON_CALL_RESPONDERS_TASK_PARAMS_URGENCY_VALUES!r}"
    )
