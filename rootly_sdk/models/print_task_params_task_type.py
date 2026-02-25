from typing import Literal, cast

PrintTaskParamsTaskType = Literal["print"]

PRINT_TASK_PARAMS_TASK_TYPE_VALUES: set[PrintTaskParamsTaskType] = {
    "print",
}


def check_print_task_params_task_type(value: str | None) -> PrintTaskParamsTaskType | None:
    if value is None:
        return None
    if value in PRINT_TASK_PARAMS_TASK_TYPE_VALUES:
        return cast(PrintTaskParamsTaskType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PRINT_TASK_PARAMS_TASK_TYPE_VALUES!r}")
