import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.new_on_call_shadow_data_attributes_shadowable_type import (
    NewOnCallShadowDataAttributesShadowableType,
    check_new_on_call_shadow_data_attributes_shadowable_type,
)

T = TypeVar("T", bound="NewOnCallShadowDataAttributes")


@_attrs_define
class NewOnCallShadowDataAttributes:
    """
    Attributes:
        shadowable_type (NewOnCallShadowDataAttributesShadowableType):
        shadowable_id (str): ID of schedule or user the shadow user is shadowing
        shadow_user_id (int): Which user the shadow shift belongs to.
        starts_at (datetime.datetime): Start datetime of shadow shift
        ends_at (datetime.datetime): End datetime for shadow shift
    """

    shadowable_type: NewOnCallShadowDataAttributesShadowableType
    shadowable_id: str
    shadow_user_id: int
    starts_at: datetime.datetime
    ends_at: datetime.datetime

    def to_dict(self) -> dict[str, Any]:
        shadowable_type: str = self.shadowable_type

        shadowable_id = self.shadowable_id

        shadow_user_id = self.shadow_user_id

        starts_at = self.starts_at.isoformat()

        ends_at = self.ends_at.isoformat()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "shadowable_type": shadowable_type,
                "shadowable_id": shadowable_id,
                "shadow_user_id": shadow_user_id,
                "starts_at": starts_at,
                "ends_at": ends_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        shadowable_type = check_new_on_call_shadow_data_attributes_shadowable_type(d.pop("shadowable_type"))

        shadowable_id = d.pop("shadowable_id")

        shadow_user_id = d.pop("shadow_user_id")

        starts_at = isoparse(d.pop("starts_at"))

        ends_at = isoparse(d.pop("ends_at"))

        new_on_call_shadow_data_attributes = cls(
            shadowable_type=shadowable_type,
            shadowable_id=shadowable_id,
            shadow_user_id=shadow_user_id,
            starts_at=starts_at,
            ends_at=ends_at,
        )

        return new_on_call_shadow_data_attributes
