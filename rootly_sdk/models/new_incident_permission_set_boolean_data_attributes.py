from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define

from ..models.new_incident_permission_set_boolean_data_attributes_kind import (
    NewIncidentPermissionSetBooleanDataAttributesKind,
    check_new_incident_permission_set_boolean_data_attributes_kind,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.new_incident_permission_set_boolean_data_attributes_severity_params import (
        NewIncidentPermissionSetBooleanDataAttributesSeverityParams,
    )


T = TypeVar("T", bound="NewIncidentPermissionSetBooleanDataAttributes")


@_attrs_define
class NewIncidentPermissionSetBooleanDataAttributes:
    """
    Attributes:
        incident_permission_set_id (str):
        kind (NewIncidentPermissionSetBooleanDataAttributesKind):
        private (Union[Unset, bool]):
        enabled (Union[Unset, bool]):
        severity_params (Union[Unset, NewIncidentPermissionSetBooleanDataAttributesSeverityParams]):
    """

    incident_permission_set_id: str
    kind: NewIncidentPermissionSetBooleanDataAttributesKind
    private: Unset | bool = UNSET
    enabled: Unset | bool = UNSET
    severity_params: Union[Unset, "NewIncidentPermissionSetBooleanDataAttributesSeverityParams"] = UNSET

    def to_dict(self) -> dict[str, Any]:
        incident_permission_set_id = self.incident_permission_set_id

        kind: str = self.kind

        private = self.private

        enabled = self.enabled

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
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if severity_params is not UNSET:
            field_dict["severity_params"] = severity_params

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.new_incident_permission_set_boolean_data_attributes_severity_params import (
            NewIncidentPermissionSetBooleanDataAttributesSeverityParams,
        )

        d = dict(src_dict)
        incident_permission_set_id = d.pop("incident_permission_set_id")

        kind = check_new_incident_permission_set_boolean_data_attributes_kind(d.pop("kind"))

        private = d.pop("private", UNSET)

        enabled = d.pop("enabled", UNSET)

        _severity_params = d.pop("severity_params", UNSET)
        severity_params: Unset | NewIncidentPermissionSetBooleanDataAttributesSeverityParams
        if isinstance(_severity_params, Unset):
            severity_params = UNSET
        else:
            severity_params = NewIncidentPermissionSetBooleanDataAttributesSeverityParams.from_dict(_severity_params)

        new_incident_permission_set_boolean_data_attributes = cls(
            incident_permission_set_id=incident_permission_set_id,
            kind=kind,
            private=private,
            enabled=enabled,
            severity_params=severity_params,
        )

        return new_incident_permission_set_boolean_data_attributes
