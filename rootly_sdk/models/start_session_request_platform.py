from typing import Literal, cast

StartSessionRequestPlatform = Literal["google_meet", "microsoft_teams", "webex", "zoom"]

START_SESSION_REQUEST_PLATFORM_VALUES: set[StartSessionRequestPlatform] = {
    "google_meet",
    "microsoft_teams",
    "webex",
    "zoom",
}


def check_start_session_request_platform(value: str | None) -> StartSessionRequestPlatform | None:
    if value is None:
        return None
    if value in START_SESSION_REQUEST_PLATFORM_VALUES:
        return cast(StartSessionRequestPlatform, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {START_SESSION_REQUEST_PLATFORM_VALUES!r}")
