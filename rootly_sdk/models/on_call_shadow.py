import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.on_call_shadow_shadowable_type import OnCallShadowShadowableType, check_on_call_shadow_shadowable_type
from ..types import UNSET, Unset

T = TypeVar("T", bound="OnCallShadow")


@_attrs_define
class OnCallShadow:
    """
    Attributes:
        schedule_id (str): ID of schedule the shadow shift belongs to
        shadowable_type (OnCallShadowShadowableType):
        shadowable_id (str): ID of schedule or user the shadow user is shadowing
        shadow_user_id (int): Which user the shadow shift belongs to.
        starts_at (datetime.datetime): Start datetime of shadow shift
        ends_at (datetime.datetime): End datetime for shadow shift
        created_at (Union[Unset, str]): Date of creation
        updated_at (Union[Unset, str]): Date of last update
    """

    schedule_id: str
    shadowable_type: OnCallShadowShadowableType
    shadowable_id: str
    shadow_user_id: int
    starts_at: datetime.datetime
    ends_at: datetime.datetime
    created_at: Unset | str = UNSET
    updated_at: Unset | str = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        schedule_id = self.schedule_id

        shadowable_type: str = self.shadowable_type

        shadowable_id = self.shadowable_id

        shadow_user_id = self.shadow_user_id

        starts_at = self.starts_at.isoformat()

        ends_at = self.ends_at.isoformat()

        created_at = self.created_at

        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "schedule_id": schedule_id,
                "shadowable_type": shadowable_type,
                "shadowable_id": shadowable_id,
                "shadow_user_id": shadow_user_id,
                "starts_at": starts_at,
                "ends_at": ends_at,
            }
        )
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        schedule_id = d.pop("schedule_id")

        shadowable_type = check_on_call_shadow_shadowable_type(d.pop("shadowable_type"))

        shadowable_id = d.pop("shadowable_id")

        shadow_user_id = d.pop("shadow_user_id")

        starts_at = isoparse(d.pop("starts_at"))

        ends_at = isoparse(d.pop("ends_at"))

        created_at = d.pop("created_at", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        on_call_shadow = cls(
            schedule_id=schedule_id,
            shadowable_type=shadowable_type,
            shadowable_id=shadowable_id,
            shadow_user_id=shadow_user_id,
            starts_at=starts_at,
            ends_at=ends_at,
            created_at=created_at,
            updated_at=updated_at,
        )

        on_call_shadow.additional_properties = d
        return on_call_shadow

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
