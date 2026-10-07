from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.update_incident_form_field_selection_data import UpdateIncidentFormFieldSelectionData


T = TypeVar("T", bound="UpdateIncidentFormFieldSelection")


@_attrs_define
class UpdateIncidentFormFieldSelection:
    """
    Attributes:
        data (UpdateIncidentFormFieldSelectionData):
    """

    data: UpdateIncidentFormFieldSelectionData

    def to_dict(self) -> dict[str, Any]:
        data = self.data.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "data": data,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.update_incident_form_field_selection_data import UpdateIncidentFormFieldSelectionData

        d = dict(src_dict)
        data = UpdateIncidentFormFieldSelectionData.from_dict(d.pop("data"))

        update_incident_form_field_selection = cls(
            data=data,
        )

        return update_incident_form_field_selection
