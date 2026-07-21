from typing import Literal, cast

OncallRelationshipsScheduleDataType0Type = Literal["schedules"]

ONCALL_RELATIONSHIPS_SCHEDULE_DATA_TYPE_0_TYPE_VALUES: set[OncallRelationshipsScheduleDataType0Type] = {
    "schedules",
}


def check_oncall_relationships_schedule_data_type_0_type(
    value: str | None,
) -> OncallRelationshipsScheduleDataType0Type | None:
    if value is None:
        return None
    if value in ONCALL_RELATIONSHIPS_SCHEDULE_DATA_TYPE_0_TYPE_VALUES:
        return cast(OncallRelationshipsScheduleDataType0Type, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ONCALL_RELATIONSHIPS_SCHEDULE_DATA_TYPE_0_TYPE_VALUES!r}"
    )
