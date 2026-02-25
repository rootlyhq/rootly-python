from typing import Literal, cast

NewEnvironmentDataType = Literal["environments"]

NEW_ENVIRONMENT_DATA_TYPE_VALUES: set[NewEnvironmentDataType] = {
    "environments",
}


def check_new_environment_data_type(value: str | None) -> NewEnvironmentDataType | None:
    if value is None:
        return None
    if value in NEW_ENVIRONMENT_DATA_TYPE_VALUES:
        return cast(NewEnvironmentDataType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {NEW_ENVIRONMENT_DATA_TYPE_VALUES!r}")
