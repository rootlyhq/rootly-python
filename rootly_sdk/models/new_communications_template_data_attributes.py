from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.new_communications_template_data_attributes_communication_template_stages_attributes_type_0_item import (
        NewCommunicationsTemplateDataAttributesCommunicationTemplateStagesAttributesType0Item,
    )


T = TypeVar("T", bound="NewCommunicationsTemplateDataAttributes")


@_attrs_define
class NewCommunicationsTemplateDataAttributes:
    """
    Attributes:
        name (str): The name of the communications template
        communication_type_id (str): The communication type ID
        description (None | str | Unset): The description of the communications template
        position (int | None | Unset): Position of the communications template
        communication_template_stages_attributes
            (list[NewCommunicationsTemplateDataAttributesCommunicationTemplateStagesAttributesType0Item] | None | Unset):
            Template stages attributes
    """

    name: str
    communication_type_id: str
    description: None | str | Unset = UNSET
    position: int | None | Unset = UNSET
    communication_template_stages_attributes: (
        list[NewCommunicationsTemplateDataAttributesCommunicationTemplateStagesAttributesType0Item] | None | Unset
    ) = UNSET

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        communication_type_id = self.communication_type_id

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        position: int | None | Unset
        if isinstance(self.position, Unset):
            position = UNSET
        else:
            position = self.position

        communication_template_stages_attributes: list[dict[str, Any]] | None | Unset
        if isinstance(self.communication_template_stages_attributes, Unset):
            communication_template_stages_attributes = UNSET
        elif isinstance(self.communication_template_stages_attributes, list):
            communication_template_stages_attributes = []
            for (
                communication_template_stages_attributes_type_0_item_data
            ) in self.communication_template_stages_attributes:
                communication_template_stages_attributes_type_0_item = (
                    communication_template_stages_attributes_type_0_item_data.to_dict()
                )
                communication_template_stages_attributes.append(communication_template_stages_attributes_type_0_item)

        else:
            communication_template_stages_attributes = self.communication_template_stages_attributes

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "name": name,
                "communication_type_id": communication_type_id,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if position is not UNSET:
            field_dict["position"] = position
        if communication_template_stages_attributes is not UNSET:
            field_dict["communication_template_stages_attributes"] = communication_template_stages_attributes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.new_communications_template_data_attributes_communication_template_stages_attributes_type_0_item import (
            NewCommunicationsTemplateDataAttributesCommunicationTemplateStagesAttributesType0Item,
        )

        d = dict(src_dict)
        name = d.pop("name")

        communication_type_id = d.pop("communication_type_id")

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_position(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        position = _parse_position(d.pop("position", UNSET))

        def _parse_communication_template_stages_attributes(
            data: object,
        ) -> list[NewCommunicationsTemplateDataAttributesCommunicationTemplateStagesAttributesType0Item] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                communication_template_stages_attributes_type_0 = []
                _communication_template_stages_attributes_type_0 = data
                for (
                    communication_template_stages_attributes_type_0_item_data
                ) in _communication_template_stages_attributes_type_0:
                    communication_template_stages_attributes_type_0_item = (
                        NewCommunicationsTemplateDataAttributesCommunicationTemplateStagesAttributesType0Item.from_dict(
                            communication_template_stages_attributes_type_0_item_data
                        )
                    )

                    communication_template_stages_attributes_type_0.append(
                        communication_template_stages_attributes_type_0_item
                    )

                return communication_template_stages_attributes_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                list[NewCommunicationsTemplateDataAttributesCommunicationTemplateStagesAttributesType0Item]
                | None
                | Unset,
                data,
            )

        communication_template_stages_attributes = _parse_communication_template_stages_attributes(
            d.pop("communication_template_stages_attributes", UNSET)
        )

        new_communications_template_data_attributes = cls(
            name=name,
            communication_type_id=communication_type_id,
            description=description,
            position=position,
            communication_template_stages_attributes=communication_template_stages_attributes,
        )

        return new_communications_template_data_attributes
