from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.remove_google_docs_permissions_task_params_attribute_to_query_by import (
    RemoveGoogleDocsPermissionsTaskParamsAttributeToQueryBy,
    check_remove_google_docs_permissions_task_params_attribute_to_query_by,
)
from ..models.remove_google_docs_permissions_task_params_task_type import (
    RemoveGoogleDocsPermissionsTaskParamsTaskType,
    check_remove_google_docs_permissions_task_params_task_type,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="RemoveGoogleDocsPermissionsTaskParams")


@_attrs_define
class RemoveGoogleDocsPermissionsTaskParams:
    """
    Attributes:
        file_id (str): The Google Doc file ID
        attribute_to_query_by (RemoveGoogleDocsPermissionsTaskParamsAttributeToQueryBy):  Default: 'email_address'.
        value (str):
        task_type (Union[Unset, RemoveGoogleDocsPermissionsTaskParamsTaskType]):
    """

    file_id: str
    value: str
    attribute_to_query_by: RemoveGoogleDocsPermissionsTaskParamsAttributeToQueryBy = "email_address"
    task_type: Unset | RemoveGoogleDocsPermissionsTaskParamsTaskType = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        file_id = self.file_id

        attribute_to_query_by: str = self.attribute_to_query_by

        value = self.value

        task_type: Unset | str = UNSET
        if not isinstance(self.task_type, Unset):
            task_type = self.task_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "file_id": file_id,
                "attribute_to_query_by": attribute_to_query_by,
                "value": value,
            }
        )
        if task_type is not UNSET:
            field_dict["task_type"] = task_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        file_id = d.pop("file_id")

        attribute_to_query_by = check_remove_google_docs_permissions_task_params_attribute_to_query_by(
            d.pop("attribute_to_query_by")
        )

        value = d.pop("value")

        _task_type = d.pop("task_type", UNSET)
        task_type: Unset | RemoveGoogleDocsPermissionsTaskParamsTaskType
        if isinstance(_task_type, Unset):
            task_type = UNSET
        else:
            task_type = check_remove_google_docs_permissions_task_params_task_type(_task_type)

        remove_google_docs_permissions_task_params = cls(
            file_id=file_id,
            attribute_to_query_by=attribute_to_query_by,
            value=value,
            task_type=task_type,
        )

        remove_google_docs_permissions_task_params.additional_properties = d
        return remove_google_docs_permissions_task_params

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
