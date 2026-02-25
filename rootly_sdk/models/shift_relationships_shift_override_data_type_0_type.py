from typing import Literal, cast

ShiftRelationshipsShiftOverrideDataType0Type = Literal["shift_overrides"]

SHIFT_RELATIONSHIPS_SHIFT_OVERRIDE_DATA_TYPE_0_TYPE_VALUES: set[ShiftRelationshipsShiftOverrideDataType0Type] = {
    "shift_overrides",
}


def check_shift_relationships_shift_override_data_type_0_type(
    value: str | None,
) -> ShiftRelationshipsShiftOverrideDataType0Type | None:
    if value is None:
        return None
    if value in SHIFT_RELATIONSHIPS_SHIFT_OVERRIDE_DATA_TYPE_0_TYPE_VALUES:
        return cast(ShiftRelationshipsShiftOverrideDataType0Type, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {SHIFT_RELATIONSHIPS_SHIFT_OVERRIDE_DATA_TYPE_0_TYPE_VALUES!r}"
    )
