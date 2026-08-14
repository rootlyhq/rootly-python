from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.tiptap_block_schema_followup_component import TiptapBlockSchemaFollowupComponent
    from ..models.tiptap_block_schema_timeline_component import TiptapBlockSchemaTimelineComponent


T = TypeVar("T", bound="TiptapBlockSchema")


@_attrs_define
class TiptapBlockSchema:
    """TipTap block component schema for post mortem templates

    Attributes:
        followup_component (Union[Unset, TiptapBlockSchemaFollowupComponent]): Followup component block
        timeline_component (Union[Unset, TiptapBlockSchemaTimelineComponent]): Timeline component block
    """

    followup_component: Union[Unset, "TiptapBlockSchemaFollowupComponent"] = UNSET
    timeline_component: Union[Unset, "TiptapBlockSchemaTimelineComponent"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        followup_component: Unset | dict[str, Any] = UNSET
        if not isinstance(self.followup_component, Unset):
            followup_component = self.followup_component.to_dict()

        timeline_component: Unset | dict[str, Any] = UNSET
        if not isinstance(self.timeline_component, Unset):
            timeline_component = self.timeline_component.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if followup_component is not UNSET:
            field_dict["followup_component"] = followup_component
        if timeline_component is not UNSET:
            field_dict["timeline_component"] = timeline_component

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.tiptap_block_schema_followup_component import TiptapBlockSchemaFollowupComponent
        from ..models.tiptap_block_schema_timeline_component import TiptapBlockSchemaTimelineComponent

        d = dict(src_dict)
        _followup_component = d.pop("followup_component", UNSET)
        followup_component: Unset | TiptapBlockSchemaFollowupComponent
        if isinstance(_followup_component, Unset):
            followup_component = UNSET
        else:
            followup_component = TiptapBlockSchemaFollowupComponent.from_dict(_followup_component)

        _timeline_component = d.pop("timeline_component", UNSET)
        timeline_component: Unset | TiptapBlockSchemaTimelineComponent
        if isinstance(_timeline_component, Unset):
            timeline_component = UNSET
        else:
            timeline_component = TiptapBlockSchemaTimelineComponent.from_dict(_timeline_component)

        tiptap_block_schema = cls(
            followup_component=followup_component,
            timeline_component=timeline_component,
        )

        tiptap_block_schema.additional_properties = d
        return tiptap_block_schema

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
