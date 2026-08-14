from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_google_docs_permissions_task_params_task_type import (
    CreateGoogleDocsPermissionsTaskParamsTaskType,
    check_create_google_docs_permissions_task_params_task_type,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateGoogleDocsPermissionsTaskParams")


@_attrs_define
class CreateGoogleDocsPermissionsTaskParams:
    """
    Attributes:
        file_id (str): The Google Doc file ID
        permissions (str): Page permissions JSON
        task_type (Union[Unset, CreateGoogleDocsPermissionsTaskParamsTaskType]):
        send_notification_email (Union[Unset, bool]):
        email_message (Union[None, Unset, str]): Email message notification
    """

    file_id: str
    permissions: str
    task_type: Unset | CreateGoogleDocsPermissionsTaskParamsTaskType = UNSET
    send_notification_email: Unset | bool = UNSET
    email_message: None | Unset | str = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        file_id = self.file_id

        permissions = self.permissions

        task_type: Unset | str = UNSET
        if not isinstance(self.task_type, Unset):
            task_type = self.task_type

        send_notification_email = self.send_notification_email

        email_message: None | Unset | str
        if isinstance(self.email_message, Unset):
            email_message = UNSET
        else:
            email_message = self.email_message

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "file_id": file_id,
                "permissions": permissions,
            }
        )
        if task_type is not UNSET:
            field_dict["task_type"] = task_type
        if send_notification_email is not UNSET:
            field_dict["send_notification_email"] = send_notification_email
        if email_message is not UNSET:
            field_dict["email_message"] = email_message

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        file_id = d.pop("file_id")

        permissions = d.pop("permissions")

        _task_type = d.pop("task_type", UNSET)
        task_type: Unset | CreateGoogleDocsPermissionsTaskParamsTaskType
        if isinstance(_task_type, Unset):
            task_type = UNSET
        else:
            task_type = check_create_google_docs_permissions_task_params_task_type(_task_type)

        send_notification_email = d.pop("send_notification_email", UNSET)

        def _parse_email_message(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        email_message = _parse_email_message(d.pop("email_message", UNSET))

        create_google_docs_permissions_task_params = cls(
            file_id=file_id,
            permissions=permissions,
            task_type=task_type,
            send_notification_email=send_notification_email,
            email_message=email_message,
        )

        create_google_docs_permissions_task_params.additional_properties = d
        return create_google_docs_permissions_task_params

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
