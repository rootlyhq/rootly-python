from typing import Literal, cast

UpdateOnCallRoleDataAttributesOnCallReadinessReportPermissionsItem = Literal["read"]

UPDATE_ON_CALL_ROLE_DATA_ATTRIBUTES_ON_CALL_READINESS_REPORT_PERMISSIONS_ITEM_VALUES: set[
    UpdateOnCallRoleDataAttributesOnCallReadinessReportPermissionsItem
] = {
    "read",
}


def check_update_on_call_role_data_attributes_on_call_readiness_report_permissions_item(
    value: str | None,
) -> UpdateOnCallRoleDataAttributesOnCallReadinessReportPermissionsItem | None:
    if value is None:
        return None
    if value in UPDATE_ON_CALL_ROLE_DATA_ATTRIBUTES_ON_CALL_READINESS_REPORT_PERMISSIONS_ITEM_VALUES:
        return cast(UpdateOnCallRoleDataAttributesOnCallReadinessReportPermissionsItem, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_ON_CALL_ROLE_DATA_ATTRIBUTES_ON_CALL_READINESS_REPORT_PERMISSIONS_ITEM_VALUES!r}"
    )
