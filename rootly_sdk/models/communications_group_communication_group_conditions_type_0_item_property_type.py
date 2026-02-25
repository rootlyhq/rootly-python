from typing import Literal, cast

CommunicationsGroupCommunicationGroupConditionsType0ItemPropertyType = Literal[
    "functionality", "group", "incident_type", "service", "severity"
]

COMMUNICATIONS_GROUP_COMMUNICATION_GROUP_CONDITIONS_TYPE_0_ITEM_PROPERTY_TYPE_VALUES: set[
    CommunicationsGroupCommunicationGroupConditionsType0ItemPropertyType
] = {
    "functionality",
    "group",
    "incident_type",
    "service",
    "severity",
}


def check_communications_group_communication_group_conditions_type_0_item_property_type(
    value: str | None,
) -> CommunicationsGroupCommunicationGroupConditionsType0ItemPropertyType | None:
    if value is None:
        return None
    if value in COMMUNICATIONS_GROUP_COMMUNICATION_GROUP_CONDITIONS_TYPE_0_ITEM_PROPERTY_TYPE_VALUES:
        return cast(CommunicationsGroupCommunicationGroupConditionsType0ItemPropertyType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {COMMUNICATIONS_GROUP_COMMUNICATION_GROUP_CONDITIONS_TYPE_0_ITEM_PROPERTY_TYPE_VALUES!r}"
    )
