from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define

from ..models.update_incident_permission_set_resource_data_attributes_kind import (
    UpdateIncidentPermissionSetResourceDataAttributesKind,
    check_update_incident_permission_set_resource_data_attributes_kind,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.update_incident_permission_set_resource_data_attributes_severity_params import (
        UpdateIncidentPermissionSetResourceDataAttributesSeverityParams,
    )


T = TypeVar("T", bound="UpdateIncidentPermissionSetResourceDataAttributes")


@_attrs_define
class UpdateIncidentPermissionSetResourceDataAttributes:
    """
    Attributes:
        kind (Union[Unset, UpdateIncidentPermissionSetResourceDataAttributesKind]):
        private (Union[Unset, bool]):
        resource_id (Union[Unset, str]):
        resource_type (Union[Unset, str]):
        severity_params (Union[Unset, UpdateIncidentPermissionSetResourceDataAttributesSeverityParams]):
    """

    kind: Unset | UpdateIncidentPermissionSetResourceDataAttributesKind = UNSET
    private: Unset | bool = UNSET
    resource_id: Unset | str = UNSET
    resource_type: Unset | str = UNSET
    severity_params: Union[Unset, "UpdateIncidentPermissionSetResourceDataAttributesSeverityParams"] = UNSET

    def to_dict(self) -> dict[str, Any]:
        kind: Unset | str = UNSET
        if not isinstance(self.kind, Unset):
            kind = self.kind

        private = self.private

        resource_id = self.resource_id

        resource_type = self.resource_type

        severity_params: Unset | dict[str, Any] = UNSET
        if not isinstance(self.severity_params, Unset):
            severity_params = self.severity_params.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if kind is not UNSET:
            field_dict["kind"] = kind
        if private is not UNSET:
            field_dict["private"] = private
        if resource_id is not UNSET:
            field_dict["resource_id"] = resource_id
        if resource_type is not UNSET:
            field_dict["resource_type"] = resource_type
        if severity_params is not UNSET:
            field_dict["severity_params"] = severity_params

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.update_incident_permission_set_resource_data_attributes_severity_params import (
            UpdateIncidentPermissionSetResourceDataAttributesSeverityParams,
        )

        d = dict(src_dict)
        _kind = d.pop("kind", UNSET)
        kind: Unset | UpdateIncidentPermissionSetResourceDataAttributesKind
        if isinstance(_kind, Unset):
            kind = UNSET
        else:
            kind = check_update_incident_permission_set_resource_data_attributes_kind(_kind)

        private = d.pop("private", UNSET)

        resource_id = d.pop("resource_id", UNSET)

        resource_type = d.pop("resource_type", UNSET)

        _severity_params = d.pop("severity_params", UNSET)
        severity_params: Unset | UpdateIncidentPermissionSetResourceDataAttributesSeverityParams
        if isinstance(_severity_params, Unset):
            severity_params = UNSET
        else:
            severity_params = UpdateIncidentPermissionSetResourceDataAttributesSeverityParams.from_dict(
                _severity_params
            )

        update_incident_permission_set_resource_data_attributes = cls(
            kind=kind,
            private=private,
            resource_id=resource_id,
            resource_type=resource_type,
            severity_params=severity_params,
        )

        return update_incident_permission_set_resource_data_attributes
