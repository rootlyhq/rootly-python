from typing import Literal, cast

NewScheduleRotationDataAttributesScheduleRotationMembersType0ItemMemberType = Literal["Schedule", "User"]

NEW_SCHEDULE_ROTATION_DATA_ATTRIBUTES_SCHEDULE_ROTATION_MEMBERS_TYPE_0_ITEM_MEMBER_TYPE_VALUES: set[
    NewScheduleRotationDataAttributesScheduleRotationMembersType0ItemMemberType
] = {
    "Schedule",
    "User",
}


def check_new_schedule_rotation_data_attributes_schedule_rotation_members_type_0_item_member_type(
    value: str,
) -> NewScheduleRotationDataAttributesScheduleRotationMembersType0ItemMemberType:
    if value in NEW_SCHEDULE_ROTATION_DATA_ATTRIBUTES_SCHEDULE_ROTATION_MEMBERS_TYPE_0_ITEM_MEMBER_TYPE_VALUES:
        return cast(NewScheduleRotationDataAttributesScheduleRotationMembersType0ItemMemberType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {NEW_SCHEDULE_ROTATION_DATA_ATTRIBUTES_SCHEDULE_ROTATION_MEMBERS_TYPE_0_ITEM_MEMBER_TYPE_VALUES!r}"
    )
