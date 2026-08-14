from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RemoveSubscribersDataAttributes")


@_attrs_define
class RemoveSubscribersDataAttributes:
    """
    Attributes:
        user_ids (Union[None, Unset, list[str]]): IDs of users you wish to remove from the list of subscribers for this
            incident
        remove_users_with_no_private_incident_access (Union[None, Unset, bool]): Users without read permissions for
            private incidents will be removed from the subscriber list of this incident Default: False.
    """

    user_ids: None | Unset | list[str] = UNSET
    remove_users_with_no_private_incident_access: None | Unset | bool = False

    def to_dict(self) -> dict[str, Any]:
        user_ids: None | Unset | list[str]
        if isinstance(self.user_ids, Unset):
            user_ids = UNSET
        elif isinstance(self.user_ids, list):
            user_ids = self.user_ids

        else:
            user_ids = self.user_ids

        remove_users_with_no_private_incident_access: None | Unset | bool
        if isinstance(self.remove_users_with_no_private_incident_access, Unset):
            remove_users_with_no_private_incident_access = UNSET
        else:
            remove_users_with_no_private_incident_access = self.remove_users_with_no_private_incident_access

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if user_ids is not UNSET:
            field_dict["user_ids"] = user_ids
        if remove_users_with_no_private_incident_access is not UNSET:
            field_dict["remove_users_with_no_private_incident_access"] = remove_users_with_no_private_incident_access

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_user_ids(data: object) -> None | Unset | list[str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                user_ids_type_0 = cast(list[str], data)

                return user_ids_type_0
            except:  # noqa: E722
                pass
            return cast(None | Unset | list[str], data)

        user_ids = _parse_user_ids(d.pop("user_ids", UNSET))

        def _parse_remove_users_with_no_private_incident_access(data: object) -> None | Unset | bool:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | bool, data)

        remove_users_with_no_private_incident_access = _parse_remove_users_with_no_private_incident_access(
            d.pop("remove_users_with_no_private_incident_access", UNSET)
        )

        remove_subscribers_data_attributes = cls(
            user_ids=user_ids,
            remove_users_with_no_private_incident_access=remove_users_with_no_private_incident_access,
        )

        return remove_subscribers_data_attributes
