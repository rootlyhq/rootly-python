from typing import Literal, cast

OnCallShadowResponseDataType = Literal["on_call_shadows"]

ON_CALL_SHADOW_RESPONSE_DATA_TYPE_VALUES: set[OnCallShadowResponseDataType] = {
    "on_call_shadows",
}


def check_on_call_shadow_response_data_type(value: str | None) -> OnCallShadowResponseDataType | None:
    if value is None:
        return None
    if value in ON_CALL_SHADOW_RESPONSE_DATA_TYPE_VALUES:
        return cast(OnCallShadowResponseDataType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ON_CALL_SHADOW_RESPONSE_DATA_TYPE_VALUES!r}")
