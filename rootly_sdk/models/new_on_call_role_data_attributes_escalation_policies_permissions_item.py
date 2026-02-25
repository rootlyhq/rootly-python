from typing import Literal, cast

NewOnCallRoleDataAttributesEscalationPoliciesPermissionsItem = Literal["create", "delete", "read", "update"]

NEW_ON_CALL_ROLE_DATA_ATTRIBUTES_ESCALATION_POLICIES_PERMISSIONS_ITEM_VALUES: set[
    NewOnCallRoleDataAttributesEscalationPoliciesPermissionsItem
] = {
    "create",
    "delete",
    "read",
    "update",
}


def check_new_on_call_role_data_attributes_escalation_policies_permissions_item(
    value: str | None,
) -> NewOnCallRoleDataAttributesEscalationPoliciesPermissionsItem | None:
    if value is None:
        return None
    if value in NEW_ON_CALL_ROLE_DATA_ATTRIBUTES_ESCALATION_POLICIES_PERMISSIONS_ITEM_VALUES:
        return cast(NewOnCallRoleDataAttributesEscalationPoliciesPermissionsItem, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {NEW_ON_CALL_ROLE_DATA_ATTRIBUTES_ESCALATION_POLICIES_PERMISSIONS_ITEM_VALUES!r}"
    )
