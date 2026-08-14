from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UserFlatResponse")


@_attrs_define
class UserFlatResponse:
    """Flat user attributes as returned by UserFlatSerializer (no nested associations)

    Attributes:
        id (int): User ID
        email (str): Email address
        created_at (str): Date of creation
        updated_at (str): Date of last update
        name (Union[Unset, str]): Display name
        phone (Union[None, Unset, str]): Primary phone number
        phone_2 (Union[None, Unset, str]): Secondary phone number
        first_name (Union[None, Unset, str]): First name
        last_name (Union[None, Unset, str]): Last name
        preferred_name (Union[None, Unset, str]): Preferred name
        full_name (Union[None, Unset, str]): Full name
        full_name_with_team (Union[None, Unset, str]): Full name with team context
        slack_id (Union[None, Unset, str]): Slack user ID
        time_zone (Union[None, Unset, str]): IANA time zone
    """

    id: int
    email: str
    created_at: str
    updated_at: str
    name: Unset | str = UNSET
    phone: None | Unset | str = UNSET
    phone_2: None | Unset | str = UNSET
    first_name: None | Unset | str = UNSET
    last_name: None | Unset | str = UNSET
    preferred_name: None | Unset | str = UNSET
    full_name: None | Unset | str = UNSET
    full_name_with_team: None | Unset | str = UNSET
    slack_id: None | Unset | str = UNSET
    time_zone: None | Unset | str = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        email = self.email

        created_at = self.created_at

        updated_at = self.updated_at

        name = self.name

        phone: None | Unset | str
        if isinstance(self.phone, Unset):
            phone = UNSET
        else:
            phone = self.phone

        phone_2: None | Unset | str
        if isinstance(self.phone_2, Unset):
            phone_2 = UNSET
        else:
            phone_2 = self.phone_2

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

        preferred_name: None | Unset | str
        if isinstance(self.preferred_name, Unset):
            preferred_name = UNSET
        else:
            preferred_name = self.preferred_name

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

        slack_id: None | Unset | str
        if isinstance(self.slack_id, Unset):
            slack_id = UNSET
        else:
            slack_id = self.slack_id

        time_zone: None | Unset | str
        if isinstance(self.time_zone, Unset):
            time_zone = UNSET
        else:
            time_zone = self.time_zone

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "email": email,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if phone is not UNSET:
            field_dict["phone"] = phone
        if phone_2 is not UNSET:
            field_dict["phone_2"] = phone_2
        if first_name is not UNSET:
            field_dict["first_name"] = first_name
        if last_name is not UNSET:
            field_dict["last_name"] = last_name
        if preferred_name is not UNSET:
            field_dict["preferred_name"] = preferred_name
        if full_name is not UNSET:
            field_dict["full_name"] = full_name
        if full_name_with_team is not UNSET:
            field_dict["full_name_with_team"] = full_name_with_team
        if slack_id is not UNSET:
            field_dict["slack_id"] = slack_id
        if time_zone is not UNSET:
            field_dict["time_zone"] = time_zone

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        email = d.pop("email")

        created_at = d.pop("created_at")

        updated_at = d.pop("updated_at")

        name = d.pop("name", UNSET)

        def _parse_phone(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        phone = _parse_phone(d.pop("phone", UNSET))

        def _parse_phone_2(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        phone_2 = _parse_phone_2(d.pop("phone_2", UNSET))

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

        def _parse_preferred_name(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        preferred_name = _parse_preferred_name(d.pop("preferred_name", UNSET))

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

        def _parse_slack_id(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        slack_id = _parse_slack_id(d.pop("slack_id", UNSET))

        def _parse_time_zone(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        time_zone = _parse_time_zone(d.pop("time_zone", UNSET))

        user_flat_response = cls(
            id=id,
            email=email,
            created_at=created_at,
            updated_at=updated_at,
            name=name,
            phone=phone,
            phone_2=phone_2,
            first_name=first_name,
            last_name=last_name,
            preferred_name=preferred_name,
            full_name=full_name,
            full_name_with_team=full_name_with_team,
            slack_id=slack_id,
            time_zone=time_zone,
        )

        user_flat_response.additional_properties = d
        return user_flat_response

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
