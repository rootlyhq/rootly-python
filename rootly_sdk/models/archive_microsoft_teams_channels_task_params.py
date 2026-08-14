from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.archive_microsoft_teams_channels_task_params_task_type import (
    ArchiveMicrosoftTeamsChannelsTaskParamsTaskType,
    check_archive_microsoft_teams_channels_task_params_task_type,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.archive_microsoft_teams_channels_task_params_channels_item import (
        ArchiveMicrosoftTeamsChannelsTaskParamsChannelsItem,
    )
    from ..models.archive_microsoft_teams_channels_task_params_team import ArchiveMicrosoftTeamsChannelsTaskParamsTeam


T = TypeVar("T", bound="ArchiveMicrosoftTeamsChannelsTaskParams")


@_attrs_define
class ArchiveMicrosoftTeamsChannelsTaskParams:
    """
    Attributes:
        team (ArchiveMicrosoftTeamsChannelsTaskParamsTeam):
        channels (list['ArchiveMicrosoftTeamsChannelsTaskParamsChannelsItem']):
        task_type (Union[Unset, ArchiveMicrosoftTeamsChannelsTaskParamsTaskType]):
    """

    team: "ArchiveMicrosoftTeamsChannelsTaskParamsTeam"
    channels: list["ArchiveMicrosoftTeamsChannelsTaskParamsChannelsItem"]
    task_type: Unset | ArchiveMicrosoftTeamsChannelsTaskParamsTaskType = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        team = self.team.to_dict()

        channels = []
        for channels_item_data in self.channels:
            channels_item = channels_item_data.to_dict()
            channels.append(channels_item)

        task_type: Unset | str = UNSET
        if not isinstance(self.task_type, Unset):
            task_type = self.task_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "team": team,
                "channels": channels,
            }
        )
        if task_type is not UNSET:
            field_dict["task_type"] = task_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.archive_microsoft_teams_channels_task_params_channels_item import (
            ArchiveMicrosoftTeamsChannelsTaskParamsChannelsItem,
        )
        from ..models.archive_microsoft_teams_channels_task_params_team import (
            ArchiveMicrosoftTeamsChannelsTaskParamsTeam,
        )

        d = dict(src_dict)
        team = ArchiveMicrosoftTeamsChannelsTaskParamsTeam.from_dict(d.pop("team"))

        channels = []
        _channels = d.pop("channels")
        for channels_item_data in _channels:
            channels_item = ArchiveMicrosoftTeamsChannelsTaskParamsChannelsItem.from_dict(channels_item_data)

            channels.append(channels_item)

        _task_type = d.pop("task_type", UNSET)
        task_type: Unset | ArchiveMicrosoftTeamsChannelsTaskParamsTaskType
        if isinstance(_task_type, Unset):
            task_type = UNSET
        else:
            task_type = check_archive_microsoft_teams_channels_task_params_task_type(_task_type)

        archive_microsoft_teams_channels_task_params = cls(
            team=team,
            channels=channels,
            task_type=task_type,
        )

        archive_microsoft_teams_channels_task_params.additional_properties = d
        return archive_microsoft_teams_channels_task_params

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
