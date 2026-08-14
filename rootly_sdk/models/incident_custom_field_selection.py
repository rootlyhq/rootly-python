from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="IncidentCustomFieldSelection")


@_attrs_define
class IncidentCustomFieldSelection:
    """
    Attributes:
        value (Union[None, str]): The value of the incident_custom_field_selection
        selected_option_ids (list[int]):
        incident_id (Union[Unset, str]):
        custom_field_id (Union[Unset, int]):
    """

    value: None | str
    selected_option_ids: list[int]
    incident_id: Unset | str = UNSET
    custom_field_id: Unset | int = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        value: None | str
        value = self.value

        selected_option_ids = self.selected_option_ids

        incident_id = self.incident_id

        custom_field_id = self.custom_field_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "value": value,
                "selected_option_ids": selected_option_ids,
            }
        )
        if incident_id is not UNSET:
            field_dict["incident_id"] = incident_id
        if custom_field_id is not UNSET:
            field_dict["custom_field_id"] = custom_field_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_value(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        value = _parse_value(d.pop("value"))

        selected_option_ids = cast(list[int], d.pop("selected_option_ids"))

        incident_id = d.pop("incident_id", UNSET)

        custom_field_id = d.pop("custom_field_id", UNSET)

        incident_custom_field_selection = cls(
            value=value,
            selected_option_ids=selected_option_ids,
            incident_id=incident_id,
            custom_field_id=custom_field_id,
        )

        incident_custom_field_selection.additional_properties = d
        return incident_custom_field_selection

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
