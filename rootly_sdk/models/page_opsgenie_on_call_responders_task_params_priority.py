from typing import Literal, cast

PageOpsgenieOnCallRespondersTaskParamsPriority = Literal["auto", "P1", "P2", "P3", "P4", "P5"]

PAGE_OPSGENIE_ON_CALL_RESPONDERS_TASK_PARAMS_PRIORITY_VALUES: set[PageOpsgenieOnCallRespondersTaskParamsPriority] = {
    "auto",
    "P1",
    "P2",
    "P3",
    "P4",
    "P5",
}


def check_page_opsgenie_on_call_responders_task_params_priority(
    value: str | None,
) -> PageOpsgenieOnCallRespondersTaskParamsPriority | None:
    if value is None:
        return None
    if value in PAGE_OPSGENIE_ON_CALL_RESPONDERS_TASK_PARAMS_PRIORITY_VALUES:
        return cast(PageOpsgenieOnCallRespondersTaskParamsPriority, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PAGE_OPSGENIE_ON_CALL_RESPONDERS_TASK_PARAMS_PRIORITY_VALUES!r}"
    )
