from typing import Literal, cast

TiptapBlockSchemaFollowupComponentDataSort = Literal["due_date", "priority", "status"]

TIPTAP_BLOCK_SCHEMA_FOLLOWUP_COMPONENT_DATA_SORT_VALUES: set[TiptapBlockSchemaFollowupComponentDataSort] = {
    "due_date",
    "priority",
    "status",
}


def check_tiptap_block_schema_followup_component_data_sort(
    value: str | None,
) -> TiptapBlockSchemaFollowupComponentDataSort | None:
    if value is None:
        return None
    if value in TIPTAP_BLOCK_SCHEMA_FOLLOWUP_COMPONENT_DATA_SORT_VALUES:
        return cast(TiptapBlockSchemaFollowupComponentDataSort, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {TIPTAP_BLOCK_SCHEMA_FOLLOWUP_COMPONENT_DATA_SORT_VALUES!r}"
    )
