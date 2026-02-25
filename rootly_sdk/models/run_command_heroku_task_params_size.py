from typing import Literal, cast

RunCommandHerokuTaskParamsSize = Literal["standard-1X", "standard-2X"]

RUN_COMMAND_HEROKU_TASK_PARAMS_SIZE_VALUES: set[RunCommandHerokuTaskParamsSize] = {
    "standard-1X",
    "standard-2X",
}


def check_run_command_heroku_task_params_size(value: str | None) -> RunCommandHerokuTaskParamsSize | None:
    if value is None:
        return None
    if value in RUN_COMMAND_HEROKU_TASK_PARAMS_SIZE_VALUES:
        return cast(RunCommandHerokuTaskParamsSize, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {RUN_COMMAND_HEROKU_TASK_PARAMS_SIZE_VALUES!r}")
