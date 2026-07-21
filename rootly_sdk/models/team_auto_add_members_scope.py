from typing import Literal, cast

TeamAutoAddMembersScope = Literal["all", "off", "public_and_test", "public_only"]

TEAM_AUTO_ADD_MEMBERS_SCOPE_VALUES: set[TeamAutoAddMembersScope] = {
    "all",
    "off",
    "public_and_test",
    "public_only",
}


def check_team_auto_add_members_scope(value: str | None) -> TeamAutoAddMembersScope | None:
    if value is None:
        return None
    if value in TEAM_AUTO_ADD_MEMBERS_SCOPE_VALUES:
        return cast(TeamAutoAddMembersScope, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {TEAM_AUTO_ADD_MEMBERS_SCOPE_VALUES!r}")
