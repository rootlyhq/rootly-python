from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define

from ..models.new_incident_permission_set_resource_data_attributes_kind import (
    NewIncidentPermissionSetResourceDataAttributesKind,
    check_new_incident_permission_set_resource_data_attributes_kind,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.new_incident_permission_set_resource_data_attributes_severity_params import (
        NewIncidentPermissionSetResourceDataAttributesSeverityParams,
    )


T = TypeVar("T", bound="NewIncidentPermissionSetResourceDataAttributes")


@_attrs_define
class NewIncidentPermissionSetResourceDataAttributes:
    """
    Attributes:
        incident_permission_set_id (str):
        kind (NewIncidentPermissionSetResourceDataAttributesKind):
        private (Union[Unset, bool]):
        resource_id (Union[Unset, str]):
        resource_type (Union[Unset, str]):
        severity_params (Union[Unset, NewIncidentPermissionSetResourceDataAttributesSeverityParams]):
    """

    incident_permission_set_id: str
    kind: NewIncidentPermissionSetResourceDataAttributesKind
    private: Unset | bool = UNSET
    resource_id: Unset | str = UNSET
    resource_type: Unset | str = UNSET
    severity_params: Union[Unset, "NewIncidentPermissionSetResourceDataAttributesSeverityParams"] = UNSET

    def to_dict(self) -> dict[str, Any]:
        incident_permission_set_id = self.incident_permission_set_id

        kind: str = self.kind

        private = self.private

        resource_id = self.resource_id

        resource_type = self.resource_type

        severity_params: Unset | dict[str, Any] = UNSET
        if not isinstance(self.severity_params, Unset):
            severity_params = self.severity_params.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "incident_permission_set_id": incident_permission_set_id,
                "kind": kind,
            }
        )
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
        from ..models.new_incident_permission_set_resource_data_attributes_severity_params import (
            NewIncidentPermissionSetResourceDataAttributesSeverityParams,
        )

        d = dict(src_dict)
        incident_permission_set_id = d.pop("incident_permission_set_id")

        kind = check_new_incident_permission_set_resource_data_attributes_kind(d.pop("kind"))

        private = d.pop("private", UNSET)

        resource_id = d.pop("resource_id", UNSET)

        resource_type = d.pop("resource_type", UNSET)

        _severity_params = d.pop("severity_params", UNSET)
        severity_params: Unset | NewIncidentPermissionSetResourceDataAttributesSeverityParams
        if isinstance(_severity_params, Unset):
            severity_params = UNSET
        else:
            severity_params = NewIncidentPermissionSetResourceDataAttributesSeverityParams.from_dict(_severity_params)

        new_incident_permission_set_resource_data_attributes = cls(
            incident_permission_set_id=incident_permission_set_id,
            kind=kind,
            private=private,
            resource_id=resource_id,
            resource_type=resource_type,
            severity_params=severity_params,
        )

        return new_incident_permission_set_resource_data_attributes
