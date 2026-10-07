from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..models.new_status_page_team_data_type import NewStatusPageTeamDataType, check_new_status_page_team_data_type

if TYPE_CHECKING:
    from ..models.new_status_page_team_data_attributes import NewStatusPageTeamDataAttributes


T = TypeVar("T", bound="NewStatusPageTeamData")


@_attrs_define
class NewStatusPageTeamData:
    """
    Attributes:
        type_ (NewStatusPageTeamDataType):
        attributes (NewStatusPageTeamDataAttributes):
    """

    type_: NewStatusPageTeamDataType
    attributes: NewStatusPageTeamDataAttributes

    def to_dict(self) -> dict[str, Any]:
        type_: str = self.type_

        attributes = self.attributes.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "type": type_,
                "attributes": attributes,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.new_status_page_team_data_attributes import NewStatusPageTeamDataAttributes

        d = dict(src_dict)
        type_ = check_new_status_page_team_data_type(d.pop("type"))

        attributes = NewStatusPageTeamDataAttributes.from_dict(d.pop("attributes"))

        new_status_page_team_data = cls(
            type_=type_,
            attributes=attributes,
        )

        return new_status_page_team_data
