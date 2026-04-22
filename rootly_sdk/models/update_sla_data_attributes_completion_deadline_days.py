from typing import Literal, cast

UpdateSlaDataAttributesCompletionDeadlineDays = Literal[1, 2, 3, 4, 5, 6, 7, 14, 21, 30]

UPDATE_SLA_DATA_ATTRIBUTES_COMPLETION_DEADLINE_DAYS_VALUES: set[UpdateSlaDataAttributesCompletionDeadlineDays] = {
    1,
    2,
    3,
    4,
    5,
    6,
    7,
    14,
    21,
    30,
}


def check_update_sla_data_attributes_completion_deadline_days(
    value: int,
) -> UpdateSlaDataAttributesCompletionDeadlineDays:
    if value in UPDATE_SLA_DATA_ATTRIBUTES_COMPLETION_DEADLINE_DAYS_VALUES:
        return cast(UpdateSlaDataAttributesCompletionDeadlineDays, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_SLA_DATA_ATTRIBUTES_COMPLETION_DEADLINE_DAYS_VALUES!r}"
    )
