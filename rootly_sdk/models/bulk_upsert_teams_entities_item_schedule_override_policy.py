from typing import Literal

BulkUpsertTeamsEntitiesItemScheduleOverridePolicy = Literal["admins", "everyone", "members"]

BULK_UPSERT_TEAMS_ENTITIES_ITEM_SCHEDULE_OVERRIDE_POLICY_VALUES: set[
    BulkUpsertTeamsEntitiesItemScheduleOverridePolicy
] = {
    "admins",
    "everyone",
    "members",
}


def check_bulk_upsert_teams_entities_item_schedule_override_policy(
    value: str | None,
) -> BulkUpsertTeamsEntitiesItemScheduleOverridePolicy | None:
    if value is None:
        return None
    if value in BULK_UPSERT_TEAMS_ENTITIES_ITEM_SCHEDULE_OVERRIDE_POLICY_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {BULK_UPSERT_TEAMS_ENTITIES_ITEM_SCHEDULE_OVERRIDE_POLICY_VALUES!r}"
    )
