from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.update_alert_data_attributes_noise import (
    UpdateAlertDataAttributesNoise,
    check_update_alert_data_attributes_noise,
)
from ..models.update_alert_data_attributes_source import (
    UpdateAlertDataAttributesSource,
    check_update_alert_data_attributes_source,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.update_alert_data_attributes_alert_field_values_attributes_item_type_0 import (
        UpdateAlertDataAttributesAlertFieldValuesAttributesItemType0,
    )
    from ..models.update_alert_data_attributes_data_type_0 import UpdateAlertDataAttributesDataType0
    from ..models.update_alert_data_attributes_labels_item_type_0 import UpdateAlertDataAttributesLabelsItemType0


T = TypeVar("T", bound="UpdateAlertDataAttributes")


@_attrs_define
class UpdateAlertDataAttributes:
    """
    Attributes:
        noise (UpdateAlertDataAttributesNoise | Unset): Whether the alert is marked as noise
        source (UpdateAlertDataAttributesSource | Unset): The source of the alert
        summary (str | Unset): The summary of the alert
        description (None | str | Unset): The description of the alert
        service_ids (list[str] | None | Unset): The Service IDs to attach to the alert
        group_ids (list[str] | None | Unset): The Group IDs to attach to the alert
        environment_ids (list[str] | None | Unset): The Environment IDs to attach to the alert
        started_at (datetime.datetime | None | Unset): Alert start datetime
        ended_at (datetime.datetime | None | Unset): Alert end datetime
        external_id (None | str | Unset): External ID
        external_url (None | str | Unset): External Url
        alert_urgency_id (None | str | Unset): The ID of the alert urgency
        labels (list[None | UpdateAlertDataAttributesLabelsItemType0] | Unset):
        data (None | Unset | UpdateAlertDataAttributesDataType0): Additional data
        deduplication_key (None | str | Unset): Alerts sharing the same deduplication key are treated as a single alert.
        alert_field_values_attributes (list[None | UpdateAlertDataAttributesAlertFieldValuesAttributesItemType0] |
            Unset): Custom alert field values to create with the alert
    """

    noise: UpdateAlertDataAttributesNoise | Unset = UNSET
    source: UpdateAlertDataAttributesSource | Unset = UNSET
    summary: str | Unset = UNSET
    description: None | str | Unset = UNSET
    service_ids: list[str] | None | Unset = UNSET
    group_ids: list[str] | None | Unset = UNSET
    environment_ids: list[str] | None | Unset = UNSET
    started_at: datetime.datetime | None | Unset = UNSET
    ended_at: datetime.datetime | None | Unset = UNSET
    external_id: None | str | Unset = UNSET
    external_url: None | str | Unset = UNSET
    alert_urgency_id: None | str | Unset = UNSET
    labels: list[None | UpdateAlertDataAttributesLabelsItemType0] | Unset = UNSET
    data: None | Unset | UpdateAlertDataAttributesDataType0 = UNSET
    deduplication_key: None | str | Unset = UNSET
    alert_field_values_attributes: list[None | UpdateAlertDataAttributesAlertFieldValuesAttributesItemType0] | Unset = (
        UNSET
    )

    def to_dict(self) -> dict[str, Any]:
        from ..models.update_alert_data_attributes_alert_field_values_attributes_item_type_0 import (
            UpdateAlertDataAttributesAlertFieldValuesAttributesItemType0,
        )
        from ..models.update_alert_data_attributes_data_type_0 import UpdateAlertDataAttributesDataType0
        from ..models.update_alert_data_attributes_labels_item_type_0 import UpdateAlertDataAttributesLabelsItemType0

        noise: str | Unset = UNSET
        if not isinstance(self.noise, Unset):
            noise = self.noise

        source: str | Unset = UNSET
        if not isinstance(self.source, Unset):
            source = self.source

        summary = self.summary

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        service_ids: list[str] | None | Unset
        if isinstance(self.service_ids, Unset):
            service_ids = UNSET
        elif isinstance(self.service_ids, list):
            service_ids = self.service_ids

        else:
            service_ids = self.service_ids

        group_ids: list[str] | None | Unset
        if isinstance(self.group_ids, Unset):
            group_ids = UNSET
        elif isinstance(self.group_ids, list):
            group_ids = self.group_ids

        else:
            group_ids = self.group_ids

        environment_ids: list[str] | None | Unset
        if isinstance(self.environment_ids, Unset):
            environment_ids = UNSET
        elif isinstance(self.environment_ids, list):
            environment_ids = self.environment_ids

        else:
            environment_ids = self.environment_ids

        started_at: None | str | Unset
        if isinstance(self.started_at, Unset):
            started_at = UNSET
        elif isinstance(self.started_at, datetime.datetime):
            started_at = self.started_at.isoformat()
        else:
            started_at = self.started_at

        ended_at: None | str | Unset
        if isinstance(self.ended_at, Unset):
            ended_at = UNSET
        elif isinstance(self.ended_at, datetime.datetime):
            ended_at = self.ended_at.isoformat()
        else:
            ended_at = self.ended_at

        external_id: None | str | Unset
        if isinstance(self.external_id, Unset):
            external_id = UNSET
        else:
            external_id = self.external_id

        external_url: None | str | Unset
        if isinstance(self.external_url, Unset):
            external_url = UNSET
        else:
            external_url = self.external_url

        alert_urgency_id: None | str | Unset
        if isinstance(self.alert_urgency_id, Unset):
            alert_urgency_id = UNSET
        else:
            alert_urgency_id = self.alert_urgency_id

        labels: list[dict[str, Any] | None] | Unset = UNSET
        if not isinstance(self.labels, Unset):
            labels = []
            for labels_item_data in self.labels:
                labels_item: dict[str, Any] | None
                if isinstance(labels_item_data, UpdateAlertDataAttributesLabelsItemType0):
                    labels_item = labels_item_data.to_dict()
                else:
                    labels_item = labels_item_data
                labels.append(labels_item)

        data: dict[str, Any] | None | Unset
        if isinstance(self.data, Unset):
            data = UNSET
        elif isinstance(self.data, UpdateAlertDataAttributesDataType0):
            data = self.data.to_dict()
        else:
            data = self.data

        deduplication_key: None | str | Unset
        if isinstance(self.deduplication_key, Unset):
            deduplication_key = UNSET
        else:
            deduplication_key = self.deduplication_key

        alert_field_values_attributes: list[dict[str, Any] | None] | Unset = UNSET
        if not isinstance(self.alert_field_values_attributes, Unset):
            alert_field_values_attributes = []
            for alert_field_values_attributes_item_data in self.alert_field_values_attributes:
                alert_field_values_attributes_item: dict[str, Any] | None
                if isinstance(
                    alert_field_values_attributes_item_data,
                    UpdateAlertDataAttributesAlertFieldValuesAttributesItemType0,
                ):
                    alert_field_values_attributes_item = alert_field_values_attributes_item_data.to_dict()
                else:
                    alert_field_values_attributes_item = alert_field_values_attributes_item_data
                alert_field_values_attributes.append(alert_field_values_attributes_item)

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if noise is not UNSET:
            field_dict["noise"] = noise
        if source is not UNSET:
            field_dict["source"] = source
        if summary is not UNSET:
            field_dict["summary"] = summary
        if description is not UNSET:
            field_dict["description"] = description
        if service_ids is not UNSET:
            field_dict["service_ids"] = service_ids
        if group_ids is not UNSET:
            field_dict["group_ids"] = group_ids
        if environment_ids is not UNSET:
            field_dict["environment_ids"] = environment_ids
        if started_at is not UNSET:
            field_dict["started_at"] = started_at
        if ended_at is not UNSET:
            field_dict["ended_at"] = ended_at
        if external_id is not UNSET:
            field_dict["external_id"] = external_id
        if external_url is not UNSET:
            field_dict["external_url"] = external_url
        if alert_urgency_id is not UNSET:
            field_dict["alert_urgency_id"] = alert_urgency_id
        if labels is not UNSET:
            field_dict["labels"] = labels
        if data is not UNSET:
            field_dict["data"] = data
        if deduplication_key is not UNSET:
            field_dict["deduplication_key"] = deduplication_key
        if alert_field_values_attributes is not UNSET:
            field_dict["alert_field_values_attributes"] = alert_field_values_attributes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.update_alert_data_attributes_alert_field_values_attributes_item_type_0 import (
            UpdateAlertDataAttributesAlertFieldValuesAttributesItemType0,
        )
        from ..models.update_alert_data_attributes_data_type_0 import UpdateAlertDataAttributesDataType0
        from ..models.update_alert_data_attributes_labels_item_type_0 import UpdateAlertDataAttributesLabelsItemType0

        d = dict(src_dict)
        _noise = d.pop("noise", UNSET)
        noise: UpdateAlertDataAttributesNoise | Unset
        if isinstance(_noise, Unset):
            noise = UNSET
        else:
            noise = check_update_alert_data_attributes_noise(_noise)

        _source = d.pop("source", UNSET)
        source: UpdateAlertDataAttributesSource | Unset
        if isinstance(_source, Unset):
            source = UNSET
        else:
            source = check_update_alert_data_attributes_source(_source)

        summary = d.pop("summary", UNSET)

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_service_ids(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                service_ids_type_0 = cast(list[str], data)

                return service_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        service_ids = _parse_service_ids(d.pop("service_ids", UNSET))

        def _parse_group_ids(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                group_ids_type_0 = cast(list[str], data)

                return group_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        group_ids = _parse_group_ids(d.pop("group_ids", UNSET))

        def _parse_environment_ids(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                environment_ids_type_0 = cast(list[str], data)

                return environment_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        environment_ids = _parse_environment_ids(d.pop("environment_ids", UNSET))

        def _parse_started_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                started_at_type_0 = isoparse(data)

                return started_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        started_at = _parse_started_at(d.pop("started_at", UNSET))

        def _parse_ended_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                ended_at_type_0 = isoparse(data)

                return ended_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        ended_at = _parse_ended_at(d.pop("ended_at", UNSET))

        def _parse_external_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        external_id = _parse_external_id(d.pop("external_id", UNSET))

        def _parse_external_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        external_url = _parse_external_url(d.pop("external_url", UNSET))

        def _parse_alert_urgency_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        alert_urgency_id = _parse_alert_urgency_id(d.pop("alert_urgency_id", UNSET))

        _labels = d.pop("labels", UNSET)
        labels: list[None | UpdateAlertDataAttributesLabelsItemType0] | Unset = UNSET
        if _labels is not UNSET:
            labels = []
            for labels_item_data in _labels:

                def _parse_labels_item(data: object) -> None | UpdateAlertDataAttributesLabelsItemType0:
                    if data is None:
                        return data
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        labels_item_type_0 = UpdateAlertDataAttributesLabelsItemType0.from_dict(data)

                        return labels_item_type_0
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    return cast(None | UpdateAlertDataAttributesLabelsItemType0, data)

                labels_item = _parse_labels_item(labels_item_data)

                labels.append(labels_item)

        def _parse_data(data: object) -> None | Unset | UpdateAlertDataAttributesDataType0:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                data_type_0 = UpdateAlertDataAttributesDataType0.from_dict(data)

                return data_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UpdateAlertDataAttributesDataType0, data)

        data = _parse_data(d.pop("data", UNSET))

        def _parse_deduplication_key(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        deduplication_key = _parse_deduplication_key(d.pop("deduplication_key", UNSET))

        _alert_field_values_attributes = d.pop("alert_field_values_attributes", UNSET)
        alert_field_values_attributes: (
            list[None | UpdateAlertDataAttributesAlertFieldValuesAttributesItemType0] | Unset
        ) = UNSET
        if _alert_field_values_attributes is not UNSET:
            alert_field_values_attributes = []
            for alert_field_values_attributes_item_data in _alert_field_values_attributes:

                def _parse_alert_field_values_attributes_item(
                    data: object,
                ) -> None | UpdateAlertDataAttributesAlertFieldValuesAttributesItemType0:
                    if data is None:
                        return data
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        alert_field_values_attributes_item_type_0 = (
                            UpdateAlertDataAttributesAlertFieldValuesAttributesItemType0.from_dict(data)
                        )

                        return alert_field_values_attributes_item_type_0
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    return cast(None | UpdateAlertDataAttributesAlertFieldValuesAttributesItemType0, data)

                alert_field_values_attributes_item = _parse_alert_field_values_attributes_item(
                    alert_field_values_attributes_item_data
                )

                alert_field_values_attributes.append(alert_field_values_attributes_item)

        update_alert_data_attributes = cls(
            noise=noise,
            source=source,
            summary=summary,
            description=description,
            service_ids=service_ids,
            group_ids=group_ids,
            environment_ids=environment_ids,
            started_at=started_at,
            ended_at=ended_at,
            external_id=external_id,
            external_url=external_url,
            alert_urgency_id=alert_urgency_id,
            labels=labels,
            data=data,
            deduplication_key=deduplication_key,
            alert_field_values_attributes=alert_field_values_attributes,
        )

        return update_alert_data_attributes
