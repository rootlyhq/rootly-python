from typing import Literal, cast

UpdateOnCallShadowDataAttributesShadowableType = Literal["Schedule", "User"]

UPDATE_ON_CALL_SHADOW_DATA_ATTRIBUTES_SHADOWABLE_TYPE_VALUES: set[UpdateOnCallShadowDataAttributesShadowableType] = {
    "Schedule",
    "User",
}


def check_update_on_call_shadow_data_attributes_shadowable_type(
    value: str | None,
) -> UpdateOnCallShadowDataAttributesShadowableType | None:
    if value is None:
        return None
    if value in UPDATE_ON_CALL_SHADOW_DATA_ATTRIBUTES_SHADOWABLE_TYPE_VALUES:
        return cast(UpdateOnCallShadowDataAttributesShadowableType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_ON_CALL_SHADOW_DATA_ATTRIBUTES_SHADOWABLE_TYPE_VALUES!r}"
    )
