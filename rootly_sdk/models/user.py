from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="User")


@_attrs_define
class User:
    """
    Attributes:
        email (str): The email of the user
        created_at (str): Date of creation
        updated_at (str): Date of last update
        first_name (Union[None, Unset, str]): First name of the user
        last_name (Union[None, Unset, str]): Last name of the user
        full_name (Union[None, Unset, str]): The full name of the user
        full_name_with_team (Union[None, Unset, str]): The full name with team of the user
        time_zone (Union[None, Unset, str]): Configured time zone
    """

    email: str
    created_at: str
    updated_at: str
    first_name: None | Unset | str = UNSET
    last_name: None | Unset | str = UNSET
    full_name: None | Unset | str = UNSET
    full_name_with_team: None | Unset | str = UNSET
    time_zone: None | Unset | str = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        email = self.email

        created_at = self.created_at

        updated_at = self.updated_at

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

        full_name: None | Unset | str
        if isinstance(self.full_name, Unset):
            full_name = UNSET
        else:
            full_name = self.full_name

        full_name_with_team: None | Unset | str
        if isinstance(self.full_name_with_team, Unset):
            full_name_with_team = UNSET
        else:
            full_name_with_team = self.full_name_with_team

        time_zone: None | Unset | str
        if isinstance(self.time_zone, Unset):
            time_zone = UNSET
        else:
            time_zone = self.time_zone

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "email": email,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if first_name is not UNSET:
            field_dict["first_name"] = first_name
        if last_name is not UNSET:
            field_dict["last_name"] = last_name
        if full_name is not UNSET:
            field_dict["full_name"] = full_name
        if full_name_with_team is not UNSET:
            field_dict["full_name_with_team"] = full_name_with_team
        if time_zone is not UNSET:
            field_dict["time_zone"] = time_zone

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        email = d.pop("email")

        created_at = d.pop("created_at")

        updated_at = d.pop("updated_at")

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

        def _parse_full_name(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        full_name = _parse_full_name(d.pop("full_name", UNSET))

        def _parse_full_name_with_team(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        full_name_with_team = _parse_full_name_with_team(d.pop("full_name_with_team", UNSET))

        def _parse_time_zone(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        time_zone = _parse_time_zone(d.pop("time_zone", UNSET))

        user = cls(
            email=email,
            created_at=created_at,
            updated_at=updated_at,
            first_name=first_name,
            last_name=last_name,
            full_name=full_name,
            full_name_with_team=full_name_with_team,
            time_zone=time_zone,
        )

        user.additional_properties = d
        return user

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
