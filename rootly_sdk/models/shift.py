from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Shift")


@_attrs_define
class Shift:
    """
    Attributes:
        schedule_id (str): ID of schedule
        rotation_id (Union[None, str]): ID of rotation
        starts_at (str): Start datetime of shift
        ends_at (str): End datetime of shift
        is_override (bool): Denotes shift is an override shift
        user_id (Union[None, Unset, int]): ID of user on shift
    """

    schedule_id: str
    rotation_id: Union[None, str]
    starts_at: str
    ends_at: str
    is_override: bool
    user_id: Union[None, Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        schedule_id = self.schedule_id

        rotation_id: Union[None, str]
        rotation_id = self.rotation_id

        starts_at = self.starts_at

        ends_at = self.ends_at

        is_override = self.is_override

        user_id: Union[None, Unset, int]
        if isinstance(self.user_id, Unset):
            user_id = UNSET
        else:
            user_id = self.user_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "schedule_id": schedule_id,
                "rotation_id": rotation_id,
                "starts_at": starts_at,
                "ends_at": ends_at,
                "is_override": is_override,
            }
        )
        if user_id is not UNSET:
            field_dict["user_id"] = user_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        schedule_id = d.pop("schedule_id")

        def _parse_rotation_id(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        rotation_id = _parse_rotation_id(d.pop("rotation_id"))

        starts_at = d.pop("starts_at")

        ends_at = d.pop("ends_at")

        is_override = d.pop("is_override")

        def _parse_user_id(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        user_id = _parse_user_id(d.pop("user_id", UNSET))

        shift = cls(
            schedule_id=schedule_id,
            rotation_id=rotation_id,
            starts_at=starts_at,
            ends_at=ends_at,
            is_override=is_override,
            user_id=user_id,
        )

        shift.additional_properties = d
        return shift

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
