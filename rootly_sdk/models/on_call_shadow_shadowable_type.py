from typing import Literal, cast

OnCallShadowShadowableType = Literal["Schedule", "User"]

ON_CALL_SHADOW_SHADOWABLE_TYPE_VALUES: set[OnCallShadowShadowableType] = {
    "Schedule",
    "User",
}


def check_on_call_shadow_shadowable_type(value: str | None) -> OnCallShadowShadowableType | None:
    if value is None:
        return None
    if value in ON_CALL_SHADOW_SHADOWABLE_TYPE_VALUES:
        return cast(OnCallShadowShadowableType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ON_CALL_SHADOW_SHADOWABLE_TYPE_VALUES!r}")
