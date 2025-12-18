from typing import Literal, cast

UpdateCommunicationsGroupDataAttributesCommunicationGroupConditionsType0ItemPropertyType = Literal[
    "functionality", "group", "incident_type", "service", "severity"
]

UPDATE_COMMUNICATIONS_GROUP_DATA_ATTRIBUTES_COMMUNICATION_GROUP_CONDITIONS_TYPE_0_ITEM_PROPERTY_TYPE_VALUES: set[
    UpdateCommunicationsGroupDataAttributesCommunicationGroupConditionsType0ItemPropertyType
] = {
    "functionality",
    "group",
    "incident_type",
    "service",
    "severity",
}


def check_update_communications_group_data_attributes_communication_group_conditions_type_0_item_property_type(
    value: str,
) -> UpdateCommunicationsGroupDataAttributesCommunicationGroupConditionsType0ItemPropertyType:
    if (
        value
        in UPDATE_COMMUNICATIONS_GROUP_DATA_ATTRIBUTES_COMMUNICATION_GROUP_CONDITIONS_TYPE_0_ITEM_PROPERTY_TYPE_VALUES
    ):
        return cast(UpdateCommunicationsGroupDataAttributesCommunicationGroupConditionsType0ItemPropertyType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_COMMUNICATIONS_GROUP_DATA_ATTRIBUTES_COMMUNICATION_GROUP_CONDITIONS_TYPE_0_ITEM_PROPERTY_TYPE_VALUES!r}"
    )
