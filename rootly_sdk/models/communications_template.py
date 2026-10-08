from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.communications_template_communication_template_stages_type_0_item import (
        CommunicationsTemplateCommunicationTemplateStagesType0Item,
    )
    from ..models.communications_template_communication_type import CommunicationsTemplateCommunicationType


T = TypeVar("T", bound="CommunicationsTemplate")


@_attrs_define
class CommunicationsTemplate:
    """
    Attributes:
        name (str): The name of the communications template
        position (int | None): Position of the communications template
        created_at (str): Date of creation
        updated_at (str): Date of last update
        slug (str | Unset): The slug of the communications template
        description (None | str | Unset): The description of the communications template
        communication_type_id (str | Unset): The communication type ID
        communication_template_stages (list[CommunicationsTemplateCommunicationTemplateStagesType0Item] | None | Unset):
            Communication template stages
        communication_type (CommunicationsTemplateCommunicationType | Unset):
    """

    name: str
    position: int | None
    created_at: str
    updated_at: str
    slug: str | Unset = UNSET
    description: None | str | Unset = UNSET
    communication_type_id: str | Unset = UNSET
    communication_template_stages: list[CommunicationsTemplateCommunicationTemplateStagesType0Item] | None | Unset = (
        UNSET
    )
    communication_type: CommunicationsTemplateCommunicationType | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        position: int | None
        position = self.position

        created_at = self.created_at

        updated_at = self.updated_at

        slug = self.slug

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        communication_type_id = self.communication_type_id

        communication_template_stages: list[dict[str, Any]] | None | Unset
        if isinstance(self.communication_template_stages, Unset):
            communication_template_stages = UNSET
        elif isinstance(self.communication_template_stages, list):
            communication_template_stages = []
            for communication_template_stages_type_0_item_data in self.communication_template_stages:
                communication_template_stages_type_0_item = communication_template_stages_type_0_item_data.to_dict()
                communication_template_stages.append(communication_template_stages_type_0_item)

        else:
            communication_template_stages = self.communication_template_stages

        communication_type: dict[str, Any] | Unset = UNSET
        if not isinstance(self.communication_type, Unset):
            communication_type = self.communication_type.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "position": position,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if slug is not UNSET:
            field_dict["slug"] = slug
        if description is not UNSET:
            field_dict["description"] = description
        if communication_type_id is not UNSET:
            field_dict["communication_type_id"] = communication_type_id
        if communication_template_stages is not UNSET:
            field_dict["communication_template_stages"] = communication_template_stages
        if communication_type is not UNSET:
            field_dict["communication_type"] = communication_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.communications_template_communication_template_stages_type_0_item import (
            CommunicationsTemplateCommunicationTemplateStagesType0Item,
        )
        from ..models.communications_template_communication_type import CommunicationsTemplateCommunicationType

        d = dict(src_dict)
        name = d.pop("name")

        def _parse_position(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        position = _parse_position(d.pop("position"))

        created_at = d.pop("created_at")

        updated_at = d.pop("updated_at")

        slug = d.pop("slug", UNSET)

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        communication_type_id = d.pop("communication_type_id", UNSET)

        def _parse_communication_template_stages(
            data: object,
        ) -> list[CommunicationsTemplateCommunicationTemplateStagesType0Item] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                communication_template_stages_type_0 = []
                _communication_template_stages_type_0 = data
                for communication_template_stages_type_0_item_data in _communication_template_stages_type_0:
                    communication_template_stages_type_0_item = (
                        CommunicationsTemplateCommunicationTemplateStagesType0Item.from_dict(
                            communication_template_stages_type_0_item_data
                        )
                    )

                    communication_template_stages_type_0.append(communication_template_stages_type_0_item)

                return communication_template_stages_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[CommunicationsTemplateCommunicationTemplateStagesType0Item] | None | Unset, data)

        communication_template_stages = _parse_communication_template_stages(
            d.pop("communication_template_stages", UNSET)
        )

        _communication_type = d.pop("communication_type", UNSET)
        communication_type: CommunicationsTemplateCommunicationType | Unset
        if isinstance(_communication_type, Unset):
            communication_type = UNSET
        else:
            communication_type = CommunicationsTemplateCommunicationType.from_dict(_communication_type)

        communications_template = cls(
            name=name,
            position=position,
            created_at=created_at,
            updated_at=updated_at,
            slug=slug,
            description=description,
            communication_type_id=communication_type_id,
            communication_template_stages=communication_template_stages,
            communication_type=communication_type,
        )

        communications_template.additional_properties = d
        return communications_template

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
