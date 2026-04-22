from typing import Literal, cast

SlaEntityType = Literal["follow_up"]

SLA_ENTITY_TYPE_VALUES: set[SlaEntityType] = {
    "follow_up",
}


def check_sla_entity_type(value: str | None) -> SlaEntityType | None:
    if value is None:
        return None
    if value in SLA_ENTITY_TYPE_VALUES:
        return cast(SlaEntityType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {SLA_ENTITY_TYPE_VALUES!r}")
