from typing import Literal, cast

NewFormFieldDataAttributesInputKind = Literal[
    "checkbox", "date", "datetime", "multi_select", "number", "rich_text", "select", "tags", "text", "textarea"
]

NEW_FORM_FIELD_DATA_ATTRIBUTES_INPUT_KIND_VALUES: set[NewFormFieldDataAttributesInputKind] = {
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


def check_new_form_field_data_attributes_input_kind(value: str | None) -> NewFormFieldDataAttributesInputKind | None:
    if value is None:
        return None
    if value in NEW_FORM_FIELD_DATA_ATTRIBUTES_INPUT_KIND_VALUES:
        return cast(NewFormFieldDataAttributesInputKind, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {NEW_FORM_FIELD_DATA_ATTRIBUTES_INPUT_KIND_VALUES!r}")
