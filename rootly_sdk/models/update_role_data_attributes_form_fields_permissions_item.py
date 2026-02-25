from typing import Literal, cast

UpdateRoleDataAttributesFormFieldsPermissionsItem = Literal["create", "delete", "read", "update"]

UPDATE_ROLE_DATA_ATTRIBUTES_FORM_FIELDS_PERMISSIONS_ITEM_VALUES: set[
    UpdateRoleDataAttributesFormFieldsPermissionsItem
] = {
    "create",
    "delete",
    "read",
    "update",
}


def check_update_role_data_attributes_form_fields_permissions_item(
    value: str | None,
) -> UpdateRoleDataAttributesFormFieldsPermissionsItem | None:
    if value is None:
        return None
    if value in UPDATE_ROLE_DATA_ATTRIBUTES_FORM_FIELDS_PERMISSIONS_ITEM_VALUES:
        return cast(UpdateRoleDataAttributesFormFieldsPermissionsItem, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_ROLE_DATA_ATTRIBUTES_FORM_FIELDS_PERMISSIONS_ITEM_VALUES!r}"
    )
