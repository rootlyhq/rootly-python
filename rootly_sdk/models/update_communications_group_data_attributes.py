from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.update_communications_group_data_attributes_condition_type import (
    UpdateCommunicationsGroupDataAttributesConditionType,
    check_update_communications_group_data_attributes_condition_type,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.update_communications_group_data_attributes_communication_external_group_members_type_0_item import (
        UpdateCommunicationsGroupDataAttributesCommunicationExternalGroupMembersType0Item,
    )
    from ..models.update_communications_group_data_attributes_communication_group_conditions_type_0_item import (
        UpdateCommunicationsGroupDataAttributesCommunicationGroupConditionsType0Item,
    )


T = TypeVar("T", bound="UpdateCommunicationsGroupDataAttributes")


@_attrs_define
class UpdateCommunicationsGroupDataAttributes:
    """
    Attributes:
        name (str | Unset): The name of the communications group
        description (None | str | Unset): The description of the communications group
        communication_type_id (str | Unset): The communication type ID
        is_private (bool | None | Unset): Whether the group is private
        condition_type (UpdateCommunicationsGroupDataAttributesConditionType | Unset): Condition type
        sms_channel (bool | None | Unset): SMS channel enabled
        email_channel (bool | None | Unset): Email channel enabled
        member_ids (list[int] | None | Unset): Array of member user IDs
        slack_channel_ids (list[str] | None | Unset): Array of Slack channel IDs
        communication_group_conditions
            (list[UpdateCommunicationsGroupDataAttributesCommunicationGroupConditionsType0Item] | None | Unset): Group
            conditions attributes
        communication_external_group_members
            (list[UpdateCommunicationsGroupDataAttributesCommunicationExternalGroupMembersType0Item] | None | Unset):
            External group members attributes
    """

    name: str | Unset = UNSET
    description: None | str | Unset = UNSET
    communication_type_id: str | Unset = UNSET
    is_private: bool | None | Unset = UNSET
    condition_type: UpdateCommunicationsGroupDataAttributesConditionType | Unset = UNSET
    sms_channel: bool | None | Unset = UNSET
    email_channel: bool | None | Unset = UNSET
    member_ids: list[int] | None | Unset = UNSET
    slack_channel_ids: list[str] | None | Unset = UNSET
    communication_group_conditions: (
        list[UpdateCommunicationsGroupDataAttributesCommunicationGroupConditionsType0Item] | None | Unset
    ) = UNSET
    communication_external_group_members: (
        list[UpdateCommunicationsGroupDataAttributesCommunicationExternalGroupMembersType0Item] | None | Unset
    ) = UNSET

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        communication_type_id = self.communication_type_id

        is_private: bool | None | Unset
        if isinstance(self.is_private, Unset):
            is_private = UNSET
        else:
            is_private = self.is_private

        condition_type: str | Unset = UNSET
        if not isinstance(self.condition_type, Unset):
            condition_type = self.condition_type

        sms_channel: bool | None | Unset
        if isinstance(self.sms_channel, Unset):
            sms_channel = UNSET
        else:
            sms_channel = self.sms_channel

        email_channel: bool | None | Unset
        if isinstance(self.email_channel, Unset):
            email_channel = UNSET
        else:
            email_channel = self.email_channel

        member_ids: list[int] | None | Unset
        if isinstance(self.member_ids, Unset):
            member_ids = UNSET
        elif isinstance(self.member_ids, list):
            member_ids = self.member_ids

        else:
            member_ids = self.member_ids

        slack_channel_ids: list[str] | None | Unset
        if isinstance(self.slack_channel_ids, Unset):
            slack_channel_ids = UNSET
        elif isinstance(self.slack_channel_ids, list):
            slack_channel_ids = self.slack_channel_ids

        else:
            slack_channel_ids = self.slack_channel_ids

        communication_group_conditions: list[dict[str, Any]] | None | Unset
        if isinstance(self.communication_group_conditions, Unset):
            communication_group_conditions = UNSET
        elif isinstance(self.communication_group_conditions, list):
            communication_group_conditions = []
            for communication_group_conditions_type_0_item_data in self.communication_group_conditions:
                communication_group_conditions_type_0_item = communication_group_conditions_type_0_item_data.to_dict()
                communication_group_conditions.append(communication_group_conditions_type_0_item)

        else:
            communication_group_conditions = self.communication_group_conditions

        communication_external_group_members: list[dict[str, Any]] | None | Unset
        if isinstance(self.communication_external_group_members, Unset):
            communication_external_group_members = UNSET
        elif isinstance(self.communication_external_group_members, list):
            communication_external_group_members = []
            for communication_external_group_members_type_0_item_data in self.communication_external_group_members:
                communication_external_group_members_type_0_item = (
                    communication_external_group_members_type_0_item_data.to_dict()
                )
                communication_external_group_members.append(communication_external_group_members_type_0_item)

        else:
            communication_external_group_members = self.communication_external_group_members

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if communication_type_id is not UNSET:
            field_dict["communication_type_id"] = communication_type_id
        if is_private is not UNSET:
            field_dict["is_private"] = is_private
        if condition_type is not UNSET:
            field_dict["condition_type"] = condition_type
        if sms_channel is not UNSET:
            field_dict["sms_channel"] = sms_channel
        if email_channel is not UNSET:
            field_dict["email_channel"] = email_channel
        if member_ids is not UNSET:
            field_dict["member_ids"] = member_ids
        if slack_channel_ids is not UNSET:
            field_dict["slack_channel_ids"] = slack_channel_ids
        if communication_group_conditions is not UNSET:
            field_dict["communication_group_conditions"] = communication_group_conditions
        if communication_external_group_members is not UNSET:
            field_dict["communication_external_group_members"] = communication_external_group_members

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.update_communications_group_data_attributes_communication_external_group_members_type_0_item import (
            UpdateCommunicationsGroupDataAttributesCommunicationExternalGroupMembersType0Item,
        )
        from ..models.update_communications_group_data_attributes_communication_group_conditions_type_0_item import (
            UpdateCommunicationsGroupDataAttributesCommunicationGroupConditionsType0Item,
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

        def _parse_is_private(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_private = _parse_is_private(d.pop("is_private", UNSET))

        _condition_type = d.pop("condition_type", UNSET)
        condition_type: UpdateCommunicationsGroupDataAttributesConditionType | Unset
        if isinstance(_condition_type, Unset):
            condition_type = UNSET
        else:
            condition_type = check_update_communications_group_data_attributes_condition_type(_condition_type)

        def _parse_sms_channel(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        sms_channel = _parse_sms_channel(d.pop("sms_channel", UNSET))

        def _parse_email_channel(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        email_channel = _parse_email_channel(d.pop("email_channel", UNSET))

        def _parse_member_ids(data: object) -> list[int] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                member_ids_type_0 = cast(list[int], data)

                return member_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[int] | None | Unset, data)

        member_ids = _parse_member_ids(d.pop("member_ids", UNSET))

        def _parse_slack_channel_ids(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                slack_channel_ids_type_0 = cast(list[str], data)

                return slack_channel_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        slack_channel_ids = _parse_slack_channel_ids(d.pop("slack_channel_ids", UNSET))

        def _parse_communication_group_conditions(
            data: object,
        ) -> list[UpdateCommunicationsGroupDataAttributesCommunicationGroupConditionsType0Item] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                communication_group_conditions_type_0 = []
                _communication_group_conditions_type_0 = data
                for communication_group_conditions_type_0_item_data in _communication_group_conditions_type_0:
                    communication_group_conditions_type_0_item = (
                        UpdateCommunicationsGroupDataAttributesCommunicationGroupConditionsType0Item.from_dict(
                            communication_group_conditions_type_0_item_data
                        )
                    )

                    communication_group_conditions_type_0.append(communication_group_conditions_type_0_item)

                return communication_group_conditions_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                list[UpdateCommunicationsGroupDataAttributesCommunicationGroupConditionsType0Item] | None | Unset, data
            )

        communication_group_conditions = _parse_communication_group_conditions(
            d.pop("communication_group_conditions", UNSET)
        )

        def _parse_communication_external_group_members(
            data: object,
        ) -> list[UpdateCommunicationsGroupDataAttributesCommunicationExternalGroupMembersType0Item] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                communication_external_group_members_type_0 = []
                _communication_external_group_members_type_0 = data
                for (
                    communication_external_group_members_type_0_item_data
                ) in _communication_external_group_members_type_0:
                    communication_external_group_members_type_0_item = (
                        UpdateCommunicationsGroupDataAttributesCommunicationExternalGroupMembersType0Item.from_dict(
                            communication_external_group_members_type_0_item_data
                        )
                    )

                    communication_external_group_members_type_0.append(communication_external_group_members_type_0_item)

                return communication_external_group_members_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                list[UpdateCommunicationsGroupDataAttributesCommunicationExternalGroupMembersType0Item] | None | Unset,
                data,
            )

        communication_external_group_members = _parse_communication_external_group_members(
            d.pop("communication_external_group_members", UNSET)
        )

        update_communications_group_data_attributes = cls(
            name=name,
            description=description,
            communication_type_id=communication_type_id,
            is_private=is_private,
            condition_type=condition_type,
            sms_channel=sms_channel,
            email_channel=email_channel,
            member_ids=member_ids,
            slack_channel_ids=slack_channel_ids,
            communication_group_conditions=communication_group_conditions,
            communication_external_group_members=communication_external_group_members,
        )

        return update_communications_group_data_attributes
