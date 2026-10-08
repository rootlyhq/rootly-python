from typing import Literal

OncallNotificationType = Literal["audible", "quiet"]

ONCALL_NOTIFICATION_TYPE_VALUES: set[OncallNotificationType] = {
    "audible",
    "quiet",
}


def check_oncall_notification_type(value: str | None) -> OncallNotificationType | None:
    if value is None:
        return None
    if value in ONCALL_NOTIFICATION_TYPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ONCALL_NOTIFICATION_TYPE_VALUES!r}")
