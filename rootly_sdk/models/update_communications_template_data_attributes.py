from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.update_communications_template_data_attributes_communication_template_stages_attributes_type_0_item import (
        UpdateCommunicationsTemplateDataAttributesCommunicationTemplateStagesAttributesType0Item,
    )


T = TypeVar("T", bound="UpdateCommunicationsTemplateDataAttributes")


@_attrs_define
class UpdateCommunicationsTemplateDataAttributes:
    """
    Attributes:
        name (str | Unset): The name of the communications template
        description (None | str | Unset): The description of the communications template
        communication_type_id (str | Unset): The communication type ID
        position (int | None | Unset): Position of the communications template
        communication_template_stages_attributes
            (list[UpdateCommunicationsTemplateDataAttributesCommunicationTemplateStagesAttributesType0Item] | None | Unset):
            Template stages attributes
    """

    name: str | Unset = UNSET
    description: None | str | Unset = UNSET
    communication_type_id: str | Unset = UNSET
    position: int | None | Unset = UNSET
    communication_template_stages_attributes: (
        list[UpdateCommunicationsTemplateDataAttributesCommunicationTemplateStagesAttributesType0Item] | None | Unset
    ) = UNSET

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        communication_type_id = self.communication_type_id

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

        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if communication_type_id is not UNSET:
            field_dict["communication_type_id"] = communication_type_id
        if position is not UNSET:
            field_dict["position"] = position
        if communication_template_stages_attributes is not UNSET:
            field_dict["communication_template_stages_attributes"] = communication_template_stages_attributes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.update_communications_template_data_attributes_communication_template_stages_attributes_type_0_item import (
            UpdateCommunicationsTemplateDataAttributesCommunicationTemplateStagesAttributesType0Item,
        )

        d = dict(src_dict)
        name = d.pop("name", UNSET)

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        communication_type_id = d.pop("communication_type_id", UNSET)

        def _parse_position(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        position = _parse_position(d.pop("position", UNSET))

        def _parse_communication_template_stages_attributes(
            data: object,
        ) -> (
            list[UpdateCommunicationsTemplateDataAttributesCommunicationTemplateStagesAttributesType0Item]
            | None
            | Unset
        ):
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
                    communication_template_stages_attributes_type_0_item = UpdateCommunicationsTemplateDataAttributesCommunicationTemplateStagesAttributesType0Item.from_dict(
                        communication_template_stages_attributes_type_0_item_data
                    )

                    communication_template_stages_attributes_type_0.append(
                        communication_template_stages_attributes_type_0_item
                    )

                return communication_template_stages_attributes_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                list[UpdateCommunicationsTemplateDataAttributesCommunicationTemplateStagesAttributesType0Item]
                | None
                | Unset,
                data,
            )

        communication_template_stages_attributes = _parse_communication_template_stages_attributes(
            d.pop("communication_template_stages_attributes", UNSET)
        )

        update_communications_template_data_attributes = cls(
            name=name,
            description=description,
            communication_type_id=communication_type_id,
            position=position,
            communication_template_stages_attributes=communication_template_stages_attributes,
        )

        return update_communications_template_data_attributes
