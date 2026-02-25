from typing import Literal, cast

UpdateOnCallShadowDataType = Literal["on_call_shadows"]

UPDATE_ON_CALL_SHADOW_DATA_TYPE_VALUES: set[UpdateOnCallShadowDataType] = {
    "on_call_shadows",
}


def check_update_on_call_shadow_data_type(value: str | None) -> UpdateOnCallShadowDataType | None:
    if value is None:
        return None
    if value in UPDATE_ON_CALL_SHADOW_DATA_TYPE_VALUES:
        return cast(UpdateOnCallShadowDataType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {UPDATE_ON_CALL_SHADOW_DATA_TYPE_VALUES!r}")
