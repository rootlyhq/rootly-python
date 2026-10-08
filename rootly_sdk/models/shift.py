from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.overridden_shift import OverriddenShift


T = TypeVar("T", bound="Shift")


@_attrs_define
class Shift:
    """
    Attributes:
        schedule_id (str): ID of schedule
        rotation_id (None | str): ID of rotation
        starts_at (str): Start datetime of shift
        ends_at (str): End datetime of shift
        is_override (bool): Denotes shift is an override shift
        is_shadow (bool): Denotes shift is a shadow shift
        user_id (int | None | Unset): ID of user on shift
        overridden_shifts (list[OverriddenShift] | None | Unset): For override shifts, the portions of the regular
            shifts this override replaces, clipped to the override window. Null for non-override shifts. Available when
            overridden shifts are enabled for the organization.
    """

    schedule_id: str
    rotation_id: None | str
    starts_at: str
    ends_at: str
    is_override: bool
    is_shadow: bool
    user_id: int | None | Unset = UNSET
    overridden_shifts: list[OverriddenShift] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        schedule_id = self.schedule_id

        rotation_id: None | str
        rotation_id = self.rotation_id

        starts_at = self.starts_at

        ends_at = self.ends_at

        is_override = self.is_override

        is_shadow = self.is_shadow

        user_id: int | None | Unset
        if isinstance(self.user_id, Unset):
            user_id = UNSET
        else:
            user_id = self.user_id

        overridden_shifts: list[dict[str, Any]] | None | Unset
        if isinstance(self.overridden_shifts, Unset):
            overridden_shifts = UNSET
        elif isinstance(self.overridden_shifts, list):
            overridden_shifts = []
            for overridden_shifts_type_0_item_data in self.overridden_shifts:
                overridden_shifts_type_0_item = overridden_shifts_type_0_item_data.to_dict()
                overridden_shifts.append(overridden_shifts_type_0_item)

        else:
            overridden_shifts = self.overridden_shifts

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "schedule_id": schedule_id,
                "rotation_id": rotation_id,
                "starts_at": starts_at,
                "ends_at": ends_at,
                "is_override": is_override,
                "is_shadow": is_shadow,
            }
        )
        if user_id is not UNSET:
            field_dict["user_id"] = user_id
        if overridden_shifts is not UNSET:
            field_dict["overridden_shifts"] = overridden_shifts

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.overridden_shift import OverriddenShift

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

        is_shadow = d.pop("is_shadow")

        def _parse_user_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        user_id = _parse_user_id(d.pop("user_id", UNSET))

        def _parse_overridden_shifts(data: object) -> list[OverriddenShift] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                overridden_shifts_type_0 = []
                _overridden_shifts_type_0 = data
                for overridden_shifts_type_0_item_data in _overridden_shifts_type_0:
                    overridden_shifts_type_0_item = OverriddenShift.from_dict(overridden_shifts_type_0_item_data)

                    overridden_shifts_type_0.append(overridden_shifts_type_0_item)

                return overridden_shifts_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[OverriddenShift] | None | Unset, data)

        overridden_shifts = _parse_overridden_shifts(d.pop("overridden_shifts", UNSET))

        shift = cls(
            schedule_id=schedule_id,
            rotation_id=rotation_id,
            starts_at=starts_at,
            ends_at=ends_at,
            is_override=is_override,
            is_shadow=is_shadow,
            user_id=user_id,
            overridden_shifts=overridden_shifts,
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
