from typing import Literal, cast

CommunicationsTemplateResponseDataType = Literal["communications_templates"]

COMMUNICATIONS_TEMPLATE_RESPONSE_DATA_TYPE_VALUES: set[CommunicationsTemplateResponseDataType] = {
    "communications_templates",
}


def check_communications_template_response_data_type(value: str | None) -> CommunicationsTemplateResponseDataType | None:
    if value is None:
        return None
    if value in COMMUNICATIONS_TEMPLATE_RESPONSE_DATA_TYPE_VALUES:
        return cast(CommunicationsTemplateResponseDataType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {COMMUNICATIONS_TEMPLATE_RESPONSE_DATA_TYPE_VALUES!r}"
    )
