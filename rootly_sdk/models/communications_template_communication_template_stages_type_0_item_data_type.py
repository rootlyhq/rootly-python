from typing import Literal, cast

CommunicationsTemplateCommunicationTemplateStagesType0ItemDataType = Literal["communications_template_stages"]

COMMUNICATIONS_TEMPLATE_COMMUNICATION_TEMPLATE_STAGES_TYPE_0_ITEM_DATA_TYPE_VALUES: set[
    CommunicationsTemplateCommunicationTemplateStagesType0ItemDataType
] = {
    "communications_template_stages",
}


def check_communications_template_communication_template_stages_type_0_item_data_type(
    value: str | None,
) -> CommunicationsTemplateCommunicationTemplateStagesType0ItemDataType | None:
    if value is None:
        return None
    if value in COMMUNICATIONS_TEMPLATE_COMMUNICATION_TEMPLATE_STAGES_TYPE_0_ITEM_DATA_TYPE_VALUES:
        return cast(CommunicationsTemplateCommunicationTemplateStagesType0ItemDataType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {COMMUNICATIONS_TEMPLATE_COMMUNICATION_TEMPLATE_STAGES_TYPE_0_ITEM_DATA_TYPE_VALUES!r}"
    )
