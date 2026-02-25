from typing import Literal, cast

FormFieldInputKind = Literal[
    "checkbox", "date", "datetime", "multi_select", "number", "rich_text", "select", "tags", "text", "textarea"
]

FORM_FIELD_INPUT_KIND_VALUES: set[FormFieldInputKind] = {
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


def check_form_field_input_kind(value: str | None) -> FormFieldInputKind | None:
    if value is None:
        return None
    if value in FORM_FIELD_INPUT_KIND_VALUES:
        return cast(FormFieldInputKind, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {FORM_FIELD_INPUT_KIND_VALUES!r}")
