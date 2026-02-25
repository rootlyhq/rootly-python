from typing import Literal, cast

NewOnCallShadowDataType = Literal["on_call_shadows"]

NEW_ON_CALL_SHADOW_DATA_TYPE_VALUES: set[NewOnCallShadowDataType] = {
    "on_call_shadows",
}


def check_new_on_call_shadow_data_type(value: str | None) -> NewOnCallShadowDataType | None:
    if value is None:
        return None
    if value in NEW_ON_CALL_SHADOW_DATA_TYPE_VALUES:
        return cast(NewOnCallShadowDataType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {NEW_ON_CALL_SHADOW_DATA_TYPE_VALUES!r}")
