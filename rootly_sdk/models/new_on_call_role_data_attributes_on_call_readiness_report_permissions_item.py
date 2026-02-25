from typing import Literal, cast

NewOnCallRoleDataAttributesOnCallReadinessReportPermissionsItem = Literal["read"]

NEW_ON_CALL_ROLE_DATA_ATTRIBUTES_ON_CALL_READINESS_REPORT_PERMISSIONS_ITEM_VALUES: set[
    NewOnCallRoleDataAttributesOnCallReadinessReportPermissionsItem
] = {
    "read",
}


def check_new_on_call_role_data_attributes_on_call_readiness_report_permissions_item(
    value: str | None,
) -> NewOnCallRoleDataAttributesOnCallReadinessReportPermissionsItem | None:
    if value is None:
        return None
    if value in NEW_ON_CALL_ROLE_DATA_ATTRIBUTES_ON_CALL_READINESS_REPORT_PERMISSIONS_ITEM_VALUES:
        return cast(NewOnCallRoleDataAttributesOnCallReadinessReportPermissionsItem, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {NEW_ON_CALL_ROLE_DATA_ATTRIBUTES_ON_CALL_READINESS_REPORT_PERMISSIONS_ITEM_VALUES!r}"
    )
