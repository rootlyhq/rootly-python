from typing import Literal, cast

UpdateCommunicationsTemplateDataType = Literal["communications_templates"]

UPDATE_COMMUNICATIONS_TEMPLATE_DATA_TYPE_VALUES: set[UpdateCommunicationsTemplateDataType] = {
    "communications_templates",
}


def check_update_communications_template_data_type(value: str | None) -> UpdateCommunicationsTemplateDataType | None:
    if value is None:
        return None
    if value in UPDATE_COMMUNICATIONS_TEMPLATE_DATA_TYPE_VALUES:
        return cast(UpdateCommunicationsTemplateDataType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {UPDATE_COMMUNICATIONS_TEMPLATE_DATA_TYPE_VALUES!r}")
