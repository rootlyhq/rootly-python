from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define

from ..models.update_incident_permission_set_boolean_data_attributes_kind import (
    UpdateIncidentPermissionSetBooleanDataAttributesKind,
    check_update_incident_permission_set_boolean_data_attributes_kind,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.update_incident_permission_set_boolean_data_attributes_severity_params import (
        UpdateIncidentPermissionSetBooleanDataAttributesSeverityParams,
    )


T = TypeVar("T", bound="UpdateIncidentPermissionSetBooleanDataAttributes")


@_attrs_define
class UpdateIncidentPermissionSetBooleanDataAttributes:
    """
    Attributes:
        kind (Union[Unset, UpdateIncidentPermissionSetBooleanDataAttributesKind]):
        private (Union[Unset, bool]):
        enabled (Union[Unset, bool]):
        severity_params (Union[Unset, UpdateIncidentPermissionSetBooleanDataAttributesSeverityParams]):
    """

    kind: Unset | UpdateIncidentPermissionSetBooleanDataAttributesKind = UNSET
    private: Unset | bool = UNSET
    enabled: Unset | bool = UNSET
    severity_params: Union[Unset, "UpdateIncidentPermissionSetBooleanDataAttributesSeverityParams"] = UNSET

    def to_dict(self) -> dict[str, Any]:
        kind: Unset | str = UNSET
        if not isinstance(self.kind, Unset):
            kind = self.kind

        private = self.private

        enabled = self.enabled

        severity_params: Unset | dict[str, Any] = UNSET
        if not isinstance(self.severity_params, Unset):
            severity_params = self.severity_params.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if kind is not UNSET:
            field_dict["kind"] = kind
        if private is not UNSET:
            field_dict["private"] = private
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if severity_params is not UNSET:
            field_dict["severity_params"] = severity_params

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.update_incident_permission_set_boolean_data_attributes_severity_params import (
            UpdateIncidentPermissionSetBooleanDataAttributesSeverityParams,
        )

        d = dict(src_dict)
        _kind = d.pop("kind", UNSET)
        kind: Unset | UpdateIncidentPermissionSetBooleanDataAttributesKind
        if isinstance(_kind, Unset):
            kind = UNSET
        else:
            kind = check_update_incident_permission_set_boolean_data_attributes_kind(_kind)

        private = d.pop("private", UNSET)

        enabled = d.pop("enabled", UNSET)

        _severity_params = d.pop("severity_params", UNSET)
        severity_params: Unset | UpdateIncidentPermissionSetBooleanDataAttributesSeverityParams
        if isinstance(_severity_params, Unset):
            severity_params = UNSET
        else:
            severity_params = UpdateIncidentPermissionSetBooleanDataAttributesSeverityParams.from_dict(_severity_params)

        update_incident_permission_set_boolean_data_attributes = cls(
            kind=kind,
            private=private,
            enabled=enabled,
            severity_params=severity_params,
        )

        return update_incident_permission_set_boolean_data_attributes
