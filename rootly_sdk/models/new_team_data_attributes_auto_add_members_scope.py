from typing import Literal

NewTeamDataAttributesAutoAddMembersScope = Literal["all", "off", "public_and_test", "public_only"]

NEW_TEAM_DATA_ATTRIBUTES_AUTO_ADD_MEMBERS_SCOPE_VALUES: set[NewTeamDataAttributesAutoAddMembersScope] = {
    "all",
    "off",
    "public_and_test",
    "public_only",
}


def check_new_team_data_attributes_auto_add_members_scope(
    value: str | None,
) -> NewTeamDataAttributesAutoAddMembersScope | None:
    if value is None:
        return None
    if value in NEW_TEAM_DATA_ATTRIBUTES_AUTO_ADD_MEMBERS_SCOPE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {NEW_TEAM_DATA_ATTRIBUTES_AUTO_ADD_MEMBERS_SCOPE_VALUES!r}"
    )
