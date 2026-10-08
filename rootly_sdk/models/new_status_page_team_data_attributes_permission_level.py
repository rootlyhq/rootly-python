from typing import Literal

NewStatusPageTeamDataAttributesPermissionLevel = Literal["edit_and_publish", "publish_only"]

NEW_STATUS_PAGE_TEAM_DATA_ATTRIBUTES_PERMISSION_LEVEL_VALUES: set[NewStatusPageTeamDataAttributesPermissionLevel] = {
    "edit_and_publish",
    "publish_only",
}


def check_new_status_page_team_data_attributes_permission_level(
    value: str | None,
) -> NewStatusPageTeamDataAttributesPermissionLevel | None:
    if value is None:
        return None
    if value in NEW_STATUS_PAGE_TEAM_DATA_ATTRIBUTES_PERMISSION_LEVEL_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {NEW_STATUS_PAGE_TEAM_DATA_ATTRIBUTES_PERMISSION_LEVEL_VALUES!r}"
    )
