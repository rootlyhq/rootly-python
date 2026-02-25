from typing import Literal, cast

CreateGoogleDocsPermissionsTaskParamsTaskType = Literal["create_google_docs_permissions"]

CREATE_GOOGLE_DOCS_PERMISSIONS_TASK_PARAMS_TASK_TYPE_VALUES: set[CreateGoogleDocsPermissionsTaskParamsTaskType] = {
    "create_google_docs_permissions",
}


def check_create_google_docs_permissions_task_params_task_type(
    value: str | None,
) -> CreateGoogleDocsPermissionsTaskParamsTaskType | None:
    if value is None:
        return None
    if value in CREATE_GOOGLE_DOCS_PERMISSIONS_TASK_PARAMS_TASK_TYPE_VALUES:
        return cast(CreateGoogleDocsPermissionsTaskParamsTaskType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CREATE_GOOGLE_DOCS_PERMISSIONS_TASK_PARAMS_TASK_TYPE_VALUES!r}"
    )
