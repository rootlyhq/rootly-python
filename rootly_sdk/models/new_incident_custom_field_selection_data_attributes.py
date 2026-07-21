from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast


T = TypeVar("T", bound="NewIncidentCustomFieldSelectionDataAttributes")


@_attrs_define
class NewIncidentCustomFieldSelectionDataAttributes:
    """
    Attributes:
        custom_field_id (int): The custom field for this selection
        value (None | str): The selected value for text kind custom fields
        selected_option_ids (list[int] | Unset):
    """

    custom_field_id: int
    value: None | str
    selected_option_ids: list[int] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        custom_field_id = self.custom_field_id

        value: None | str
        value = self.value

        selected_option_ids: list[int] | Unset = UNSET
        if not isinstance(self.selected_option_ids, Unset):
            selected_option_ids = self.selected_option_ids

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "custom_field_id": custom_field_id,
                "value": value,
            }
        )
        if selected_option_ids is not UNSET:
            field_dict["selected_option_ids"] = selected_option_ids

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        custom_field_id = d.pop("custom_field_id")

        def _parse_value(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        value = _parse_value(d.pop("value"))

        selected_option_ids = cast(list[int], d.pop("selected_option_ids", UNSET))

        new_incident_custom_field_selection_data_attributes = cls(
            custom_field_id=custom_field_id,
            value=value,
            selected_option_ids=selected_option_ids,
        )

        return new_incident_custom_field_selection_data_attributes
