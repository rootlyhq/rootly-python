from typing import Literal

UpdateTeamDataAttributesAutoAddMembersScope = Literal["all", "off", "public_and_test", "public_only"]

UPDATE_TEAM_DATA_ATTRIBUTES_AUTO_ADD_MEMBERS_SCOPE_VALUES: set[UpdateTeamDataAttributesAutoAddMembersScope] = {
    "all",
    "off",
    "public_and_test",
    "public_only",
}


def check_update_team_data_attributes_auto_add_members_scope(
    value: str | None,
) -> UpdateTeamDataAttributesAutoAddMembersScope | None:
    if value is None:
        return None
    if value in UPDATE_TEAM_DATA_ATTRIBUTES_AUTO_ADD_MEMBERS_SCOPE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_TEAM_DATA_ATTRIBUTES_AUTO_ADD_MEMBERS_SCOPE_VALUES!r}"
    )
