from typing import Literal, cast

PostMortemTriggerParamsTriggerType = Literal["post_mortem"]

POST_MORTEM_TRIGGER_PARAMS_TRIGGER_TYPE_VALUES: set[PostMortemTriggerParamsTriggerType] = {
    "post_mortem",
}


def check_post_mortem_trigger_params_trigger_type(value: str | None) -> PostMortemTriggerParamsTriggerType | None:
    if value is None:
        return None
    if value in POST_MORTEM_TRIGGER_PARAMS_TRIGGER_TYPE_VALUES:
        return cast(PostMortemTriggerParamsTriggerType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {POST_MORTEM_TRIGGER_PARAMS_TRIGGER_TYPE_VALUES!r}")
