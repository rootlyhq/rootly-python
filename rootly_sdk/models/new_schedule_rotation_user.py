from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.new_schedule_rotation_user_data import NewScheduleRotationUserData


T = TypeVar("T", bound="NewScheduleRotationUser")


@_attrs_define
class NewScheduleRotationUser:
    """
    Attributes:
        data (Union[Unset, NewScheduleRotationUserData]):
    """

    data: Union[Unset, "NewScheduleRotationUserData"] = UNSET
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
        from ..models.new_schedule_rotation_user_data import NewScheduleRotationUserData

        d = dict(src_dict)
        _data = d.pop("data", UNSET)
        data: Unset | NewScheduleRotationUserData
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = NewScheduleRotationUserData.from_dict(_data)

        new_schedule_rotation_user = cls(
            data=data,
        )

        new_schedule_rotation_user.additional_properties = d
        return new_schedule_rotation_user

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
