import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateApiKeyDataAttributes")


@_attrs_define
class UpdateApiKeyDataAttributes:
    """
    Attributes:
        name (Union[Unset, str]): The name of the API key
        description (Union[None, Unset, str]): A description of the API key
        expires_at (Union[None, Unset, datetime.datetime]): The expiration date of the API key (ISO 8601)
    """

    name: Unset | str = UNSET
    description: None | Unset | str = UNSET
    expires_at: None | Unset | datetime.datetime = UNSET

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        description: None | Unset | str
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        expires_at: None | Unset | str
        if isinstance(self.expires_at, Unset):
            expires_at = UNSET
        elif isinstance(self.expires_at, datetime.datetime):
            expires_at = self.expires_at.isoformat()
        else:
            expires_at = self.expires_at

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if expires_at is not UNSET:
            field_dict["expires_at"] = expires_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        def _parse_description(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_expires_at(data: object) -> None | Unset | datetime.datetime:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                expires_at_type_0 = isoparse(data)

                return expires_at_type_0
            except:  # noqa: E722
                pass
            return cast(None | Unset | datetime.datetime, data)

        expires_at = _parse_expires_at(d.pop("expires_at", UNSET))

        update_api_key_data_attributes = cls(
            name=name,
            description=description,
            expires_at=expires_at,
        )

        return update_api_key_data_attributes
