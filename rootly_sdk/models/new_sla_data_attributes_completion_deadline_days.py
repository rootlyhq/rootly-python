from typing import Literal, cast

NewSlaDataAttributesCompletionDeadlineDays = Literal[1, 2, 3, 4, 5, 6, 7, 14, 21, 30]

NEW_SLA_DATA_ATTRIBUTES_COMPLETION_DEADLINE_DAYS_VALUES: set[NewSlaDataAttributesCompletionDeadlineDays] = {
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


def check_new_sla_data_attributes_completion_deadline_days(value: int) -> NewSlaDataAttributesCompletionDeadlineDays:
    if value in NEW_SLA_DATA_ATTRIBUTES_COMPLETION_DEADLINE_DAYS_VALUES:
        return cast(NewSlaDataAttributesCompletionDeadlineDays, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {NEW_SLA_DATA_ATTRIBUTES_COMPLETION_DEADLINE_DAYS_VALUES!r}"
    )
