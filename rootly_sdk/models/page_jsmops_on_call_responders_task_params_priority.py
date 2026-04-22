from typing import Literal, cast

PageJsmopsOnCallRespondersTaskParamsPriority = Literal["auto", "P1", "P2", "P3", "P4", "P5"]

PAGE_JSMOPS_ON_CALL_RESPONDERS_TASK_PARAMS_PRIORITY_VALUES: set[PageJsmopsOnCallRespondersTaskParamsPriority] = {
    "auto",
    "P1",
    "P2",
    "P3",
    "P4",
    "P5",
}


def check_page_jsmops_on_call_responders_task_params_priority(
    value: str | None,
) -> PageJsmopsOnCallRespondersTaskParamsPriority | None:
    if value is None:
        return None
    if value in PAGE_JSMOPS_ON_CALL_RESPONDERS_TASK_PARAMS_PRIORITY_VALUES:
        return cast(PageJsmopsOnCallRespondersTaskParamsPriority, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PAGE_JSMOPS_ON_CALL_RESPONDERS_TASK_PARAMS_PRIORITY_VALUES!r}"
    )
