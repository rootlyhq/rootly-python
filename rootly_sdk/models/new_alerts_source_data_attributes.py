from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.new_alerts_source_data_attributes_deduplication_key_kind import (
    NewAlertsSourceDataAttributesDeduplicationKeyKind,
    check_new_alerts_source_data_attributes_deduplication_key_kind,
)
from ..models.new_alerts_source_data_attributes_source_type import (
    NewAlertsSourceDataAttributesSourceType,
    check_new_alerts_source_data_attributes_source_type,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.new_alerts_source_data_attributes_alert_source_fields_attributes_item import (
        NewAlertsSourceDataAttributesAlertSourceFieldsAttributesItem,
    )
    from ..models.new_alerts_source_data_attributes_alert_source_urgency_rules_attributes_item import (
        NewAlertsSourceDataAttributesAlertSourceUrgencyRulesAttributesItem,
    )
    from ..models.new_alerts_source_data_attributes_alert_template_attributes_type_0 import (
        NewAlertsSourceDataAttributesAlertTemplateAttributesType0,
    )
    from ..models.new_alerts_source_data_attributes_resolution_rule_attributes_type_0 import (
        NewAlertsSourceDataAttributesResolutionRuleAttributesType0,
    )
    from ..models.new_alerts_source_data_attributes_sourceable_attributes_type_0 import (
        NewAlertsSourceDataAttributesSourceableAttributesType0,
    )


T = TypeVar("T", bound="NewAlertsSourceDataAttributes")


@_attrs_define
class NewAlertsSourceDataAttributes:
    """
    Attributes:
        name (str): The name of the alert source
        source_type (NewAlertsSourceDataAttributesSourceType | Unset): The alert source type
        alert_urgency_id (str | Unset): ID for the default alert urgency assigned to this alert source
        deduplicate_alerts_by_key (bool | Unset): Toggle alert deduplication using deduplication key. If enabled,
            deduplication_key_kind and deduplication_key_path are required.
        deduplication_key_kind (NewAlertsSourceDataAttributesDeduplicationKeyKind | Unset): Kind of deduplication key.
        deduplication_key_path (None | str | Unset): Path to deduplication key. This is a JSON Path to extract the
            deduplication key from the request body.
        deduplication_key_regexp (None | str | Unset): Regular expression to extract key from value found at key path.
        owner_group_ids (list[str] | Unset): List of team IDs that will own the alert source
        alert_template_attributes (NewAlertsSourceDataAttributesAlertTemplateAttributesType0 | None | Unset):
        alert_source_urgency_rules_attributes (list[NewAlertsSourceDataAttributesAlertSourceUrgencyRulesAttributesItem]
            | Unset): List of rules that define the conditions under which the alert urgency will be set automatically based
            on the alert payload
        sourceable_attributes (NewAlertsSourceDataAttributesSourceableAttributesType0 | None | Unset): Provide
            additional attributes for generic_webhook alerts source
        resolution_rule_attributes (NewAlertsSourceDataAttributesResolutionRuleAttributesType0 | None | Unset): Provide
            additional attributes for email alerts source
        alert_source_fields_attributes (list[NewAlertsSourceDataAttributesAlertSourceFieldsAttributesItem] | Unset):
            List of alert fields to be added to the alert source. Note: This attribute requires the alert field feature to
            be enabled on your account. Contact Rootly customer support if you need assistance with this feature.
    """

    name: str
    source_type: NewAlertsSourceDataAttributesSourceType | Unset = UNSET
    alert_urgency_id: str | Unset = UNSET
    deduplicate_alerts_by_key: bool | Unset = UNSET
    deduplication_key_kind: NewAlertsSourceDataAttributesDeduplicationKeyKind | Unset = UNSET
    deduplication_key_path: None | str | Unset = UNSET
    deduplication_key_regexp: None | str | Unset = UNSET
    owner_group_ids: list[str] | Unset = UNSET
    alert_template_attributes: NewAlertsSourceDataAttributesAlertTemplateAttributesType0 | None | Unset = UNSET
    alert_source_urgency_rules_attributes: (
        list[NewAlertsSourceDataAttributesAlertSourceUrgencyRulesAttributesItem] | Unset
    ) = UNSET
    sourceable_attributes: NewAlertsSourceDataAttributesSourceableAttributesType0 | None | Unset = UNSET
    resolution_rule_attributes: NewAlertsSourceDataAttributesResolutionRuleAttributesType0 | None | Unset = UNSET
    alert_source_fields_attributes: list[NewAlertsSourceDataAttributesAlertSourceFieldsAttributesItem] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.new_alerts_source_data_attributes_alert_template_attributes_type_0 import (
            NewAlertsSourceDataAttributesAlertTemplateAttributesType0,
        )
        from ..models.new_alerts_source_data_attributes_resolution_rule_attributes_type_0 import (
            NewAlertsSourceDataAttributesResolutionRuleAttributesType0,
        )
        from ..models.new_alerts_source_data_attributes_sourceable_attributes_type_0 import (
            NewAlertsSourceDataAttributesSourceableAttributesType0,
        )

        name = self.name

        source_type: str | Unset = UNSET
        if not isinstance(self.source_type, Unset):
            source_type = self.source_type

        alert_urgency_id = self.alert_urgency_id

        deduplicate_alerts_by_key = self.deduplicate_alerts_by_key

        deduplication_key_kind: str | Unset = UNSET
        if not isinstance(self.deduplication_key_kind, Unset):
            deduplication_key_kind = self.deduplication_key_kind

        deduplication_key_path: None | str | Unset
        if isinstance(self.deduplication_key_path, Unset):
            deduplication_key_path = UNSET
        else:
            deduplication_key_path = self.deduplication_key_path

        deduplication_key_regexp: None | str | Unset
        if isinstance(self.deduplication_key_regexp, Unset):
            deduplication_key_regexp = UNSET
        else:
            deduplication_key_regexp = self.deduplication_key_regexp

        owner_group_ids: list[str] | Unset = UNSET
        if not isinstance(self.owner_group_ids, Unset):
            owner_group_ids = self.owner_group_ids

        alert_template_attributes: dict[str, Any] | None | Unset
        if isinstance(self.alert_template_attributes, Unset):
            alert_template_attributes = UNSET
        elif isinstance(self.alert_template_attributes, NewAlertsSourceDataAttributesAlertTemplateAttributesType0):
            alert_template_attributes = self.alert_template_attributes.to_dict()
        else:
            alert_template_attributes = self.alert_template_attributes

        alert_source_urgency_rules_attributes: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.alert_source_urgency_rules_attributes, Unset):
            alert_source_urgency_rules_attributes = []
            for alert_source_urgency_rules_attributes_item_data in self.alert_source_urgency_rules_attributes:
                alert_source_urgency_rules_attributes_item = alert_source_urgency_rules_attributes_item_data.to_dict()
                alert_source_urgency_rules_attributes.append(alert_source_urgency_rules_attributes_item)

        sourceable_attributes: dict[str, Any] | None | Unset
        if isinstance(self.sourceable_attributes, Unset):
            sourceable_attributes = UNSET
        elif isinstance(self.sourceable_attributes, NewAlertsSourceDataAttributesSourceableAttributesType0):
            sourceable_attributes = self.sourceable_attributes.to_dict()
        else:
            sourceable_attributes = self.sourceable_attributes

        resolution_rule_attributes: dict[str, Any] | None | Unset
        if isinstance(self.resolution_rule_attributes, Unset):
            resolution_rule_attributes = UNSET
        elif isinstance(self.resolution_rule_attributes, NewAlertsSourceDataAttributesResolutionRuleAttributesType0):
            resolution_rule_attributes = self.resolution_rule_attributes.to_dict()
        else:
            resolution_rule_attributes = self.resolution_rule_attributes

        alert_source_fields_attributes: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.alert_source_fields_attributes, Unset):
            alert_source_fields_attributes = []
            for alert_source_fields_attributes_item_data in self.alert_source_fields_attributes:
                alert_source_fields_attributes_item = alert_source_fields_attributes_item_data.to_dict()
                alert_source_fields_attributes.append(alert_source_fields_attributes_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "name": name,
            }
        )
        if source_type is not UNSET:
            field_dict["source_type"] = source_type
        if alert_urgency_id is not UNSET:
            field_dict["alert_urgency_id"] = alert_urgency_id
        if deduplicate_alerts_by_key is not UNSET:
            field_dict["deduplicate_alerts_by_key"] = deduplicate_alerts_by_key
        if deduplication_key_kind is not UNSET:
            field_dict["deduplication_key_kind"] = deduplication_key_kind
        if deduplication_key_path is not UNSET:
            field_dict["deduplication_key_path"] = deduplication_key_path
        if deduplication_key_regexp is not UNSET:
            field_dict["deduplication_key_regexp"] = deduplication_key_regexp
        if owner_group_ids is not UNSET:
            field_dict["owner_group_ids"] = owner_group_ids
        if alert_template_attributes is not UNSET:
            field_dict["alert_template_attributes"] = alert_template_attributes
        if alert_source_urgency_rules_attributes is not UNSET:
            field_dict["alert_source_urgency_rules_attributes"] = alert_source_urgency_rules_attributes
        if sourceable_attributes is not UNSET:
            field_dict["sourceable_attributes"] = sourceable_attributes
        if resolution_rule_attributes is not UNSET:
            field_dict["resolution_rule_attributes"] = resolution_rule_attributes
        if alert_source_fields_attributes is not UNSET:
            field_dict["alert_source_fields_attributes"] = alert_source_fields_attributes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.new_alerts_source_data_attributes_alert_source_fields_attributes_item import (
            NewAlertsSourceDataAttributesAlertSourceFieldsAttributesItem,
        )
        from ..models.new_alerts_source_data_attributes_alert_source_urgency_rules_attributes_item import (
            NewAlertsSourceDataAttributesAlertSourceUrgencyRulesAttributesItem,
        )
        from ..models.new_alerts_source_data_attributes_alert_template_attributes_type_0 import (
            NewAlertsSourceDataAttributesAlertTemplateAttributesType0,
        )
        from ..models.new_alerts_source_data_attributes_resolution_rule_attributes_type_0 import (
            NewAlertsSourceDataAttributesResolutionRuleAttributesType0,
        )
        from ..models.new_alerts_source_data_attributes_sourceable_attributes_type_0 import (
            NewAlertsSourceDataAttributesSourceableAttributesType0,
        )

        d = dict(src_dict)
        name = d.pop("name")

        _source_type = d.pop("source_type", UNSET)
        source_type: NewAlertsSourceDataAttributesSourceType | Unset
        if isinstance(_source_type, Unset):
            source_type = UNSET
        else:
            source_type = check_new_alerts_source_data_attributes_source_type(_source_type)

        alert_urgency_id = d.pop("alert_urgency_id", UNSET)

        deduplicate_alerts_by_key = d.pop("deduplicate_alerts_by_key", UNSET)

        _deduplication_key_kind = d.pop("deduplication_key_kind", UNSET)
        deduplication_key_kind: NewAlertsSourceDataAttributesDeduplicationKeyKind | Unset
        if isinstance(_deduplication_key_kind, Unset):
            deduplication_key_kind = UNSET
        else:
            deduplication_key_kind = check_new_alerts_source_data_attributes_deduplication_key_kind(
                _deduplication_key_kind
            )

        def _parse_deduplication_key_path(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        deduplication_key_path = _parse_deduplication_key_path(d.pop("deduplication_key_path", UNSET))

        def _parse_deduplication_key_regexp(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        deduplication_key_regexp = _parse_deduplication_key_regexp(d.pop("deduplication_key_regexp", UNSET))

        owner_group_ids = cast(list[str], d.pop("owner_group_ids", UNSET))

        def _parse_alert_template_attributes(
            data: object,
        ) -> NewAlertsSourceDataAttributesAlertTemplateAttributesType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                alert_template_attributes_type_0 = NewAlertsSourceDataAttributesAlertTemplateAttributesType0.from_dict(
                    data
                )

                return alert_template_attributes_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(NewAlertsSourceDataAttributesAlertTemplateAttributesType0 | None | Unset, data)

        alert_template_attributes = _parse_alert_template_attributes(d.pop("alert_template_attributes", UNSET))

        _alert_source_urgency_rules_attributes = d.pop("alert_source_urgency_rules_attributes", UNSET)
        alert_source_urgency_rules_attributes: (
            list[NewAlertsSourceDataAttributesAlertSourceUrgencyRulesAttributesItem] | Unset
        ) = UNSET
        if _alert_source_urgency_rules_attributes is not UNSET:
            alert_source_urgency_rules_attributes = []
            for alert_source_urgency_rules_attributes_item_data in _alert_source_urgency_rules_attributes:
                alert_source_urgency_rules_attributes_item = (
                    NewAlertsSourceDataAttributesAlertSourceUrgencyRulesAttributesItem.from_dict(
                        alert_source_urgency_rules_attributes_item_data
                    )
                )

                alert_source_urgency_rules_attributes.append(alert_source_urgency_rules_attributes_item)

        def _parse_sourceable_attributes(
            data: object,
        ) -> NewAlertsSourceDataAttributesSourceableAttributesType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                sourceable_attributes_type_0 = NewAlertsSourceDataAttributesSourceableAttributesType0.from_dict(data)

                return sourceable_attributes_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(NewAlertsSourceDataAttributesSourceableAttributesType0 | None | Unset, data)

        sourceable_attributes = _parse_sourceable_attributes(d.pop("sourceable_attributes", UNSET))

        def _parse_resolution_rule_attributes(
            data: object,
        ) -> NewAlertsSourceDataAttributesResolutionRuleAttributesType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                resolution_rule_attributes_type_0 = (
                    NewAlertsSourceDataAttributesResolutionRuleAttributesType0.from_dict(data)
                )

                return resolution_rule_attributes_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(NewAlertsSourceDataAttributesResolutionRuleAttributesType0 | None | Unset, data)

        resolution_rule_attributes = _parse_resolution_rule_attributes(d.pop("resolution_rule_attributes", UNSET))

        _alert_source_fields_attributes = d.pop("alert_source_fields_attributes", UNSET)
        alert_source_fields_attributes: list[NewAlertsSourceDataAttributesAlertSourceFieldsAttributesItem] | Unset = (
            UNSET
        )
        if _alert_source_fields_attributes is not UNSET:
            alert_source_fields_attributes = []
            for alert_source_fields_attributes_item_data in _alert_source_fields_attributes:
                alert_source_fields_attributes_item = (
                    NewAlertsSourceDataAttributesAlertSourceFieldsAttributesItem.from_dict(
                        alert_source_fields_attributes_item_data
                    )
                )

                alert_source_fields_attributes.append(alert_source_fields_attributes_item)

        new_alerts_source_data_attributes = cls(
            name=name,
            source_type=source_type,
            alert_urgency_id=alert_urgency_id,
            deduplicate_alerts_by_key=deduplicate_alerts_by_key,
            deduplication_key_kind=deduplication_key_kind,
            deduplication_key_path=deduplication_key_path,
            deduplication_key_regexp=deduplication_key_regexp,
            owner_group_ids=owner_group_ids,
            alert_template_attributes=alert_template_attributes,
            alert_source_urgency_rules_attributes=alert_source_urgency_rules_attributes,
            sourceable_attributes=sourceable_attributes,
            resolution_rule_attributes=resolution_rule_attributes,
            alert_source_fields_attributes=alert_source_fields_attributes,
        )

        return new_alerts_source_data_attributes
