from typing import Literal, cast

NewSlaDataAttributesAssignmentDeadlineDays = Literal[1, 2, 3, 4, 5, 6, 7, 14, 21, 30]

NEW_SLA_DATA_ATTRIBUTES_ASSIGNMENT_DEADLINE_DAYS_VALUES: set[NewSlaDataAttributesAssignmentDeadlineDays] = {
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


def check_new_sla_data_attributes_assignment_deadline_days(value: int) -> NewSlaDataAttributesAssignmentDeadlineDays:
    if value in NEW_SLA_DATA_ATTRIBUTES_ASSIGNMENT_DEADLINE_DAYS_VALUES:
        return cast(NewSlaDataAttributesAssignmentDeadlineDays, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {NEW_SLA_DATA_ATTRIBUTES_ASSIGNMENT_DEADLINE_DAYS_VALUES!r}"
    )
