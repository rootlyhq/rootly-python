from typing import Literal, cast

UpdateFormFieldDataAttributesInputKind = Literal[
    "checkbox", "date", "datetime", "multi_select", "number", "rich_text", "select", "tags", "text", "textarea"
]

UPDATE_FORM_FIELD_DATA_ATTRIBUTES_INPUT_KIND_VALUES: set[UpdateFormFieldDataAttributesInputKind] = {
    "checkbox",
    "date",
    "datetime",
    "multi_select",
    "number",
    "rich_text",
    "select",
    "tags",
    "text",
    "textarea",
}


def check_update_form_field_data_attributes_input_kind(
    value: str | None,
) -> UpdateFormFieldDataAttributesInputKind | None:
    if value is None:
        return None
    if value in UPDATE_FORM_FIELD_DATA_ATTRIBUTES_INPUT_KIND_VALUES:
        return cast(UpdateFormFieldDataAttributesInputKind, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_FORM_FIELD_DATA_ATTRIBUTES_INPUT_KIND_VALUES!r}"
    )
