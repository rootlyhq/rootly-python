from typing import Literal, cast

OnCallRoleOnCallReadinessReportPermissionsItem = Literal["read"]

ON_CALL_ROLE_ON_CALL_READINESS_REPORT_PERMISSIONS_ITEM_VALUES: set[OnCallRoleOnCallReadinessReportPermissionsItem] = {
    "read",
}


def check_on_call_role_on_call_readiness_report_permissions_item(
    value: str,
) -> OnCallRoleOnCallReadinessReportPermissionsItem:
    if value in ON_CALL_ROLE_ON_CALL_READINESS_REPORT_PERMISSIONS_ITEM_VALUES:
        return cast(OnCallRoleOnCallReadinessReportPermissionsItem, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ON_CALL_ROLE_ON_CALL_READINESS_REPORT_PERMISSIONS_ITEM_VALUES!r}"
    )
