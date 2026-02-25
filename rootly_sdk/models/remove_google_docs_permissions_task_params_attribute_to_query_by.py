from typing import Literal, cast

RemoveGoogleDocsPermissionsTaskParamsAttributeToQueryBy = Literal["email_address", "role", "type"]

REMOVE_GOOGLE_DOCS_PERMISSIONS_TASK_PARAMS_ATTRIBUTE_TO_QUERY_BY_VALUES: set[
    RemoveGoogleDocsPermissionsTaskParamsAttributeToQueryBy
] = {
    "email_address",
    "role",
    "type",
}


def check_remove_google_docs_permissions_task_params_attribute_to_query_by(
    value: str | None,
) -> RemoveGoogleDocsPermissionsTaskParamsAttributeToQueryBy | None:
    if value is None:
        return None
    if value in REMOVE_GOOGLE_DOCS_PERMISSIONS_TASK_PARAMS_ATTRIBUTE_TO_QUERY_BY_VALUES:
        return cast(RemoveGoogleDocsPermissionsTaskParamsAttributeToQueryBy, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {REMOVE_GOOGLE_DOCS_PERMISSIONS_TASK_PARAMS_ATTRIBUTE_TO_QUERY_BY_VALUES!r}"
    )
