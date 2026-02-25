from typing import Literal, cast

UpdateRetrospectiveConfigurationDataType = Literal["retrospective_configurations"]

UPDATE_RETROSPECTIVE_CONFIGURATION_DATA_TYPE_VALUES: set[UpdateRetrospectiveConfigurationDataType] = {
    "retrospective_configurations",
}


def check_update_retrospective_configuration_data_type(
    value: str | None,
) -> UpdateRetrospectiveConfigurationDataType | None:
    if value is None:
        return None
    if value in UPDATE_RETROSPECTIVE_CONFIGURATION_DATA_TYPE_VALUES:
        return cast(UpdateRetrospectiveConfigurationDataType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_RETROSPECTIVE_CONFIGURATION_DATA_TYPE_VALUES!r}"
    )
