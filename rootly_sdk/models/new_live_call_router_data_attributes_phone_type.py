from typing import Literal, cast

NewLiveCallRouterDataAttributesPhoneType = Literal["local", "mobile", "toll_free"]

NEW_LIVE_CALL_ROUTER_DATA_ATTRIBUTES_PHONE_TYPE_VALUES: set[NewLiveCallRouterDataAttributesPhoneType] = {
    "local",
    "mobile",
    "toll_free",
}


def check_new_live_call_router_data_attributes_phone_type(
    value: str | None,
) -> NewLiveCallRouterDataAttributesPhoneType | None:
    if value is None:
        return None
    if value in NEW_LIVE_CALL_ROUTER_DATA_ATTRIBUTES_PHONE_TYPE_VALUES:
        return cast(NewLiveCallRouterDataAttributesPhoneType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {NEW_LIVE_CALL_ROUTER_DATA_ATTRIBUTES_PHONE_TYPE_VALUES!r}"
    )
