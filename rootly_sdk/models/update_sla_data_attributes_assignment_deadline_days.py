from typing import Literal, cast

UpdateSlaDataAttributesAssignmentDeadlineDays = Literal[1, 2, 3, 4, 5, 6, 7, 14, 21, 30]

UPDATE_SLA_DATA_ATTRIBUTES_ASSIGNMENT_DEADLINE_DAYS_VALUES: set[UpdateSlaDataAttributesAssignmentDeadlineDays] = {
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


def check_update_sla_data_attributes_assignment_deadline_days(
    value: int,
) -> UpdateSlaDataAttributesAssignmentDeadlineDays:
    if value in UPDATE_SLA_DATA_ATTRIBUTES_ASSIGNMENT_DEADLINE_DAYS_VALUES:
        return cast(UpdateSlaDataAttributesAssignmentDeadlineDays, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_SLA_DATA_ATTRIBUTES_ASSIGNMENT_DEADLINE_DAYS_VALUES!r}"
    )
