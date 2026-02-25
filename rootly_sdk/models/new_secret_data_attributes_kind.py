from typing import Literal, cast

NewSecretDataAttributesKind = Literal["built_in", "hashicorp_vault"]

NEW_SECRET_DATA_ATTRIBUTES_KIND_VALUES: set[NewSecretDataAttributesKind] = {
    "built_in",
    "hashicorp_vault",
}


def check_new_secret_data_attributes_kind(value: str | None) -> NewSecretDataAttributesKind | None:
    if value is None:
        return None
    if value in NEW_SECRET_DATA_ATTRIBUTES_KIND_VALUES:
        return cast(NewSecretDataAttributesKind, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {NEW_SECRET_DATA_ATTRIBUTES_KIND_VALUES!r}")
