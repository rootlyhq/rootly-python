from typing import Literal, cast

NewRoleDataAttributesFormFieldsPermissionsItem = Literal["create", "delete", "read", "update"]

NEW_ROLE_DATA_ATTRIBUTES_FORM_FIELDS_PERMISSIONS_ITEM_VALUES: set[NewRoleDataAttributesFormFieldsPermissionsItem] = {
    "create",
    "delete",
    "read",
    "update",
}


def check_new_role_data_attributes_form_fields_permissions_item(
    value: str | None,
) -> NewRoleDataAttributesFormFieldsPermissionsItem | None:
    if value is None:
        return None
    if value in NEW_ROLE_DATA_ATTRIBUTES_FORM_FIELDS_PERMISSIONS_ITEM_VALUES:
        return cast(NewRoleDataAttributesFormFieldsPermissionsItem, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {NEW_ROLE_DATA_ATTRIBUTES_FORM_FIELDS_PERMISSIONS_ITEM_VALUES!r}"
    )
