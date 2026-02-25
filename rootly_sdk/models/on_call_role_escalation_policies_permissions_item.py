from typing import Literal, cast

OnCallRoleEscalationPoliciesPermissionsItem = Literal["create", "delete", "read", "update"]

ON_CALL_ROLE_ESCALATION_POLICIES_PERMISSIONS_ITEM_VALUES: set[OnCallRoleEscalationPoliciesPermissionsItem] = {
    "create",
    "delete",
    "read",
    "update",
}


def check_on_call_role_escalation_policies_permissions_item(
    value: str | None,
) -> OnCallRoleEscalationPoliciesPermissionsItem | None:
    if value is None:
        return None
    if value in ON_CALL_ROLE_ESCALATION_POLICIES_PERMISSIONS_ITEM_VALUES:
        return cast(OnCallRoleEscalationPoliciesPermissionsItem, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ON_CALL_ROLE_ESCALATION_POLICIES_PERMISSIONS_ITEM_VALUES!r}"
    )
