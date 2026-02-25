from typing import Literal, cast

UpdateScheduleRotationDataAttributesScheduleRotationMembersType0ItemMemberType = Literal["Schedule", "User"]

UPDATE_SCHEDULE_ROTATION_DATA_ATTRIBUTES_SCHEDULE_ROTATION_MEMBERS_TYPE_0_ITEM_MEMBER_TYPE_VALUES: set[
    UpdateScheduleRotationDataAttributesScheduleRotationMembersType0ItemMemberType
] = {
    "Schedule",
    "User",
}


def check_update_schedule_rotation_data_attributes_schedule_rotation_members_type_0_item_member_type(
    value: str | None,
) -> UpdateScheduleRotationDataAttributesScheduleRotationMembersType0ItemMemberType | None:
    if value is None:
        return None
    if value in UPDATE_SCHEDULE_ROTATION_DATA_ATTRIBUTES_SCHEDULE_ROTATION_MEMBERS_TYPE_0_ITEM_MEMBER_TYPE_VALUES:
        return cast(UpdateScheduleRotationDataAttributesScheduleRotationMembersType0ItemMemberType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_SCHEDULE_ROTATION_DATA_ATTRIBUTES_SCHEDULE_ROTATION_MEMBERS_TYPE_0_ITEM_MEMBER_TYPE_VALUES!r}"
    )
