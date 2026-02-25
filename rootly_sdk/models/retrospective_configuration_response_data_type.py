from typing import Literal, cast

RetrospectiveConfigurationResponseDataType = Literal["retrospective_configurations"]

RETROSPECTIVE_CONFIGURATION_RESPONSE_DATA_TYPE_VALUES: set[RetrospectiveConfigurationResponseDataType] = {
    "retrospective_configurations",
}


def check_retrospective_configuration_response_data_type(value: str | None) -> RetrospectiveConfigurationResponseDataType | None:
    if value is None:
        return None
    if value in RETROSPECTIVE_CONFIGURATION_RESPONSE_DATA_TYPE_VALUES:
        return cast(RetrospectiveConfigurationResponseDataType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {RETROSPECTIVE_CONFIGURATION_RESPONSE_DATA_TYPE_VALUES!r}"
    )
