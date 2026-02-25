from typing import Literal, cast

RemoveGoogleDocsPermissionsTaskParamsTaskType = Literal["remove_google_docs_permissions"]

REMOVE_GOOGLE_DOCS_PERMISSIONS_TASK_PARAMS_TASK_TYPE_VALUES: set[RemoveGoogleDocsPermissionsTaskParamsTaskType] = {
    "remove_google_docs_permissions",
}


def check_remove_google_docs_permissions_task_params_task_type(
    value: str | None,
) -> RemoveGoogleDocsPermissionsTaskParamsTaskType | None:
    if value is None:
        return None
    if value in REMOVE_GOOGLE_DOCS_PERMISSIONS_TASK_PARAMS_TASK_TYPE_VALUES:
        return cast(RemoveGoogleDocsPermissionsTaskParamsTaskType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {REMOVE_GOOGLE_DOCS_PERMISSIONS_TASK_PARAMS_TASK_TYPE_VALUES!r}"
    )
