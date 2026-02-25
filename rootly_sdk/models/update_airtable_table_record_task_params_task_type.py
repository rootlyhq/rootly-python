from typing import Literal, cast

UpdateAirtableTableRecordTaskParamsTaskType = Literal["update_airtable_table_record"]

UPDATE_AIRTABLE_TABLE_RECORD_TASK_PARAMS_TASK_TYPE_VALUES: set[UpdateAirtableTableRecordTaskParamsTaskType] = {
    "update_airtable_table_record",
}


def check_update_airtable_table_record_task_params_task_type(value: str | None) -> UpdateAirtableTableRecordTaskParamsTaskType | None:
    if value is None:
        return None
    if value in UPDATE_AIRTABLE_TABLE_RECORD_TASK_PARAMS_TASK_TYPE_VALUES:
        return cast(UpdateAirtableTableRecordTaskParamsTaskType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_AIRTABLE_TABLE_RECORD_TASK_PARAMS_TASK_TYPE_VALUES!r}"
    )
