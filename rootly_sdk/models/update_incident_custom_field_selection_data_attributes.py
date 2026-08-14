from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateIncidentCustomFieldSelectionDataAttributes")


@_attrs_define
class UpdateIncidentCustomFieldSelectionDataAttributes:
    """
    Attributes:
        value (Union[None, Unset, str]): The selected value for text kind custom fields
        selected_option_ids (Union[Unset, list[int]]):
    """

    value: None | Unset | str = UNSET
    selected_option_ids: Unset | list[int] = UNSET

    def to_dict(self) -> dict[str, Any]:
        value: None | Unset | str
        if isinstance(self.value, Unset):
            value = UNSET
        else:
            value = self.value

        selected_option_ids: Unset | list[int] = UNSET
        if not isinstance(self.selected_option_ids, Unset):
            selected_option_ids = self.selected_option_ids

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if value is not UNSET:
            field_dict["value"] = value
        if selected_option_ids is not UNSET:
            field_dict["selected_option_ids"] = selected_option_ids

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_value(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        value = _parse_value(d.pop("value", UNSET))

        selected_option_ids = cast(list[int], d.pop("selected_option_ids", UNSET))

        update_incident_custom_field_selection_data_attributes = cls(
            value=value,
            selected_option_ids=selected_option_ids,
        )

        return update_incident_custom_field_selection_data_attributes
