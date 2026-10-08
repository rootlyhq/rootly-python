from typing import Literal

StatusPageTeamPermissionLevel = Literal["edit_and_publish", "publish_only"]

STATUS_PAGE_TEAM_PERMISSION_LEVEL_VALUES: set[StatusPageTeamPermissionLevel] = {
    "edit_and_publish",
    "publish_only",
}


def check_status_page_team_permission_level(value: str | None) -> StatusPageTeamPermissionLevel | None:
    if value is None:
        return None
    if value in STATUS_PAGE_TEAM_PERMISSION_LEVEL_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {STATUS_PAGE_TEAM_PERMISSION_LEVEL_VALUES!r}")
