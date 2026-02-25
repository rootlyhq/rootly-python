from typing import Literal, cast

NewAlertDataAttributesNoise = Literal["noise", "not_noise"]

NEW_ALERT_DATA_ATTRIBUTES_NOISE_VALUES: set[NewAlertDataAttributesNoise] = {
    "noise",
    "not_noise",
}


def check_new_alert_data_attributes_noise(value: str | None) -> NewAlertDataAttributesNoise | None:
    if value is None:
        return None
    if value in NEW_ALERT_DATA_ATTRIBUTES_NOISE_VALUES:
        return cast(NewAlertDataAttributesNoise, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {NEW_ALERT_DATA_ATTRIBUTES_NOISE_VALUES!r}")
