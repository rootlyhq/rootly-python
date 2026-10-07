from typing import Literal

UpdateStatusPageTeamDataAttributesPermissionLevel = Literal["edit_and_publish", "publish_only"]

UPDATE_STATUS_PAGE_TEAM_DATA_ATTRIBUTES_PERMISSION_LEVEL_VALUES: set[
    UpdateStatusPageTeamDataAttributesPermissionLevel
] = {
    "edit_and_publish",
    "publish_only",
}


def check_update_status_page_team_data_attributes_permission_level(
    value: str | None,
) -> UpdateStatusPageTeamDataAttributesPermissionLevel | None:
    if value is None:
        return None
    if value in UPDATE_STATUS_PAGE_TEAM_DATA_ATTRIBUTES_PERMISSION_LEVEL_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_STATUS_PAGE_TEAM_DATA_ATTRIBUTES_PERMISSION_LEVEL_VALUES!r}"
    )
