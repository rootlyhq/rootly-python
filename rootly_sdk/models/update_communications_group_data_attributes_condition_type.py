from typing import Literal, cast

UpdateCommunicationsGroupDataAttributesConditionType = Literal["all", "any"]

UPDATE_COMMUNICATIONS_GROUP_DATA_ATTRIBUTES_CONDITION_TYPE_VALUES: set[
    UpdateCommunicationsGroupDataAttributesConditionType
] = {
    "all",
    "any",
}


def check_update_communications_group_data_attributes_condition_type(
    value: str | None,
) -> UpdateCommunicationsGroupDataAttributesConditionType | None:
    if value is None:
        return None
    if value in UPDATE_COMMUNICATIONS_GROUP_DATA_ATTRIBUTES_CONDITION_TYPE_VALUES:
        return cast(UpdateCommunicationsGroupDataAttributesConditionType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_COMMUNICATIONS_GROUP_DATA_ATTRIBUTES_CONDITION_TYPE_VALUES!r}"
    )
