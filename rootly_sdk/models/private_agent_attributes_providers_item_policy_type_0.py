from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="PrivateAgentAttributesProvidersItemPolicyType0")


@_attrs_define
class PrivateAgentAttributesProvidersItemPolicyType0:
    """Reported local policy, not credentials or provider connection configuration. Fields are provider-type specific:
    Kubernetes reports namespace scope; search providers report index scope; databases report database/schema scope;
    HTTP reports method/path/header scope; Kafka reports topic and message-read scope; Redis and Valkey report
    diagnostic limits; and each provider family normally reports only its applicable numeric limits. Management
    responses may preserve legacy cross-family fields for backwards compatibility; capability catalog and dispatch use
    provider-scoped execution metadata. Invalid or absent fields are omitted.

        Attributes:
            digest (str | Unset):
            cluster_scoped (bool | Unset):
            pod_logs (bool | Unset):
            maximum_concurrency (int | Unset):
            maximum_attribute_values (int | Unset):
            maximum_documents (int | Unset):
            maximum_entries (int | Unset):
            maximum_exemplars (int | Unset):
            maximum_indices (int | Unset):
            maximum_label_values (int | Unset):
            maximum_nodes (int | Unset):
            maximum_pattern_points (int | Unset):
            maximum_points_per_series (int | Unset):
            maximum_profile_types (int | Unset):
            maximum_query_bytes (int | Unset):
            maximum_request_bytes (int | Unset):
            maximum_response_bytes (int | Unset):
            maximum_range_seconds (int | Unset):
            maximum_rows (int | Unset):
            maximum_result_bytes (int | Unset):
            maximum_items (int | Unset):
            maximum_messages (int | Unset):
            maximum_message_bytes (int | Unset):
            maximum_scan_records (int | Unset):
            maximum_scan_bytes (int | Unset):
            maximum_series (int | Unset):
            maximum_shards (int | Unset):
            maximum_slowlog_entries (int | Unset):
            maximum_spans_per_span_set (int | Unset):
            maximum_stale_values (int | Unset):
            maximum_timeout_seconds (int | Unset):
            maximum_traces (int | Unset):
            stuck_transaction_seconds (int | Unset):
            namespaces (list[str] | Unset):
            allowed_indices (list[str] | Unset):
            timestamp_field (str | Unset):
            database (str | Unset):
            allowed_schemas (list[str] | Unset):
            allowed_methods (list[str] | Unset):
            allowed_path_prefixes (list[str] | Unset):
            allowed_request_headers (list[str] | Unset):
            exposed_response_headers (list[str] | Unset):
            allowed_topics (list[str] | Unset):
            denied_topics (list[str] | Unset):
            include_internal_topics (bool | Unset):
            allow_message_reads (bool | Unset):
            include_message_values (bool | Unset):
    """

    digest: str | Unset = UNSET
    cluster_scoped: bool | Unset = UNSET
    pod_logs: bool | Unset = UNSET
    maximum_concurrency: int | Unset = UNSET
    maximum_attribute_values: int | Unset = UNSET
    maximum_documents: int | Unset = UNSET
    maximum_entries: int | Unset = UNSET
    maximum_exemplars: int | Unset = UNSET
    maximum_indices: int | Unset = UNSET
    maximum_label_values: int | Unset = UNSET
    maximum_nodes: int | Unset = UNSET
    maximum_pattern_points: int | Unset = UNSET
    maximum_points_per_series: int | Unset = UNSET
    maximum_profile_types: int | Unset = UNSET
    maximum_query_bytes: int | Unset = UNSET
    maximum_request_bytes: int | Unset = UNSET
    maximum_response_bytes: int | Unset = UNSET
    maximum_range_seconds: int | Unset = UNSET
    maximum_rows: int | Unset = UNSET
    maximum_result_bytes: int | Unset = UNSET
    maximum_items: int | Unset = UNSET
    maximum_messages: int | Unset = UNSET
    maximum_message_bytes: int | Unset = UNSET
    maximum_scan_records: int | Unset = UNSET
    maximum_scan_bytes: int | Unset = UNSET
    maximum_series: int | Unset = UNSET
    maximum_shards: int | Unset = UNSET
    maximum_slowlog_entries: int | Unset = UNSET
    maximum_spans_per_span_set: int | Unset = UNSET
    maximum_stale_values: int | Unset = UNSET
    maximum_timeout_seconds: int | Unset = UNSET
    maximum_traces: int | Unset = UNSET
    stuck_transaction_seconds: int | Unset = UNSET
    namespaces: list[str] | Unset = UNSET
    allowed_indices: list[str] | Unset = UNSET
    timestamp_field: str | Unset = UNSET
    database: str | Unset = UNSET
    allowed_schemas: list[str] | Unset = UNSET
    allowed_methods: list[str] | Unset = UNSET
    allowed_path_prefixes: list[str] | Unset = UNSET
    allowed_request_headers: list[str] | Unset = UNSET
    exposed_response_headers: list[str] | Unset = UNSET
    allowed_topics: list[str] | Unset = UNSET
    denied_topics: list[str] | Unset = UNSET
    include_internal_topics: bool | Unset = UNSET
    allow_message_reads: bool | Unset = UNSET
    include_message_values: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        digest = self.digest

        cluster_scoped = self.cluster_scoped

        pod_logs = self.pod_logs

        maximum_concurrency = self.maximum_concurrency

        maximum_attribute_values = self.maximum_attribute_values

        maximum_documents = self.maximum_documents

        maximum_entries = self.maximum_entries

        maximum_exemplars = self.maximum_exemplars

        maximum_indices = self.maximum_indices

        maximum_label_values = self.maximum_label_values

        maximum_nodes = self.maximum_nodes

        maximum_pattern_points = self.maximum_pattern_points

        maximum_points_per_series = self.maximum_points_per_series

        maximum_profile_types = self.maximum_profile_types

        maximum_query_bytes = self.maximum_query_bytes

        maximum_request_bytes = self.maximum_request_bytes

        maximum_response_bytes = self.maximum_response_bytes

        maximum_range_seconds = self.maximum_range_seconds

        maximum_rows = self.maximum_rows

        maximum_result_bytes = self.maximum_result_bytes

        maximum_items = self.maximum_items

        maximum_messages = self.maximum_messages

        maximum_message_bytes = self.maximum_message_bytes

        maximum_scan_records = self.maximum_scan_records

        maximum_scan_bytes = self.maximum_scan_bytes

        maximum_series = self.maximum_series

        maximum_shards = self.maximum_shards

        maximum_slowlog_entries = self.maximum_slowlog_entries

        maximum_spans_per_span_set = self.maximum_spans_per_span_set

        maximum_stale_values = self.maximum_stale_values

        maximum_timeout_seconds = self.maximum_timeout_seconds

        maximum_traces = self.maximum_traces

        stuck_transaction_seconds = self.stuck_transaction_seconds

        namespaces: list[str] | Unset = UNSET
        if not isinstance(self.namespaces, Unset):
            namespaces = self.namespaces

        allowed_indices: list[str] | Unset = UNSET
        if not isinstance(self.allowed_indices, Unset):
            allowed_indices = self.allowed_indices

        timestamp_field = self.timestamp_field

        database = self.database

        allowed_schemas: list[str] | Unset = UNSET
        if not isinstance(self.allowed_schemas, Unset):
            allowed_schemas = self.allowed_schemas

        allowed_methods: list[str] | Unset = UNSET
        if not isinstance(self.allowed_methods, Unset):
            allowed_methods = self.allowed_methods

        allowed_path_prefixes: list[str] | Unset = UNSET
        if not isinstance(self.allowed_path_prefixes, Unset):
            allowed_path_prefixes = self.allowed_path_prefixes

        allowed_request_headers: list[str] | Unset = UNSET
        if not isinstance(self.allowed_request_headers, Unset):
            allowed_request_headers = self.allowed_request_headers

        exposed_response_headers: list[str] | Unset = UNSET
        if not isinstance(self.exposed_response_headers, Unset):
            exposed_response_headers = self.exposed_response_headers

        allowed_topics: list[str] | Unset = UNSET
        if not isinstance(self.allowed_topics, Unset):
            allowed_topics = self.allowed_topics

        denied_topics: list[str] | Unset = UNSET
        if not isinstance(self.denied_topics, Unset):
            denied_topics = self.denied_topics

        include_internal_topics = self.include_internal_topics

        allow_message_reads = self.allow_message_reads

        include_message_values = self.include_message_values

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if digest is not UNSET:
            field_dict["digest"] = digest
        if cluster_scoped is not UNSET:
            field_dict["cluster_scoped"] = cluster_scoped
        if pod_logs is not UNSET:
            field_dict["pod_logs"] = pod_logs
        if maximum_concurrency is not UNSET:
            field_dict["maximum_concurrency"] = maximum_concurrency
        if maximum_attribute_values is not UNSET:
            field_dict["maximum_attribute_values"] = maximum_attribute_values
        if maximum_documents is not UNSET:
            field_dict["maximum_documents"] = maximum_documents
        if maximum_entries is not UNSET:
            field_dict["maximum_entries"] = maximum_entries
        if maximum_exemplars is not UNSET:
            field_dict["maximum_exemplars"] = maximum_exemplars
        if maximum_indices is not UNSET:
            field_dict["maximum_indices"] = maximum_indices
        if maximum_label_values is not UNSET:
            field_dict["maximum_label_values"] = maximum_label_values
        if maximum_nodes is not UNSET:
            field_dict["maximum_nodes"] = maximum_nodes
        if maximum_pattern_points is not UNSET:
            field_dict["maximum_pattern_points"] = maximum_pattern_points
        if maximum_points_per_series is not UNSET:
            field_dict["maximum_points_per_series"] = maximum_points_per_series
        if maximum_profile_types is not UNSET:
            field_dict["maximum_profile_types"] = maximum_profile_types
        if maximum_query_bytes is not UNSET:
            field_dict["maximum_query_bytes"] = maximum_query_bytes
        if maximum_request_bytes is not UNSET:
            field_dict["maximum_request_bytes"] = maximum_request_bytes
        if maximum_response_bytes is not UNSET:
            field_dict["maximum_response_bytes"] = maximum_response_bytes
        if maximum_range_seconds is not UNSET:
            field_dict["maximum_range_seconds"] = maximum_range_seconds
        if maximum_rows is not UNSET:
            field_dict["maximum_rows"] = maximum_rows
        if maximum_result_bytes is not UNSET:
            field_dict["maximum_result_bytes"] = maximum_result_bytes
        if maximum_items is not UNSET:
            field_dict["maximum_items"] = maximum_items
        if maximum_messages is not UNSET:
            field_dict["maximum_messages"] = maximum_messages
        if maximum_message_bytes is not UNSET:
            field_dict["maximum_message_bytes"] = maximum_message_bytes
        if maximum_scan_records is not UNSET:
            field_dict["maximum_scan_records"] = maximum_scan_records
        if maximum_scan_bytes is not UNSET:
            field_dict["maximum_scan_bytes"] = maximum_scan_bytes
        if maximum_series is not UNSET:
            field_dict["maximum_series"] = maximum_series
        if maximum_shards is not UNSET:
            field_dict["maximum_shards"] = maximum_shards
        if maximum_slowlog_entries is not UNSET:
            field_dict["maximum_slowlog_entries"] = maximum_slowlog_entries
        if maximum_spans_per_span_set is not UNSET:
            field_dict["maximum_spans_per_span_set"] = maximum_spans_per_span_set
        if maximum_stale_values is not UNSET:
            field_dict["maximum_stale_values"] = maximum_stale_values
        if maximum_timeout_seconds is not UNSET:
            field_dict["maximum_timeout_seconds"] = maximum_timeout_seconds
        if maximum_traces is not UNSET:
            field_dict["maximum_traces"] = maximum_traces
        if stuck_transaction_seconds is not UNSET:
            field_dict["stuck_transaction_seconds"] = stuck_transaction_seconds
        if namespaces is not UNSET:
            field_dict["namespaces"] = namespaces
        if allowed_indices is not UNSET:
            field_dict["allowed_indices"] = allowed_indices
        if timestamp_field is not UNSET:
            field_dict["timestamp_field"] = timestamp_field
        if database is not UNSET:
            field_dict["database"] = database
        if allowed_schemas is not UNSET:
            field_dict["allowed_schemas"] = allowed_schemas
        if allowed_methods is not UNSET:
            field_dict["allowed_methods"] = allowed_methods
        if allowed_path_prefixes is not UNSET:
            field_dict["allowed_path_prefixes"] = allowed_path_prefixes
        if allowed_request_headers is not UNSET:
            field_dict["allowed_request_headers"] = allowed_request_headers
        if exposed_response_headers is not UNSET:
            field_dict["exposed_response_headers"] = exposed_response_headers
        if allowed_topics is not UNSET:
            field_dict["allowed_topics"] = allowed_topics
        if denied_topics is not UNSET:
            field_dict["denied_topics"] = denied_topics
        if include_internal_topics is not UNSET:
            field_dict["include_internal_topics"] = include_internal_topics
        if allow_message_reads is not UNSET:
            field_dict["allow_message_reads"] = allow_message_reads
        if include_message_values is not UNSET:
            field_dict["include_message_values"] = include_message_values

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        digest = d.pop("digest", UNSET)

        cluster_scoped = d.pop("cluster_scoped", UNSET)

        pod_logs = d.pop("pod_logs", UNSET)

        maximum_concurrency = d.pop("maximum_concurrency", UNSET)

        maximum_attribute_values = d.pop("maximum_attribute_values", UNSET)

        maximum_documents = d.pop("maximum_documents", UNSET)

        maximum_entries = d.pop("maximum_entries", UNSET)

        maximum_exemplars = d.pop("maximum_exemplars", UNSET)

        maximum_indices = d.pop("maximum_indices", UNSET)

        maximum_label_values = d.pop("maximum_label_values", UNSET)

        maximum_nodes = d.pop("maximum_nodes", UNSET)

        maximum_pattern_points = d.pop("maximum_pattern_points", UNSET)

        maximum_points_per_series = d.pop("maximum_points_per_series", UNSET)

        maximum_profile_types = d.pop("maximum_profile_types", UNSET)

        maximum_query_bytes = d.pop("maximum_query_bytes", UNSET)

        maximum_request_bytes = d.pop("maximum_request_bytes", UNSET)

        maximum_response_bytes = d.pop("maximum_response_bytes", UNSET)

        maximum_range_seconds = d.pop("maximum_range_seconds", UNSET)

        maximum_rows = d.pop("maximum_rows", UNSET)

        maximum_result_bytes = d.pop("maximum_result_bytes", UNSET)

        maximum_items = d.pop("maximum_items", UNSET)

        maximum_messages = d.pop("maximum_messages", UNSET)

        maximum_message_bytes = d.pop("maximum_message_bytes", UNSET)

        maximum_scan_records = d.pop("maximum_scan_records", UNSET)

        maximum_scan_bytes = d.pop("maximum_scan_bytes", UNSET)

        maximum_series = d.pop("maximum_series", UNSET)

        maximum_shards = d.pop("maximum_shards", UNSET)

        maximum_slowlog_entries = d.pop("maximum_slowlog_entries", UNSET)

        maximum_spans_per_span_set = d.pop("maximum_spans_per_span_set", UNSET)

        maximum_stale_values = d.pop("maximum_stale_values", UNSET)

        maximum_timeout_seconds = d.pop("maximum_timeout_seconds", UNSET)

        maximum_traces = d.pop("maximum_traces", UNSET)

        stuck_transaction_seconds = d.pop("stuck_transaction_seconds", UNSET)

        namespaces = cast(list[str], d.pop("namespaces", UNSET))

        allowed_indices = cast(list[str], d.pop("allowed_indices", UNSET))

        timestamp_field = d.pop("timestamp_field", UNSET)

        database = d.pop("database", UNSET)

        allowed_schemas = cast(list[str], d.pop("allowed_schemas", UNSET))

        allowed_methods = cast(list[str], d.pop("allowed_methods", UNSET))

        allowed_path_prefixes = cast(list[str], d.pop("allowed_path_prefixes", UNSET))

        allowed_request_headers = cast(list[str], d.pop("allowed_request_headers", UNSET))

        exposed_response_headers = cast(list[str], d.pop("exposed_response_headers", UNSET))

        allowed_topics = cast(list[str], d.pop("allowed_topics", UNSET))

        denied_topics = cast(list[str], d.pop("denied_topics", UNSET))

        include_internal_topics = d.pop("include_internal_topics", UNSET)

        allow_message_reads = d.pop("allow_message_reads", UNSET)

        include_message_values = d.pop("include_message_values", UNSET)

        private_agent_attributes_providers_item_policy_type_0 = cls(
            digest=digest,
            cluster_scoped=cluster_scoped,
            pod_logs=pod_logs,
            maximum_concurrency=maximum_concurrency,
            maximum_attribute_values=maximum_attribute_values,
            maximum_documents=maximum_documents,
            maximum_entries=maximum_entries,
            maximum_exemplars=maximum_exemplars,
            maximum_indices=maximum_indices,
            maximum_label_values=maximum_label_values,
            maximum_nodes=maximum_nodes,
            maximum_pattern_points=maximum_pattern_points,
            maximum_points_per_series=maximum_points_per_series,
            maximum_profile_types=maximum_profile_types,
            maximum_query_bytes=maximum_query_bytes,
            maximum_request_bytes=maximum_request_bytes,
            maximum_response_bytes=maximum_response_bytes,
            maximum_range_seconds=maximum_range_seconds,
            maximum_rows=maximum_rows,
            maximum_result_bytes=maximum_result_bytes,
            maximum_items=maximum_items,
            maximum_messages=maximum_messages,
            maximum_message_bytes=maximum_message_bytes,
            maximum_scan_records=maximum_scan_records,
            maximum_scan_bytes=maximum_scan_bytes,
            maximum_series=maximum_series,
            maximum_shards=maximum_shards,
            maximum_slowlog_entries=maximum_slowlog_entries,
            maximum_spans_per_span_set=maximum_spans_per_span_set,
            maximum_stale_values=maximum_stale_values,
            maximum_timeout_seconds=maximum_timeout_seconds,
            maximum_traces=maximum_traces,
            stuck_transaction_seconds=stuck_transaction_seconds,
            namespaces=namespaces,
            allowed_indices=allowed_indices,
            timestamp_field=timestamp_field,
            database=database,
            allowed_schemas=allowed_schemas,
            allowed_methods=allowed_methods,
            allowed_path_prefixes=allowed_path_prefixes,
            allowed_request_headers=allowed_request_headers,
            exposed_response_headers=exposed_response_headers,
            allowed_topics=allowed_topics,
            denied_topics=denied_topics,
            include_internal_topics=include_internal_topics,
            allow_message_reads=allow_message_reads,
            include_message_values=include_message_values,
        )

        return private_agent_attributes_providers_item_policy_type_0
