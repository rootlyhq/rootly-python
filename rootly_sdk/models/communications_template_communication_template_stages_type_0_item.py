from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.communications_template_communication_template_stages_type_0_item_data import (
        CommunicationsTemplateCommunicationTemplateStagesType0ItemData,
    )


T = TypeVar("T", bound="CommunicationsTemplateCommunicationTemplateStagesType0Item")


@_attrs_define
class CommunicationsTemplateCommunicationTemplateStagesType0Item:
    """
    Attributes:
        data (Union[Unset, CommunicationsTemplateCommunicationTemplateStagesType0ItemData]):
    """

    data: Union[Unset, "CommunicationsTemplateCommunicationTemplateStagesType0ItemData"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data: Unset | dict[str, Any] = UNSET
        if not isinstance(self.data, Unset):
            data = self.data.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if data is not UNSET:
            field_dict["data"] = data

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.communications_template_communication_template_stages_type_0_item_data import (
            CommunicationsTemplateCommunicationTemplateStagesType0ItemData,
        )

        d = dict(src_dict)
        _data = d.pop("data", UNSET)
        data: Unset | CommunicationsTemplateCommunicationTemplateStagesType0ItemData
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = CommunicationsTemplateCommunicationTemplateStagesType0ItemData.from_dict(_data)

        communications_template_communication_template_stages_type_0_item = cls(
            data=data,
        )

        communications_template_communication_template_stages_type_0_item.additional_properties = d
        return communications_template_communication_template_stages_type_0_item

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
