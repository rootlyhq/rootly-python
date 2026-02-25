from typing import Literal, cast

FunctionalityResponseDataType = Literal["functionalities"]

FUNCTIONALITY_RESPONSE_DATA_TYPE_VALUES: set[FunctionalityResponseDataType] = {
    "functionalities",
}


def check_functionality_response_data_type(value: str | None) -> FunctionalityResponseDataType | None:
    if value is None:
        return None
    if value in FUNCTIONALITY_RESPONSE_DATA_TYPE_VALUES:
        return cast(FunctionalityResponseDataType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {FUNCTIONALITY_RESPONSE_DATA_TYPE_VALUES!r}")
