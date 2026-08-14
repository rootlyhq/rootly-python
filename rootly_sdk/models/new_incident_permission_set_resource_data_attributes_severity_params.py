from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="NewIncidentPermissionSetResourceDataAttributesSeverityParams")


@_attrs_define
class NewIncidentPermissionSetResourceDataAttributesSeverityParams:
    """
    Attributes:
        fully_enabled (Union[Unset, bool]): Whether permissions are enabled for any severity incident Default: True.
        create_enabled (Union[Unset, bool]): Whether permissions are enabled when creating incident Default: False.
        applies_to_unassigned (Union[Unset, bool]): Whether permissions are enabled for incident without severity
            Default: True.
        severity_ids (Union[None, Unset, list[str]]): Severity ids that determine if an incident is permitted based on
            matching severity
    """

    fully_enabled: Unset | bool = True
    create_enabled: Unset | bool = False
    applies_to_unassigned: Unset | bool = True
    severity_ids: None | Unset | list[str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        fully_enabled = self.fully_enabled

        create_enabled = self.create_enabled

        applies_to_unassigned = self.applies_to_unassigned

        severity_ids: None | Unset | list[str]
        if isinstance(self.severity_ids, Unset):
            severity_ids = UNSET
        elif isinstance(self.severity_ids, list):
            severity_ids = self.severity_ids

        else:
            severity_ids = self.severity_ids

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if fully_enabled is not UNSET:
            field_dict["fully_enabled"] = fully_enabled
        if create_enabled is not UNSET:
            field_dict["create_enabled"] = create_enabled
        if applies_to_unassigned is not UNSET:
            field_dict["applies_to_unassigned"] = applies_to_unassigned
        if severity_ids is not UNSET:
            field_dict["severity_ids"] = severity_ids

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        fully_enabled = d.pop("fully_enabled", UNSET)

        create_enabled = d.pop("create_enabled", UNSET)

        applies_to_unassigned = d.pop("applies_to_unassigned", UNSET)

        def _parse_severity_ids(data: object) -> None | Unset | list[str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                severity_ids_type_0 = cast(list[str], data)

                return severity_ids_type_0
            except:  # noqa: E722
                pass
            return cast(None | Unset | list[str], data)

        severity_ids = _parse_severity_ids(d.pop("severity_ids", UNSET))

        new_incident_permission_set_resource_data_attributes_severity_params = cls(
            fully_enabled=fully_enabled,
            create_enabled=create_enabled,
            applies_to_unassigned=applies_to_unassigned,
            severity_ids=severity_ids,
        )

        new_incident_permission_set_resource_data_attributes_severity_params.additional_properties = d
        return new_incident_permission_set_resource_data_attributes_severity_params

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
