from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.shift_relationships_assignee import ShiftRelationshipsAssignee
    from ..models.shift_relationships_shift_override import ShiftRelationshipsShiftOverride
    from ..models.shift_relationships_user import ShiftRelationshipsUser


T = TypeVar("T", bound="ShiftRelationships")


@_attrs_define
class ShiftRelationships:
    """
    Attributes:
        shift_override (ShiftRelationshipsShiftOverride | Unset):
        user (ShiftRelationshipsUser | Unset):
        assignee (ShiftRelationshipsAssignee | Unset): Assignee can be either a User or Schedule
    """

    shift_override: ShiftRelationshipsShiftOverride | Unset = UNSET
    user: ShiftRelationshipsUser | Unset = UNSET
    assignee: ShiftRelationshipsAssignee | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        shift_override: dict[str, Any] | Unset = UNSET
        if not isinstance(self.shift_override, Unset):
            shift_override = self.shift_override.to_dict()

        user: dict[str, Any] | Unset = UNSET
        if not isinstance(self.user, Unset):
            user = self.user.to_dict()

        assignee: dict[str, Any] | Unset = UNSET
        if not isinstance(self.assignee, Unset):
            assignee = self.assignee.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if shift_override is not UNSET:
            field_dict["shift_override"] = shift_override
        if user is not UNSET:
            field_dict["user"] = user
        if assignee is not UNSET:
            field_dict["assignee"] = assignee

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.shift_relationships_assignee import ShiftRelationshipsAssignee
        from ..models.shift_relationships_shift_override import ShiftRelationshipsShiftOverride
        from ..models.shift_relationships_user import ShiftRelationshipsUser

        d = dict(src_dict)
        _shift_override = d.pop("shift_override", UNSET)
        shift_override: ShiftRelationshipsShiftOverride | Unset
        if isinstance(_shift_override, Unset):
            shift_override = UNSET
        else:
            shift_override = ShiftRelationshipsShiftOverride.from_dict(_shift_override)

        _user = d.pop("user", UNSET)
        user: ShiftRelationshipsUser | Unset
        if isinstance(_user, Unset):
            user = UNSET
        else:
            user = ShiftRelationshipsUser.from_dict(_user)

        _assignee = d.pop("assignee", UNSET)
        assignee: ShiftRelationshipsAssignee | Unset
        if isinstance(_assignee, Unset):
            assignee = UNSET
        else:
            assignee = ShiftRelationshipsAssignee.from_dict(_assignee)

        shift_relationships = cls(
            shift_override=shift_override,
            user=user,
            assignee=assignee,
        )

        shift_relationships.additional_properties = d
        return shift_relationships

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
