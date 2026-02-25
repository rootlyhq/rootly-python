from typing import Literal, cast

UpdateSecretDataType = Literal["secrets"]

UPDATE_SECRET_DATA_TYPE_VALUES: set[UpdateSecretDataType] = {
    "secrets",
}


def check_update_secret_data_type(value: str | None) -> UpdateSecretDataType | None:
    if value is None:
        return None
    if value in UPDATE_SECRET_DATA_TYPE_VALUES:
        return cast(UpdateSecretDataType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {UPDATE_SECRET_DATA_TYPE_VALUES!r}")
