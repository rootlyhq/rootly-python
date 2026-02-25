from typing import Literal, cast

NewOnCallShadowDataAttributesShadowableType = Literal["Schedule", "User"]

NEW_ON_CALL_SHADOW_DATA_ATTRIBUTES_SHADOWABLE_TYPE_VALUES: set[NewOnCallShadowDataAttributesShadowableType] = {
    "Schedule",
    "User",
}


def check_new_on_call_shadow_data_attributes_shadowable_type(
    value: str | None,
) -> NewOnCallShadowDataAttributesShadowableType | None:
    if value is None:
        return None
    if value in NEW_ON_CALL_SHADOW_DATA_ATTRIBUTES_SHADOWABLE_TYPE_VALUES:
        return cast(NewOnCallShadowDataAttributesShadowableType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {NEW_ON_CALL_SHADOW_DATA_ATTRIBUTES_SHADOWABLE_TYPE_VALUES!r}"
    )
