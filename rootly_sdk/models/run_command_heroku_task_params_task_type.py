from typing import Literal, cast

RunCommandHerokuTaskParamsTaskType = Literal["run_command_heroku"]

RUN_COMMAND_HEROKU_TASK_PARAMS_TASK_TYPE_VALUES: set[RunCommandHerokuTaskParamsTaskType] = {
    "run_command_heroku",
}


def check_run_command_heroku_task_params_task_type(value: str | None) -> RunCommandHerokuTaskParamsTaskType | None:
    if value is None:
        return None
    if value in RUN_COMMAND_HEROKU_TASK_PARAMS_TASK_TYPE_VALUES:
        return cast(RunCommandHerokuTaskParamsTaskType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {RUN_COMMAND_HEROKU_TASK_PARAMS_TASK_TYPE_VALUES!r}")
