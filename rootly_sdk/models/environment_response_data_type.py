from typing import Literal

EnvironmentResponseDataType = Literal["environments"]

ENVIRONMENT_RESPONSE_DATA_TYPE_VALUES: set[EnvironmentResponseDataType] = {
    "environments",
}


def check_environment_response_data_type(value: str | None) -> EnvironmentResponseDataType | None:
    if value is None:
        return None
    if value in ENVIRONMENT_RESPONSE_DATA_TYPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ENVIRONMENT_RESPONSE_DATA_TYPE_VALUES!r}")
