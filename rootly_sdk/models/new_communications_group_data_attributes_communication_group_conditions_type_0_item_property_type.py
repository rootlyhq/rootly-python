from typing import Literal, cast

NewCommunicationsGroupDataAttributesCommunicationGroupConditionsType0ItemPropertyType = Literal[
    "functionality", "group", "incident_type", "service", "severity"
]

NEW_COMMUNICATIONS_GROUP_DATA_ATTRIBUTES_COMMUNICATION_GROUP_CONDITIONS_TYPE_0_ITEM_PROPERTY_TYPE_VALUES: set[
    NewCommunicationsGroupDataAttributesCommunicationGroupConditionsType0ItemPropertyType
] = {
    "functionality",
    "group",
    "incident_type",
    "service",
    "severity",
}


def check_new_communications_group_data_attributes_communication_group_conditions_type_0_item_property_type(
    value: str,
) -> NewCommunicationsGroupDataAttributesCommunicationGroupConditionsType0ItemPropertyType:
    if (
        value
        in NEW_COMMUNICATIONS_GROUP_DATA_ATTRIBUTES_COMMUNICATION_GROUP_CONDITIONS_TYPE_0_ITEM_PROPERTY_TYPE_VALUES
    ):
        return cast(NewCommunicationsGroupDataAttributesCommunicationGroupConditionsType0ItemPropertyType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {NEW_COMMUNICATIONS_GROUP_DATA_ATTRIBUTES_COMMUNICATION_GROUP_CONDITIONS_TYPE_0_ITEM_PROPERTY_TYPE_VALUES!r}"
    )
