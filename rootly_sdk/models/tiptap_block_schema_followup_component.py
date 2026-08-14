from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.tiptap_block_schema_followup_component_data_sort import (
    TiptapBlockSchemaFollowupComponentDataSort,
    check_tiptap_block_schema_followup_component_data_sort,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="TiptapBlockSchemaFollowupComponent")


@_attrs_define
class TiptapBlockSchemaFollowupComponent:
    """Followup component block

    Attributes:
        html (str): HTML representation: <div data-sort="due_date" data-followup-component="true" class="followups-node-
            placeholder"></div> Example: <div data-sort="due_date" data-followup-component="true" class="followups-node-
            placeholder"></div>.
        data_sort (Union[Unset, TiptapBlockSchemaFollowupComponentDataSort]): Sort order for followups. Valid values:
            due_date, status, priority Default: 'due_date'.
    """

    html: str
    data_sort: Unset | TiptapBlockSchemaFollowupComponentDataSort = "due_date"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        html = self.html

        data_sort: Unset | str = UNSET
        if not isinstance(self.data_sort, Unset):
            data_sort = self.data_sort

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "html": html,
            }
        )
        if data_sort is not UNSET:
            field_dict["data_sort"] = data_sort

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        html = d.pop("html")

        _data_sort = d.pop("data_sort", UNSET)
        data_sort: Unset | TiptapBlockSchemaFollowupComponentDataSort
        if isinstance(_data_sort, Unset):
            data_sort = UNSET
        else:
            data_sort = check_tiptap_block_schema_followup_component_data_sort(_data_sort)

        tiptap_block_schema_followup_component = cls(
            html=html,
            data_sort=data_sort,
        )

        tiptap_block_schema_followup_component.additional_properties = d
        return tiptap_block_schema_followup_component

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
