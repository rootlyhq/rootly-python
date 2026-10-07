from typing import Literal

NewCommunicationsTemplateDataType = Literal["communications_templates"]

NEW_COMMUNICATIONS_TEMPLATE_DATA_TYPE_VALUES: set[NewCommunicationsTemplateDataType] = {
    "communications_templates",
}


def check_new_communications_template_data_type(value: str | None) -> NewCommunicationsTemplateDataType | None:
    if value is None:
        return None
    if value in NEW_COMMUNICATIONS_TEMPLATE_DATA_TYPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {NEW_COMMUNICATIONS_TEMPLATE_DATA_TYPE_VALUES!r}")
