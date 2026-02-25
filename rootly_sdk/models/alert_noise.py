from typing import Literal, cast

AlertNoise = Literal["noise", "not_noise"]

ALERT_NOISE_VALUES: set[AlertNoise] = {
    "noise",
    "not_noise",
}


def check_alert_noise(value: str | None) -> AlertNoise | None:
    if value is None:
        return None
    if value in ALERT_NOISE_VALUES:
        return cast(AlertNoise, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ALERT_NOISE_VALUES!r}")
