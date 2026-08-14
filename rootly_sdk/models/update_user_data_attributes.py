from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateUserDataAttributes")


@_attrs_define
class UpdateUserDataAttributes:
    """
    Attributes:
        first_name (Union[None, Unset, str]): First name of the user
        last_name (Union[None, Unset, str]): Last name of the user
        role_id (Union[None, Unset, str]): ID of the role to assign
        on_call_role_id (Union[None, Unset, str]): ID of the on-call role to assign
    """

    first_name: None | Unset | str = UNSET
    last_name: None | Unset | str = UNSET
    role_id: None | Unset | str = UNSET
    on_call_role_id: None | Unset | str = UNSET

    def to_dict(self) -> dict[str, Any]:
        first_name: None | Unset | str
        if isinstance(self.first_name, Unset):
            first_name = UNSET
        else:
            first_name = self.first_name

        last_name: None | Unset | str
        if isinstance(self.last_name, Unset):
            last_name = UNSET
        else:
            last_name = self.last_name

        role_id: None | Unset | str
        if isinstance(self.role_id, Unset):
            role_id = UNSET
        else:
            role_id = self.role_id

        on_call_role_id: None | Unset | str
        if isinstance(self.on_call_role_id, Unset):
            on_call_role_id = UNSET
        else:
            on_call_role_id = self.on_call_role_id

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if first_name is not UNSET:
            field_dict["first_name"] = first_name
        if last_name is not UNSET:
            field_dict["last_name"] = last_name
        if role_id is not UNSET:
            field_dict["role_id"] = role_id
        if on_call_role_id is not UNSET:
            field_dict["on_call_role_id"] = on_call_role_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_first_name(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        first_name = _parse_first_name(d.pop("first_name", UNSET))

        def _parse_last_name(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        last_name = _parse_last_name(d.pop("last_name", UNSET))

        def _parse_role_id(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        role_id = _parse_role_id(d.pop("role_id", UNSET))

        def _parse_on_call_role_id(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        on_call_role_id = _parse_on_call_role_id(d.pop("on_call_role_id", UNSET))

        update_user_data_attributes = cls(
            first_name=first_name,
            last_name=last_name,
            role_id=role_id,
            on_call_role_id=on_call_role_id,
        )

        return update_user_data_attributes
