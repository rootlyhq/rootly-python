from typing import Literal, cast

NewApiKeyDataAttributesKind = Literal["organization", "personal", "team"]

NEW_API_KEY_DATA_ATTRIBUTES_KIND_VALUES: set[NewApiKeyDataAttributesKind] = {
    "organization",
    "personal",
    "team",
}


def check_new_api_key_data_attributes_kind(value: str | None) -> NewApiKeyDataAttributesKind | None:
    if value is None:
        return None
    if value in NEW_API_KEY_DATA_ATTRIBUTES_KIND_VALUES:
        return cast(NewApiKeyDataAttributesKind, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {NEW_API_KEY_DATA_ATTRIBUTES_KIND_VALUES!r}")
