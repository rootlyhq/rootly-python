from typing import Literal, cast

UpdateOnCallRoleDataAttributesEscalationPoliciesPermissionsItem = Literal["create", "delete", "read", "update"]

UPDATE_ON_CALL_ROLE_DATA_ATTRIBUTES_ESCALATION_POLICIES_PERMISSIONS_ITEM_VALUES: set[
    UpdateOnCallRoleDataAttributesEscalationPoliciesPermissionsItem
] = {
    "create",
    "delete",
    "read",
    "update",
}


def check_update_on_call_role_data_attributes_escalation_policies_permissions_item(
    value: str | None,
) -> UpdateOnCallRoleDataAttributesEscalationPoliciesPermissionsItem | None:
    if value is None:
        return None
    if value in UPDATE_ON_CALL_ROLE_DATA_ATTRIBUTES_ESCALATION_POLICIES_PERMISSIONS_ITEM_VALUES:
        return cast(UpdateOnCallRoleDataAttributesEscalationPoliciesPermissionsItem, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_ON_CALL_ROLE_DATA_ATTRIBUTES_ESCALATION_POLICIES_PERMISSIONS_ITEM_VALUES!r}"
    )
