from typing import Literal, cast

NewSecretDataType = Literal["secrets"]

NEW_SECRET_DATA_TYPE_VALUES: set[NewSecretDataType] = {
    "secrets",
}


def check_new_secret_data_type(value: str | None) -> NewSecretDataType | None:
    if value is None:
        return None
    if value in NEW_SECRET_DATA_TYPE_VALUES:
        return cast(NewSecretDataType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {NEW_SECRET_DATA_TYPE_VALUES!r}")
