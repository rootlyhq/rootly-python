from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.on_call_role_relationship_data_type_0 import OnCallRoleRelationshipDataType0


T = TypeVar("T", bound="OnCallRoleRelationship")


@_attrs_define
class OnCallRoleRelationship:
    """
    Attributes:
        data (Union['OnCallRoleRelationshipDataType0', None, Unset]):
    """

    data: Union["OnCallRoleRelationshipDataType0", None, Unset] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.on_call_role_relationship_data_type_0 import OnCallRoleRelationshipDataType0

        data: None | Unset | dict[str, Any]
        if isinstance(self.data, Unset):
            data = UNSET
        elif isinstance(self.data, OnCallRoleRelationshipDataType0):
            data = self.data.to_dict()
        else:
            data = self.data

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if data is not UNSET:
            field_dict["data"] = data

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.on_call_role_relationship_data_type_0 import OnCallRoleRelationshipDataType0

        d = dict(src_dict)

        def _parse_data(data: object) -> Union["OnCallRoleRelationshipDataType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                data_type_0 = OnCallRoleRelationshipDataType0.from_dict(data)

                return data_type_0
            except:  # noqa: E722
                pass
            return cast(Union["OnCallRoleRelationshipDataType0", None, Unset], data)

        data = _parse_data(d.pop("data", UNSET))

        on_call_role_relationship = cls(
            data=data,
        )

        on_call_role_relationship.additional_properties = d
        return on_call_role_relationship

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
