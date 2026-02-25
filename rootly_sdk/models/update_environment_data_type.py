from typing import Literal, cast

UpdateEnvironmentDataType = Literal["environments"]

UPDATE_ENVIRONMENT_DATA_TYPE_VALUES: set[UpdateEnvironmentDataType] = {
    "environments",
}


def check_update_environment_data_type(value: str | None) -> UpdateEnvironmentDataType | None:
    if value is None:
        return None
    if value in UPDATE_ENVIRONMENT_DATA_TYPE_VALUES:
        return cast(UpdateEnvironmentDataType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {UPDATE_ENVIRONMENT_DATA_TYPE_VALUES!r}")
