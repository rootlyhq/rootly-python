from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.shift_override_response import ShiftOverrideResponse
    from ..models.user_response import UserResponse


T = TypeVar("T", bound="OverrideShift")


@_attrs_define
class OverrideShift:
    """
    Attributes:
        schedule_id (str): ID of schedule
        rotation_id (Union[None, str]): ID of rotation
        starts_at (str): Start datetime of shift
        ends_at (str): End datetime of shift
        is_override (bool): Denotes shift is an override shift
        created_at (Union[Unset, str]): Date of creation
        updated_at (Union[Unset, str]): Date of last update
        shift_override (Union[Unset, ShiftOverrideResponse]):
        user_id (Union[Unset, int]): Override shift user
        user (Union[Unset, UserResponse]):
    """

    schedule_id: str
    rotation_id: None | str
    starts_at: str
    ends_at: str
    is_override: bool
    created_at: Unset | str = UNSET
    updated_at: Unset | str = UNSET
    shift_override: Union[Unset, "ShiftOverrideResponse"] = UNSET
    user_id: Unset | int = UNSET
    user: Union[Unset, "UserResponse"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        schedule_id = self.schedule_id

        rotation_id: None | str
        rotation_id = self.rotation_id

        starts_at = self.starts_at

        ends_at = self.ends_at

        is_override = self.is_override

        created_at = self.created_at

        updated_at = self.updated_at

        shift_override: Unset | dict[str, Any] = UNSET
        if not isinstance(self.shift_override, Unset):
            shift_override = self.shift_override.to_dict()

        user_id = self.user_id

        user: Unset | dict[str, Any] = UNSET
        if not isinstance(self.user, Unset):
            user = self.user.to_dict()

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
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if shift_override is not UNSET:
            field_dict["shift_override"] = shift_override
        if user_id is not UNSET:
            field_dict["user_id"] = user_id
        if user is not UNSET:
            field_dict["user"] = user

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.shift_override_response import ShiftOverrideResponse
        from ..models.user_response import UserResponse

        d = dict(src_dict)
        schedule_id = d.pop("schedule_id")

        def _parse_rotation_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        rotation_id = _parse_rotation_id(d.pop("rotation_id"))

        starts_at = d.pop("starts_at")

        ends_at = d.pop("ends_at")

        is_override = d.pop("is_override")

        created_at = d.pop("created_at", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        _shift_override = d.pop("shift_override", UNSET)
        shift_override: Unset | ShiftOverrideResponse
        if isinstance(_shift_override, Unset):
            shift_override = UNSET
        else:
            shift_override = ShiftOverrideResponse.from_dict(_shift_override)

        user_id = d.pop("user_id", UNSET)

        _user = d.pop("user", UNSET)
        user: Unset | UserResponse
        if isinstance(_user, Unset):
            user = UNSET
        else:
            user = UserResponse.from_dict(_user)

        override_shift = cls(
            schedule_id=schedule_id,
            rotation_id=rotation_id,
            starts_at=starts_at,
            ends_at=ends_at,
            is_override=is_override,
            created_at=created_at,
            updated_at=updated_at,
            shift_override=shift_override,
            user_id=user_id,
            user=user,
        )

        override_shift.additional_properties = d
        return override_shift

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
