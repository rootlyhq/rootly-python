from typing import Literal, cast

NewCommunicationsGroupDataAttributesConditionType = Literal["all", "any"]

NEW_COMMUNICATIONS_GROUP_DATA_ATTRIBUTES_CONDITION_TYPE_VALUES: set[
    NewCommunicationsGroupDataAttributesConditionType
] = {
    "all",
    "any",
}


def check_new_communications_group_data_attributes_condition_type(
    value: str | None,
) -> NewCommunicationsGroupDataAttributesConditionType | None:
    if value is None:
        return None
    if value in NEW_COMMUNICATIONS_GROUP_DATA_ATTRIBUTES_CONDITION_TYPE_VALUES:
        return cast(NewCommunicationsGroupDataAttributesConditionType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {NEW_COMMUNICATIONS_GROUP_DATA_ATTRIBUTES_CONDITION_TYPE_VALUES!r}"
    )
