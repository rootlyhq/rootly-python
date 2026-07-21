from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.errors_list import ErrorsList
from ...models.incident_list import IncidentList
from ...models.list_incidents_include import ListIncidentsInclude
from ...models.list_incidents_sort import ListIncidentsSort
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    pageafter: str | Unset = UNSET,
    pagenumber: int | Unset = UNSET,
    pagesize: int | Unset = UNSET,
    filtersearch: str | Unset = UNSET,
    filterkind: str | Unset = UNSET,
    filterstatus: str | Unset = UNSET,
    filterprivate: str | Unset = UNSET,
    filteruser_id: int | Unset = UNSET,
    filterseverity: str | Unset = UNSET,
    filterseverity_id: str | Unset = UNSET,
    filterlabels: str | Unset = UNSET,
    filtertypes: str | Unset = UNSET,
    filtertype_ids: str | Unset = UNSET,
    filterenvironments: str | Unset = UNSET,
    filterenvironment_ids: str | Unset = UNSET,
    filterfunctionalities: str | Unset = UNSET,
    filterfunctionality_ids: str | Unset = UNSET,
    filterfunctionality_names: str | Unset = UNSET,
    filterservices: str | Unset = UNSET,
    filterservice_ids: str | Unset = UNSET,
    filterservice_names: str | Unset = UNSET,
    filterteams: str | Unset = UNSET,
    filterteam_ids: str | Unset = UNSET,
    filterteam_names: str | Unset = UNSET,
    filtercause: str | Unset = UNSET,
    filtercause_ids: str | Unset = UNSET,
    filtercustom_field_selected_option_ids: str | Unset = UNSET,
    filterslack_channel_id: str | Unset = UNSET,
    filtersequential_id: str | Unset = UNSET,
    filtercreated_atgt: str | Unset = UNSET,
    filtercreated_atgte: str | Unset = UNSET,
    filtercreated_atlt: str | Unset = UNSET,
    filtercreated_atlte: str | Unset = UNSET,
    filterupdated_atgt: str | Unset = UNSET,
    filterupdated_atgte: str | Unset = UNSET,
    filterupdated_atlt: str | Unset = UNSET,
    filterupdated_atlte: str | Unset = UNSET,
    filterstarted_atgt: str | Unset = UNSET,
    filterstarted_atgte: str | Unset = UNSET,
    filterstarted_atlt: str | Unset = UNSET,
    filterstarted_atlte: str | Unset = UNSET,
    filterdetected_atgt: str | Unset = UNSET,
    filterdetected_atgte: str | Unset = UNSET,
    filterdetected_atlt: str | Unset = UNSET,
    filterdetected_atlte: str | Unset = UNSET,
    filteracknowledged_atgt: str | Unset = UNSET,
    filteracknowledged_atgte: str | Unset = UNSET,
    filteracknowledged_atlt: str | Unset = UNSET,
    filteracknowledged_atlte: str | Unset = UNSET,
    filtermitigated_atgt: str | Unset = UNSET,
    filtermitigated_atgte: str | Unset = UNSET,
    filtermitigated_atlt: str | Unset = UNSET,
    filtermitigated_atlte: str | Unset = UNSET,
    filterresolved_atgt: str | Unset = UNSET,
    filterresolved_atgte: str | Unset = UNSET,
    filterresolved_atlt: str | Unset = UNSET,
    filterresolved_atlte: str | Unset = UNSET,
    filterclosed_atgt: str | Unset = UNSET,
    filterclosed_atgte: str | Unset = UNSET,
    filterclosed_atlt: str | Unset = UNSET,
    filterclosed_atlte: str | Unset = UNSET,
    filterin_triage_atgt: str | Unset = UNSET,
    filterin_triage_atgte: str | Unset = UNSET,
    filterin_triage_atlt: str | Unset = UNSET,
    filterin_triage_atlte: str | Unset = UNSET,
    filterkindeq: str | Unset = UNSET,
    filterkindnot_eq: str | Unset = UNSET,
    filterkindin: str | Unset = UNSET,
    filterkindnot_in: str | Unset = UNSET,
    filterstatuseq: str | Unset = UNSET,
    filterstatusnot_eq: str | Unset = UNSET,
    filterstatusin: str | Unset = UNSET,
    filterstatusnot_in: str | Unset = UNSET,
    filterprivateeq: str | Unset = UNSET,
    filterprivatenot_eq: str | Unset = UNSET,
    filterprivatein: str | Unset = UNSET,
    filterprivatenot_in: str | Unset = UNSET,
    filteruser_ideq: str | Unset = UNSET,
    filteruser_idnot_eq: str | Unset = UNSET,
    filteruser_idin: str | Unset = UNSET,
    filteruser_idnot_in: str | Unset = UNSET,
    filterseverityeq: str | Unset = UNSET,
    filterseveritynot_eq: str | Unset = UNSET,
    filterseverityin: str | Unset = UNSET,
    filterseveritynot_in: str | Unset = UNSET,
    filterseverity_ideq: str | Unset = UNSET,
    filterseverity_idnot_eq: str | Unset = UNSET,
    filterseverity_idin: str | Unset = UNSET,
    filterseverity_idnot_in: str | Unset = UNSET,
    filterlabelseq: str | Unset = UNSET,
    filterlabelsnot_eq: str | Unset = UNSET,
    filterlabelsin: str | Unset = UNSET,
    filterlabelsnot_in: str | Unset = UNSET,
    filterzendesk_ticket_ideq: str | Unset = UNSET,
    filterzendesk_ticket_idnot_eq: str | Unset = UNSET,
    filterzendesk_ticket_idin: str | Unset = UNSET,
    filterzendesk_ticket_idnot_in: str | Unset = UNSET,
    filtersequential_ideq: str | Unset = UNSET,
    filtersequential_idnot_eq: str | Unset = UNSET,
    filtersequential_idin: str | Unset = UNSET,
    filtersequential_idnot_in: str | Unset = UNSET,
    filtertypeseq: str | Unset = UNSET,
    filtertypesnot_eq: str | Unset = UNSET,
    filtertypesin: str | Unset = UNSET,
    filtertypesnot_in: str | Unset = UNSET,
    filtertype_idseq: str | Unset = UNSET,
    filtertype_idsnot_eq: str | Unset = UNSET,
    filtertype_idsin: str | Unset = UNSET,
    filtertype_idsnot_in: str | Unset = UNSET,
    filterenvironmentseq: str | Unset = UNSET,
    filterenvironmentsnot_eq: str | Unset = UNSET,
    filterenvironmentsin: str | Unset = UNSET,
    filterenvironmentsnot_in: str | Unset = UNSET,
    filterenvironment_idseq: str | Unset = UNSET,
    filterenvironment_idsnot_eq: str | Unset = UNSET,
    filterenvironment_idsin: str | Unset = UNSET,
    filterenvironment_idsnot_in: str | Unset = UNSET,
    filterserviceseq: str | Unset = UNSET,
    filterservicesnot_eq: str | Unset = UNSET,
    filterservicesin: str | Unset = UNSET,
    filterservicesnot_in: str | Unset = UNSET,
    filterservice_idseq: str | Unset = UNSET,
    filterservice_idsnot_eq: str | Unset = UNSET,
    filterservice_idsin: str | Unset = UNSET,
    filterservice_idsnot_in: str | Unset = UNSET,
    filterservice_nameseq: str | Unset = UNSET,
    filterservice_namesnot_eq: str | Unset = UNSET,
    filterservice_namesin: str | Unset = UNSET,
    filterservice_namesnot_in: str | Unset = UNSET,
    filterfunctionalitieseq: str | Unset = UNSET,
    filterfunctionalitiesnot_eq: str | Unset = UNSET,
    filterfunctionalitiesin: str | Unset = UNSET,
    filterfunctionalitiesnot_in: str | Unset = UNSET,
    filterfunctionality_idseq: str | Unset = UNSET,
    filterfunctionality_idsnot_eq: str | Unset = UNSET,
    filterfunctionality_idsin: str | Unset = UNSET,
    filterfunctionality_idsnot_in: str | Unset = UNSET,
    filterfunctionality_nameseq: str | Unset = UNSET,
    filterfunctionality_namesnot_eq: str | Unset = UNSET,
    filterfunctionality_namesin: str | Unset = UNSET,
    filterfunctionality_namesnot_in: str | Unset = UNSET,
    filtercauseseq: str | Unset = UNSET,
    filtercausesnot_eq: str | Unset = UNSET,
    filtercausesin: str | Unset = UNSET,
    filtercausesnot_in: str | Unset = UNSET,
    filtercause_idseq: str | Unset = UNSET,
    filtercause_idsnot_eq: str | Unset = UNSET,
    filtercause_idsin: str | Unset = UNSET,
    filtercause_idsnot_in: str | Unset = UNSET,
    filterteamseq: str | Unset = UNSET,
    filterteamsnot_eq: str | Unset = UNSET,
    filterteamsin: str | Unset = UNSET,
    filterteamsnot_in: str | Unset = UNSET,
    filterteam_idseq: str | Unset = UNSET,
    filterteam_idsnot_eq: str | Unset = UNSET,
    filterteam_idsin: str | Unset = UNSET,
    filterteam_idsnot_in: str | Unset = UNSET,
    filterteam_nameseq: str | Unset = UNSET,
    filterteam_namesnot_eq: str | Unset = UNSET,
    filterteam_namesin: str | Unset = UNSET,
    filterteam_namesnot_in: str | Unset = UNSET,
    sort: ListIncidentsSort | Unset = UNSET,
    include: ListIncidentsInclude | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["page[after]"] = pageafter

    params["page[number]"] = pagenumber

    params["page[size]"] = pagesize

    params["filter[search]"] = filtersearch

    params["filter[kind]"] = filterkind

    params["filter[status]"] = filterstatus

    params["filter[private]"] = filterprivate

    params["filter[user_id]"] = filteruser_id

    params["filter[severity]"] = filterseverity

    params["filter[severity_id]"] = filterseverity_id

    params["filter[labels]"] = filterlabels

    params["filter[types]"] = filtertypes

    params["filter[type_ids]"] = filtertype_ids

    params["filter[environments]"] = filterenvironments

    params["filter[environment_ids]"] = filterenvironment_ids

    params["filter[functionalities]"] = filterfunctionalities

    params["filter[functionality_ids]"] = filterfunctionality_ids

    params["filter[functionality_names]"] = filterfunctionality_names

    params["filter[services]"] = filterservices

    params["filter[service_ids]"] = filterservice_ids

    params["filter[service_names]"] = filterservice_names

    params["filter[teams]"] = filterteams

    params["filter[team_ids]"] = filterteam_ids

    params["filter[team_names]"] = filterteam_names

    params["filter[cause]"] = filtercause

    params["filter[cause_ids]"] = filtercause_ids

    params["filter[custom_field_selected_option_ids]"] = filtercustom_field_selected_option_ids

    params["filter[slack_channel_id]"] = filterslack_channel_id

    params["filter[sequential_id]"] = filtersequential_id

    params["filter[created_at][gt]"] = filtercreated_atgt

    params["filter[created_at][gte]"] = filtercreated_atgte

    params["filter[created_at][lt]"] = filtercreated_atlt

    params["filter[created_at][lte]"] = filtercreated_atlte

    params["filter[updated_at][gt]"] = filterupdated_atgt

    params["filter[updated_at][gte]"] = filterupdated_atgte

    params["filter[updated_at][lt]"] = filterupdated_atlt

    params["filter[updated_at][lte]"] = filterupdated_atlte

    params["filter[started_at][gt]"] = filterstarted_atgt

    params["filter[started_at][gte]"] = filterstarted_atgte

    params["filter[started_at][lt]"] = filterstarted_atlt

    params["filter[started_at][lte]"] = filterstarted_atlte

    params["filter[detected_at][gt]"] = filterdetected_atgt

    params["filter[detected_at][gte]"] = filterdetected_atgte

    params["filter[detected_at][lt]"] = filterdetected_atlt

    params["filter[detected_at][lte]"] = filterdetected_atlte

    params["filter[acknowledged_at][gt]"] = filteracknowledged_atgt

    params["filter[acknowledged_at][gte]"] = filteracknowledged_atgte

    params["filter[acknowledged_at][lt]"] = filteracknowledged_atlt

    params["filter[acknowledged_at][lte]"] = filteracknowledged_atlte

    params["filter[mitigated_at][gt]"] = filtermitigated_atgt

    params["filter[mitigated_at][gte]"] = filtermitigated_atgte

    params["filter[mitigated_at][lt]"] = filtermitigated_atlt

    params["filter[mitigated_at][lte]"] = filtermitigated_atlte

    params["filter[resolved_at][gt]"] = filterresolved_atgt

    params["filter[resolved_at][gte]"] = filterresolved_atgte

    params["filter[resolved_at][lt]"] = filterresolved_atlt

    params["filter[resolved_at][lte]"] = filterresolved_atlte

    params["filter[closed_at][gt]"] = filterclosed_atgt

    params["filter[closed_at][gte]"] = filterclosed_atgte

    params["filter[closed_at][lt]"] = filterclosed_atlt

    params["filter[closed_at][lte]"] = filterclosed_atlte

    params["filter[in_triage_at][gt]"] = filterin_triage_atgt

    params["filter[in_triage_at][gte]"] = filterin_triage_atgte

    params["filter[in_triage_at][lt]"] = filterin_triage_atlt

    params["filter[in_triage_at][lte]"] = filterin_triage_atlte

    params["filter[kind][eq]"] = filterkindeq

    params["filter[kind][not_eq]"] = filterkindnot_eq

    params["filter[kind][in]"] = filterkindin

    params["filter[kind][not_in]"] = filterkindnot_in

    params["filter[status][eq]"] = filterstatuseq

    params["filter[status][not_eq]"] = filterstatusnot_eq

    params["filter[status][in]"] = filterstatusin

    params["filter[status][not_in]"] = filterstatusnot_in

    params["filter[private][eq]"] = filterprivateeq

    params["filter[private][not_eq]"] = filterprivatenot_eq

    params["filter[private][in]"] = filterprivatein

    params["filter[private][not_in]"] = filterprivatenot_in

    params["filter[user_id][eq]"] = filteruser_ideq

    params["filter[user_id][not_eq]"] = filteruser_idnot_eq

    params["filter[user_id][in]"] = filteruser_idin

    params["filter[user_id][not_in]"] = filteruser_idnot_in

    params["filter[severity][eq]"] = filterseverityeq

    params["filter[severity][not_eq]"] = filterseveritynot_eq

    params["filter[severity][in]"] = filterseverityin

    params["filter[severity][not_in]"] = filterseveritynot_in

    params["filter[severity_id][eq]"] = filterseverity_ideq

    params["filter[severity_id][not_eq]"] = filterseverity_idnot_eq

    params["filter[severity_id][in]"] = filterseverity_idin

    params["filter[severity_id][not_in]"] = filterseverity_idnot_in

    params["filter[labels][eq]"] = filterlabelseq

    params["filter[labels][not_eq]"] = filterlabelsnot_eq

    params["filter[labels][in]"] = filterlabelsin

    params["filter[labels][not_in]"] = filterlabelsnot_in

    params["filter[zendesk_ticket_id][eq]"] = filterzendesk_ticket_ideq

    params["filter[zendesk_ticket_id][not_eq]"] = filterzendesk_ticket_idnot_eq

    params["filter[zendesk_ticket_id][in]"] = filterzendesk_ticket_idin

    params["filter[zendesk_ticket_id][not_in]"] = filterzendesk_ticket_idnot_in

    params["filter[sequential_id][eq]"] = filtersequential_ideq

    params["filter[sequential_id][not_eq]"] = filtersequential_idnot_eq

    params["filter[sequential_id][in]"] = filtersequential_idin

    params["filter[sequential_id][not_in]"] = filtersequential_idnot_in

    params["filter[types][eq]"] = filtertypeseq

    params["filter[types][not_eq]"] = filtertypesnot_eq

    params["filter[types][in]"] = filtertypesin

    params["filter[types][not_in]"] = filtertypesnot_in

    params["filter[type_ids][eq]"] = filtertype_idseq

    params["filter[type_ids][not_eq]"] = filtertype_idsnot_eq

    params["filter[type_ids][in]"] = filtertype_idsin

    params["filter[type_ids][not_in]"] = filtertype_idsnot_in

    params["filter[environments][eq]"] = filterenvironmentseq

    params["filter[environments][not_eq]"] = filterenvironmentsnot_eq

    params["filter[environments][in]"] = filterenvironmentsin

    params["filter[environments][not_in]"] = filterenvironmentsnot_in

    params["filter[environment_ids][eq]"] = filterenvironment_idseq

    params["filter[environment_ids][not_eq]"] = filterenvironment_idsnot_eq

    params["filter[environment_ids][in]"] = filterenvironment_idsin

    params["filter[environment_ids][not_in]"] = filterenvironment_idsnot_in

    params["filter[services][eq]"] = filterserviceseq

    params["filter[services][not_eq]"] = filterservicesnot_eq

    params["filter[services][in]"] = filterservicesin

    params["filter[services][not_in]"] = filterservicesnot_in

    params["filter[service_ids][eq]"] = filterservice_idseq

    params["filter[service_ids][not_eq]"] = filterservice_idsnot_eq

    params["filter[service_ids][in]"] = filterservice_idsin

    params["filter[service_ids][not_in]"] = filterservice_idsnot_in

    params["filter[service_names][eq]"] = filterservice_nameseq

    params["filter[service_names][not_eq]"] = filterservice_namesnot_eq

    params["filter[service_names][in]"] = filterservice_namesin

    params["filter[service_names][not_in]"] = filterservice_namesnot_in

    params["filter[functionalities][eq]"] = filterfunctionalitieseq

    params["filter[functionalities][not_eq]"] = filterfunctionalitiesnot_eq

    params["filter[functionalities][in]"] = filterfunctionalitiesin

    params["filter[functionalities][not_in]"] = filterfunctionalitiesnot_in

    params["filter[functionality_ids][eq]"] = filterfunctionality_idseq

    params["filter[functionality_ids][not_eq]"] = filterfunctionality_idsnot_eq

    params["filter[functionality_ids][in]"] = filterfunctionality_idsin

    params["filter[functionality_ids][not_in]"] = filterfunctionality_idsnot_in

    params["filter[functionality_names][eq]"] = filterfunctionality_nameseq

    params["filter[functionality_names][not_eq]"] = filterfunctionality_namesnot_eq

    params["filter[functionality_names][in]"] = filterfunctionality_namesin

    params["filter[functionality_names][not_in]"] = filterfunctionality_namesnot_in

    params["filter[causes][eq]"] = filtercauseseq

    params["filter[causes][not_eq]"] = filtercausesnot_eq

    params["filter[causes][in]"] = filtercausesin

    params["filter[causes][not_in]"] = filtercausesnot_in

    params["filter[cause_ids][eq]"] = filtercause_idseq

    params["filter[cause_ids][not_eq]"] = filtercause_idsnot_eq

    params["filter[cause_ids][in]"] = filtercause_idsin

    params["filter[cause_ids][not_in]"] = filtercause_idsnot_in

    params["filter[teams][eq]"] = filterteamseq

    params["filter[teams][not_eq]"] = filterteamsnot_eq

    params["filter[teams][in]"] = filterteamsin

    params["filter[teams][not_in]"] = filterteamsnot_in

    params["filter[team_ids][eq]"] = filterteam_idseq

    params["filter[team_ids][not_eq]"] = filterteam_idsnot_eq

    params["filter[team_ids][in]"] = filterteam_idsin

    params["filter[team_ids][not_in]"] = filterteam_idsnot_in

    params["filter[team_names][eq]"] = filterteam_nameseq

    params["filter[team_names][not_eq]"] = filterteam_namesnot_eq

    params["filter[team_names][in]"] = filterteam_namesin

    params["filter[team_names][not_in]"] = filterteam_namesnot_in

    json_sort: str | Unset = UNSET
    if not isinstance(sort, Unset):
        json_sort = sort

    params["sort"] = json_sort

    json_include: str | Unset = UNSET
    if not isinstance(include, Unset):
        json_include = include

    params["include"] = json_include

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/incidents",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorsList | IncidentList | None:
    if response.status_code == 200:
        response_200 = IncidentList.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ErrorsList.from_dict(response.json())

        return response_400

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ErrorsList | IncidentList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    pageafter: str | Unset = UNSET,
    pagenumber: int | Unset = UNSET,
    pagesize: int | Unset = UNSET,
    filtersearch: str | Unset = UNSET,
    filterkind: str | Unset = UNSET,
    filterstatus: str | Unset = UNSET,
    filterprivate: str | Unset = UNSET,
    filteruser_id: int | Unset = UNSET,
    filterseverity: str | Unset = UNSET,
    filterseverity_id: str | Unset = UNSET,
    filterlabels: str | Unset = UNSET,
    filtertypes: str | Unset = UNSET,
    filtertype_ids: str | Unset = UNSET,
    filterenvironments: str | Unset = UNSET,
    filterenvironment_ids: str | Unset = UNSET,
    filterfunctionalities: str | Unset = UNSET,
    filterfunctionality_ids: str | Unset = UNSET,
    filterfunctionality_names: str | Unset = UNSET,
    filterservices: str | Unset = UNSET,
    filterservice_ids: str | Unset = UNSET,
    filterservice_names: str | Unset = UNSET,
    filterteams: str | Unset = UNSET,
    filterteam_ids: str | Unset = UNSET,
    filterteam_names: str | Unset = UNSET,
    filtercause: str | Unset = UNSET,
    filtercause_ids: str | Unset = UNSET,
    filtercustom_field_selected_option_ids: str | Unset = UNSET,
    filterslack_channel_id: str | Unset = UNSET,
    filtersequential_id: str | Unset = UNSET,
    filtercreated_atgt: str | Unset = UNSET,
    filtercreated_atgte: str | Unset = UNSET,
    filtercreated_atlt: str | Unset = UNSET,
    filtercreated_atlte: str | Unset = UNSET,
    filterupdated_atgt: str | Unset = UNSET,
    filterupdated_atgte: str | Unset = UNSET,
    filterupdated_atlt: str | Unset = UNSET,
    filterupdated_atlte: str | Unset = UNSET,
    filterstarted_atgt: str | Unset = UNSET,
    filterstarted_atgte: str | Unset = UNSET,
    filterstarted_atlt: str | Unset = UNSET,
    filterstarted_atlte: str | Unset = UNSET,
    filterdetected_atgt: str | Unset = UNSET,
    filterdetected_atgte: str | Unset = UNSET,
    filterdetected_atlt: str | Unset = UNSET,
    filterdetected_atlte: str | Unset = UNSET,
    filteracknowledged_atgt: str | Unset = UNSET,
    filteracknowledged_atgte: str | Unset = UNSET,
    filteracknowledged_atlt: str | Unset = UNSET,
    filteracknowledged_atlte: str | Unset = UNSET,
    filtermitigated_atgt: str | Unset = UNSET,
    filtermitigated_atgte: str | Unset = UNSET,
    filtermitigated_atlt: str | Unset = UNSET,
    filtermitigated_atlte: str | Unset = UNSET,
    filterresolved_atgt: str | Unset = UNSET,
    filterresolved_atgte: str | Unset = UNSET,
    filterresolved_atlt: str | Unset = UNSET,
    filterresolved_atlte: str | Unset = UNSET,
    filterclosed_atgt: str | Unset = UNSET,
    filterclosed_atgte: str | Unset = UNSET,
    filterclosed_atlt: str | Unset = UNSET,
    filterclosed_atlte: str | Unset = UNSET,
    filterin_triage_atgt: str | Unset = UNSET,
    filterin_triage_atgte: str | Unset = UNSET,
    filterin_triage_atlt: str | Unset = UNSET,
    filterin_triage_atlte: str | Unset = UNSET,
    filterkindeq: str | Unset = UNSET,
    filterkindnot_eq: str | Unset = UNSET,
    filterkindin: str | Unset = UNSET,
    filterkindnot_in: str | Unset = UNSET,
    filterstatuseq: str | Unset = UNSET,
    filterstatusnot_eq: str | Unset = UNSET,
    filterstatusin: str | Unset = UNSET,
    filterstatusnot_in: str | Unset = UNSET,
    filterprivateeq: str | Unset = UNSET,
    filterprivatenot_eq: str | Unset = UNSET,
    filterprivatein: str | Unset = UNSET,
    filterprivatenot_in: str | Unset = UNSET,
    filteruser_ideq: str | Unset = UNSET,
    filteruser_idnot_eq: str | Unset = UNSET,
    filteruser_idin: str | Unset = UNSET,
    filteruser_idnot_in: str | Unset = UNSET,
    filterseverityeq: str | Unset = UNSET,
    filterseveritynot_eq: str | Unset = UNSET,
    filterseverityin: str | Unset = UNSET,
    filterseveritynot_in: str | Unset = UNSET,
    filterseverity_ideq: str | Unset = UNSET,
    filterseverity_idnot_eq: str | Unset = UNSET,
    filterseverity_idin: str | Unset = UNSET,
    filterseverity_idnot_in: str | Unset = UNSET,
    filterlabelseq: str | Unset = UNSET,
    filterlabelsnot_eq: str | Unset = UNSET,
    filterlabelsin: str | Unset = UNSET,
    filterlabelsnot_in: str | Unset = UNSET,
    filterzendesk_ticket_ideq: str | Unset = UNSET,
    filterzendesk_ticket_idnot_eq: str | Unset = UNSET,
    filterzendesk_ticket_idin: str | Unset = UNSET,
    filterzendesk_ticket_idnot_in: str | Unset = UNSET,
    filtersequential_ideq: str | Unset = UNSET,
    filtersequential_idnot_eq: str | Unset = UNSET,
    filtersequential_idin: str | Unset = UNSET,
    filtersequential_idnot_in: str | Unset = UNSET,
    filtertypeseq: str | Unset = UNSET,
    filtertypesnot_eq: str | Unset = UNSET,
    filtertypesin: str | Unset = UNSET,
    filtertypesnot_in: str | Unset = UNSET,
    filtertype_idseq: str | Unset = UNSET,
    filtertype_idsnot_eq: str | Unset = UNSET,
    filtertype_idsin: str | Unset = UNSET,
    filtertype_idsnot_in: str | Unset = UNSET,
    filterenvironmentseq: str | Unset = UNSET,
    filterenvironmentsnot_eq: str | Unset = UNSET,
    filterenvironmentsin: str | Unset = UNSET,
    filterenvironmentsnot_in: str | Unset = UNSET,
    filterenvironment_idseq: str | Unset = UNSET,
    filterenvironment_idsnot_eq: str | Unset = UNSET,
    filterenvironment_idsin: str | Unset = UNSET,
    filterenvironment_idsnot_in: str | Unset = UNSET,
    filterserviceseq: str | Unset = UNSET,
    filterservicesnot_eq: str | Unset = UNSET,
    filterservicesin: str | Unset = UNSET,
    filterservicesnot_in: str | Unset = UNSET,
    filterservice_idseq: str | Unset = UNSET,
    filterservice_idsnot_eq: str | Unset = UNSET,
    filterservice_idsin: str | Unset = UNSET,
    filterservice_idsnot_in: str | Unset = UNSET,
    filterservice_nameseq: str | Unset = UNSET,
    filterservice_namesnot_eq: str | Unset = UNSET,
    filterservice_namesin: str | Unset = UNSET,
    filterservice_namesnot_in: str | Unset = UNSET,
    filterfunctionalitieseq: str | Unset = UNSET,
    filterfunctionalitiesnot_eq: str | Unset = UNSET,
    filterfunctionalitiesin: str | Unset = UNSET,
    filterfunctionalitiesnot_in: str | Unset = UNSET,
    filterfunctionality_idseq: str | Unset = UNSET,
    filterfunctionality_idsnot_eq: str | Unset = UNSET,
    filterfunctionality_idsin: str | Unset = UNSET,
    filterfunctionality_idsnot_in: str | Unset = UNSET,
    filterfunctionality_nameseq: str | Unset = UNSET,
    filterfunctionality_namesnot_eq: str | Unset = UNSET,
    filterfunctionality_namesin: str | Unset = UNSET,
    filterfunctionality_namesnot_in: str | Unset = UNSET,
    filtercauseseq: str | Unset = UNSET,
    filtercausesnot_eq: str | Unset = UNSET,
    filtercausesin: str | Unset = UNSET,
    filtercausesnot_in: str | Unset = UNSET,
    filtercause_idseq: str | Unset = UNSET,
    filtercause_idsnot_eq: str | Unset = UNSET,
    filtercause_idsin: str | Unset = UNSET,
    filtercause_idsnot_in: str | Unset = UNSET,
    filterteamseq: str | Unset = UNSET,
    filterteamsnot_eq: str | Unset = UNSET,
    filterteamsin: str | Unset = UNSET,
    filterteamsnot_in: str | Unset = UNSET,
    filterteam_idseq: str | Unset = UNSET,
    filterteam_idsnot_eq: str | Unset = UNSET,
    filterteam_idsin: str | Unset = UNSET,
    filterteam_idsnot_in: str | Unset = UNSET,
    filterteam_nameseq: str | Unset = UNSET,
    filterteam_namesnot_eq: str | Unset = UNSET,
    filterteam_namesin: str | Unset = UNSET,
    filterteam_namesnot_in: str | Unset = UNSET,
    sort: ListIncidentsSort | Unset = UNSET,
    include: ListIncidentsInclude | Unset = UNSET,
) -> Response[ErrorsList | IncidentList]:
    """List incidents

     List incidents

    Args:
        pageafter (str | Unset):
        pagenumber (int | Unset):
        pagesize (int | Unset):
        filtersearch (str | Unset):
        filterkind (str | Unset):
        filterstatus (str | Unset):
        filterprivate (str | Unset):
        filteruser_id (int | Unset):
        filterseverity (str | Unset):
        filterseverity_id (str | Unset):
        filterlabels (str | Unset):
        filtertypes (str | Unset):
        filtertype_ids (str | Unset):
        filterenvironments (str | Unset):
        filterenvironment_ids (str | Unset):
        filterfunctionalities (str | Unset):
        filterfunctionality_ids (str | Unset):
        filterfunctionality_names (str | Unset):
        filterservices (str | Unset):
        filterservice_ids (str | Unset):
        filterservice_names (str | Unset):
        filterteams (str | Unset):
        filterteam_ids (str | Unset):
        filterteam_names (str | Unset):
        filtercause (str | Unset):
        filtercause_ids (str | Unset):
        filtercustom_field_selected_option_ids (str | Unset):
        filterslack_channel_id (str | Unset):
        filtersequential_id (str | Unset):
        filtercreated_atgt (str | Unset):
        filtercreated_atgte (str | Unset):
        filtercreated_atlt (str | Unset):
        filtercreated_atlte (str | Unset):
        filterupdated_atgt (str | Unset):
        filterupdated_atgte (str | Unset):
        filterupdated_atlt (str | Unset):
        filterupdated_atlte (str | Unset):
        filterstarted_atgt (str | Unset):
        filterstarted_atgte (str | Unset):
        filterstarted_atlt (str | Unset):
        filterstarted_atlte (str | Unset):
        filterdetected_atgt (str | Unset):
        filterdetected_atgte (str | Unset):
        filterdetected_atlt (str | Unset):
        filterdetected_atlte (str | Unset):
        filteracknowledged_atgt (str | Unset):
        filteracknowledged_atgte (str | Unset):
        filteracknowledged_atlt (str | Unset):
        filteracknowledged_atlte (str | Unset):
        filtermitigated_atgt (str | Unset):
        filtermitigated_atgte (str | Unset):
        filtermitigated_atlt (str | Unset):
        filtermitigated_atlte (str | Unset):
        filterresolved_atgt (str | Unset):
        filterresolved_atgte (str | Unset):
        filterresolved_atlt (str | Unset):
        filterresolved_atlte (str | Unset):
        filterclosed_atgt (str | Unset):
        filterclosed_atgte (str | Unset):
        filterclosed_atlt (str | Unset):
        filterclosed_atlte (str | Unset):
        filterin_triage_atgt (str | Unset):
        filterin_triage_atgte (str | Unset):
        filterin_triage_atlt (str | Unset):
        filterin_triage_atlte (str | Unset):
        filterkindeq (str | Unset):
        filterkindnot_eq (str | Unset):
        filterkindin (str | Unset):
        filterkindnot_in (str | Unset):
        filterstatuseq (str | Unset):
        filterstatusnot_eq (str | Unset):
        filterstatusin (str | Unset):
        filterstatusnot_in (str | Unset):
        filterprivateeq (str | Unset):
        filterprivatenot_eq (str | Unset):
        filterprivatein (str | Unset):
        filterprivatenot_in (str | Unset):
        filteruser_ideq (str | Unset):
        filteruser_idnot_eq (str | Unset):
        filteruser_idin (str | Unset):
        filteruser_idnot_in (str | Unset):
        filterseverityeq (str | Unset):
        filterseveritynot_eq (str | Unset):
        filterseverityin (str | Unset):
        filterseveritynot_in (str | Unset):
        filterseverity_ideq (str | Unset):
        filterseverity_idnot_eq (str | Unset):
        filterseverity_idin (str | Unset):
        filterseverity_idnot_in (str | Unset):
        filterlabelseq (str | Unset):
        filterlabelsnot_eq (str | Unset):
        filterlabelsin (str | Unset):
        filterlabelsnot_in (str | Unset):
        filterzendesk_ticket_ideq (str | Unset):
        filterzendesk_ticket_idnot_eq (str | Unset):
        filterzendesk_ticket_idin (str | Unset):
        filterzendesk_ticket_idnot_in (str | Unset):
        filtersequential_ideq (str | Unset):
        filtersequential_idnot_eq (str | Unset):
        filtersequential_idin (str | Unset):
        filtersequential_idnot_in (str | Unset):
        filtertypeseq (str | Unset):
        filtertypesnot_eq (str | Unset):
        filtertypesin (str | Unset):
        filtertypesnot_in (str | Unset):
        filtertype_idseq (str | Unset):
        filtertype_idsnot_eq (str | Unset):
        filtertype_idsin (str | Unset):
        filtertype_idsnot_in (str | Unset):
        filterenvironmentseq (str | Unset):
        filterenvironmentsnot_eq (str | Unset):
        filterenvironmentsin (str | Unset):
        filterenvironmentsnot_in (str | Unset):
        filterenvironment_idseq (str | Unset):
        filterenvironment_idsnot_eq (str | Unset):
        filterenvironment_idsin (str | Unset):
        filterenvironment_idsnot_in (str | Unset):
        filterserviceseq (str | Unset):
        filterservicesnot_eq (str | Unset):
        filterservicesin (str | Unset):
        filterservicesnot_in (str | Unset):
        filterservice_idseq (str | Unset):
        filterservice_idsnot_eq (str | Unset):
        filterservice_idsin (str | Unset):
        filterservice_idsnot_in (str | Unset):
        filterservice_nameseq (str | Unset):
        filterservice_namesnot_eq (str | Unset):
        filterservice_namesin (str | Unset):
        filterservice_namesnot_in (str | Unset):
        filterfunctionalitieseq (str | Unset):
        filterfunctionalitiesnot_eq (str | Unset):
        filterfunctionalitiesin (str | Unset):
        filterfunctionalitiesnot_in (str | Unset):
        filterfunctionality_idseq (str | Unset):
        filterfunctionality_idsnot_eq (str | Unset):
        filterfunctionality_idsin (str | Unset):
        filterfunctionality_idsnot_in (str | Unset):
        filterfunctionality_nameseq (str | Unset):
        filterfunctionality_namesnot_eq (str | Unset):
        filterfunctionality_namesin (str | Unset):
        filterfunctionality_namesnot_in (str | Unset):
        filtercauseseq (str | Unset):
        filtercausesnot_eq (str | Unset):
        filtercausesin (str | Unset):
        filtercausesnot_in (str | Unset):
        filtercause_idseq (str | Unset):
        filtercause_idsnot_eq (str | Unset):
        filtercause_idsin (str | Unset):
        filtercause_idsnot_in (str | Unset):
        filterteamseq (str | Unset):
        filterteamsnot_eq (str | Unset):
        filterteamsin (str | Unset):
        filterteamsnot_in (str | Unset):
        filterteam_idseq (str | Unset):
        filterteam_idsnot_eq (str | Unset):
        filterteam_idsin (str | Unset):
        filterteam_idsnot_in (str | Unset):
        filterteam_nameseq (str | Unset):
        filterteam_namesnot_eq (str | Unset):
        filterteam_namesin (str | Unset):
        filterteam_namesnot_in (str | Unset):
        sort (ListIncidentsSort | Unset):
        include (ListIncidentsInclude | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorsList | IncidentList]
    """

    kwargs = _get_kwargs(
        pageafter=pageafter,
        pagenumber=pagenumber,
        pagesize=pagesize,
        filtersearch=filtersearch,
        filterkind=filterkind,
        filterstatus=filterstatus,
        filterprivate=filterprivate,
        filteruser_id=filteruser_id,
        filterseverity=filterseverity,
        filterseverity_id=filterseverity_id,
        filterlabels=filterlabels,
        filtertypes=filtertypes,
        filtertype_ids=filtertype_ids,
        filterenvironments=filterenvironments,
        filterenvironment_ids=filterenvironment_ids,
        filterfunctionalities=filterfunctionalities,
        filterfunctionality_ids=filterfunctionality_ids,
        filterfunctionality_names=filterfunctionality_names,
        filterservices=filterservices,
        filterservice_ids=filterservice_ids,
        filterservice_names=filterservice_names,
        filterteams=filterteams,
        filterteam_ids=filterteam_ids,
        filterteam_names=filterteam_names,
        filtercause=filtercause,
        filtercause_ids=filtercause_ids,
        filtercustom_field_selected_option_ids=filtercustom_field_selected_option_ids,
        filterslack_channel_id=filterslack_channel_id,
        filtersequential_id=filtersequential_id,
        filtercreated_atgt=filtercreated_atgt,
        filtercreated_atgte=filtercreated_atgte,
        filtercreated_atlt=filtercreated_atlt,
        filtercreated_atlte=filtercreated_atlte,
        filterupdated_atgt=filterupdated_atgt,
        filterupdated_atgte=filterupdated_atgte,
        filterupdated_atlt=filterupdated_atlt,
        filterupdated_atlte=filterupdated_atlte,
        filterstarted_atgt=filterstarted_atgt,
        filterstarted_atgte=filterstarted_atgte,
        filterstarted_atlt=filterstarted_atlt,
        filterstarted_atlte=filterstarted_atlte,
        filterdetected_atgt=filterdetected_atgt,
        filterdetected_atgte=filterdetected_atgte,
        filterdetected_atlt=filterdetected_atlt,
        filterdetected_atlte=filterdetected_atlte,
        filteracknowledged_atgt=filteracknowledged_atgt,
        filteracknowledged_atgte=filteracknowledged_atgte,
        filteracknowledged_atlt=filteracknowledged_atlt,
        filteracknowledged_atlte=filteracknowledged_atlte,
        filtermitigated_atgt=filtermitigated_atgt,
        filtermitigated_atgte=filtermitigated_atgte,
        filtermitigated_atlt=filtermitigated_atlt,
        filtermitigated_atlte=filtermitigated_atlte,
        filterresolved_atgt=filterresolved_atgt,
        filterresolved_atgte=filterresolved_atgte,
        filterresolved_atlt=filterresolved_atlt,
        filterresolved_atlte=filterresolved_atlte,
        filterclosed_atgt=filterclosed_atgt,
        filterclosed_atgte=filterclosed_atgte,
        filterclosed_atlt=filterclosed_atlt,
        filterclosed_atlte=filterclosed_atlte,
        filterin_triage_atgt=filterin_triage_atgt,
        filterin_triage_atgte=filterin_triage_atgte,
        filterin_triage_atlt=filterin_triage_atlt,
        filterin_triage_atlte=filterin_triage_atlte,
        filterkindeq=filterkindeq,
        filterkindnot_eq=filterkindnot_eq,
        filterkindin=filterkindin,
        filterkindnot_in=filterkindnot_in,
        filterstatuseq=filterstatuseq,
        filterstatusnot_eq=filterstatusnot_eq,
        filterstatusin=filterstatusin,
        filterstatusnot_in=filterstatusnot_in,
        filterprivateeq=filterprivateeq,
        filterprivatenot_eq=filterprivatenot_eq,
        filterprivatein=filterprivatein,
        filterprivatenot_in=filterprivatenot_in,
        filteruser_ideq=filteruser_ideq,
        filteruser_idnot_eq=filteruser_idnot_eq,
        filteruser_idin=filteruser_idin,
        filteruser_idnot_in=filteruser_idnot_in,
        filterseverityeq=filterseverityeq,
        filterseveritynot_eq=filterseveritynot_eq,
        filterseverityin=filterseverityin,
        filterseveritynot_in=filterseveritynot_in,
        filterseverity_ideq=filterseverity_ideq,
        filterseverity_idnot_eq=filterseverity_idnot_eq,
        filterseverity_idin=filterseverity_idin,
        filterseverity_idnot_in=filterseverity_idnot_in,
        filterlabelseq=filterlabelseq,
        filterlabelsnot_eq=filterlabelsnot_eq,
        filterlabelsin=filterlabelsin,
        filterlabelsnot_in=filterlabelsnot_in,
        filterzendesk_ticket_ideq=filterzendesk_ticket_ideq,
        filterzendesk_ticket_idnot_eq=filterzendesk_ticket_idnot_eq,
        filterzendesk_ticket_idin=filterzendesk_ticket_idin,
        filterzendesk_ticket_idnot_in=filterzendesk_ticket_idnot_in,
        filtersequential_ideq=filtersequential_ideq,
        filtersequential_idnot_eq=filtersequential_idnot_eq,
        filtersequential_idin=filtersequential_idin,
        filtersequential_idnot_in=filtersequential_idnot_in,
        filtertypeseq=filtertypeseq,
        filtertypesnot_eq=filtertypesnot_eq,
        filtertypesin=filtertypesin,
        filtertypesnot_in=filtertypesnot_in,
        filtertype_idseq=filtertype_idseq,
        filtertype_idsnot_eq=filtertype_idsnot_eq,
        filtertype_idsin=filtertype_idsin,
        filtertype_idsnot_in=filtertype_idsnot_in,
        filterenvironmentseq=filterenvironmentseq,
        filterenvironmentsnot_eq=filterenvironmentsnot_eq,
        filterenvironmentsin=filterenvironmentsin,
        filterenvironmentsnot_in=filterenvironmentsnot_in,
        filterenvironment_idseq=filterenvironment_idseq,
        filterenvironment_idsnot_eq=filterenvironment_idsnot_eq,
        filterenvironment_idsin=filterenvironment_idsin,
        filterenvironment_idsnot_in=filterenvironment_idsnot_in,
        filterserviceseq=filterserviceseq,
        filterservicesnot_eq=filterservicesnot_eq,
        filterservicesin=filterservicesin,
        filterservicesnot_in=filterservicesnot_in,
        filterservice_idseq=filterservice_idseq,
        filterservice_idsnot_eq=filterservice_idsnot_eq,
        filterservice_idsin=filterservice_idsin,
        filterservice_idsnot_in=filterservice_idsnot_in,
        filterservice_nameseq=filterservice_nameseq,
        filterservice_namesnot_eq=filterservice_namesnot_eq,
        filterservice_namesin=filterservice_namesin,
        filterservice_namesnot_in=filterservice_namesnot_in,
        filterfunctionalitieseq=filterfunctionalitieseq,
        filterfunctionalitiesnot_eq=filterfunctionalitiesnot_eq,
        filterfunctionalitiesin=filterfunctionalitiesin,
        filterfunctionalitiesnot_in=filterfunctionalitiesnot_in,
        filterfunctionality_idseq=filterfunctionality_idseq,
        filterfunctionality_idsnot_eq=filterfunctionality_idsnot_eq,
        filterfunctionality_idsin=filterfunctionality_idsin,
        filterfunctionality_idsnot_in=filterfunctionality_idsnot_in,
        filterfunctionality_nameseq=filterfunctionality_nameseq,
        filterfunctionality_namesnot_eq=filterfunctionality_namesnot_eq,
        filterfunctionality_namesin=filterfunctionality_namesin,
        filterfunctionality_namesnot_in=filterfunctionality_namesnot_in,
        filtercauseseq=filtercauseseq,
        filtercausesnot_eq=filtercausesnot_eq,
        filtercausesin=filtercausesin,
        filtercausesnot_in=filtercausesnot_in,
        filtercause_idseq=filtercause_idseq,
        filtercause_idsnot_eq=filtercause_idsnot_eq,
        filtercause_idsin=filtercause_idsin,
        filtercause_idsnot_in=filtercause_idsnot_in,
        filterteamseq=filterteamseq,
        filterteamsnot_eq=filterteamsnot_eq,
        filterteamsin=filterteamsin,
        filterteamsnot_in=filterteamsnot_in,
        filterteam_idseq=filterteam_idseq,
        filterteam_idsnot_eq=filterteam_idsnot_eq,
        filterteam_idsin=filterteam_idsin,
        filterteam_idsnot_in=filterteam_idsnot_in,
        filterteam_nameseq=filterteam_nameseq,
        filterteam_namesnot_eq=filterteam_namesnot_eq,
        filterteam_namesin=filterteam_namesin,
        filterteam_namesnot_in=filterteam_namesnot_in,
        sort=sort,
        include=include,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    pageafter: str | Unset = UNSET,
    pagenumber: int | Unset = UNSET,
    pagesize: int | Unset = UNSET,
    filtersearch: str | Unset = UNSET,
    filterkind: str | Unset = UNSET,
    filterstatus: str | Unset = UNSET,
    filterprivate: str | Unset = UNSET,
    filteruser_id: int | Unset = UNSET,
    filterseverity: str | Unset = UNSET,
    filterseverity_id: str | Unset = UNSET,
    filterlabels: str | Unset = UNSET,
    filtertypes: str | Unset = UNSET,
    filtertype_ids: str | Unset = UNSET,
    filterenvironments: str | Unset = UNSET,
    filterenvironment_ids: str | Unset = UNSET,
    filterfunctionalities: str | Unset = UNSET,
    filterfunctionality_ids: str | Unset = UNSET,
    filterfunctionality_names: str | Unset = UNSET,
    filterservices: str | Unset = UNSET,
    filterservice_ids: str | Unset = UNSET,
    filterservice_names: str | Unset = UNSET,
    filterteams: str | Unset = UNSET,
    filterteam_ids: str | Unset = UNSET,
    filterteam_names: str | Unset = UNSET,
    filtercause: str | Unset = UNSET,
    filtercause_ids: str | Unset = UNSET,
    filtercustom_field_selected_option_ids: str | Unset = UNSET,
    filterslack_channel_id: str | Unset = UNSET,
    filtersequential_id: str | Unset = UNSET,
    filtercreated_atgt: str | Unset = UNSET,
    filtercreated_atgte: str | Unset = UNSET,
    filtercreated_atlt: str | Unset = UNSET,
    filtercreated_atlte: str | Unset = UNSET,
    filterupdated_atgt: str | Unset = UNSET,
    filterupdated_atgte: str | Unset = UNSET,
    filterupdated_atlt: str | Unset = UNSET,
    filterupdated_atlte: str | Unset = UNSET,
    filterstarted_atgt: str | Unset = UNSET,
    filterstarted_atgte: str | Unset = UNSET,
    filterstarted_atlt: str | Unset = UNSET,
    filterstarted_atlte: str | Unset = UNSET,
    filterdetected_atgt: str | Unset = UNSET,
    filterdetected_atgte: str | Unset = UNSET,
    filterdetected_atlt: str | Unset = UNSET,
    filterdetected_atlte: str | Unset = UNSET,
    filteracknowledged_atgt: str | Unset = UNSET,
    filteracknowledged_atgte: str | Unset = UNSET,
    filteracknowledged_atlt: str | Unset = UNSET,
    filteracknowledged_atlte: str | Unset = UNSET,
    filtermitigated_atgt: str | Unset = UNSET,
    filtermitigated_atgte: str | Unset = UNSET,
    filtermitigated_atlt: str | Unset = UNSET,
    filtermitigated_atlte: str | Unset = UNSET,
    filterresolved_atgt: str | Unset = UNSET,
    filterresolved_atgte: str | Unset = UNSET,
    filterresolved_atlt: str | Unset = UNSET,
    filterresolved_atlte: str | Unset = UNSET,
    filterclosed_atgt: str | Unset = UNSET,
    filterclosed_atgte: str | Unset = UNSET,
    filterclosed_atlt: str | Unset = UNSET,
    filterclosed_atlte: str | Unset = UNSET,
    filterin_triage_atgt: str | Unset = UNSET,
    filterin_triage_atgte: str | Unset = UNSET,
    filterin_triage_atlt: str | Unset = UNSET,
    filterin_triage_atlte: str | Unset = UNSET,
    filterkindeq: str | Unset = UNSET,
    filterkindnot_eq: str | Unset = UNSET,
    filterkindin: str | Unset = UNSET,
    filterkindnot_in: str | Unset = UNSET,
    filterstatuseq: str | Unset = UNSET,
    filterstatusnot_eq: str | Unset = UNSET,
    filterstatusin: str | Unset = UNSET,
    filterstatusnot_in: str | Unset = UNSET,
    filterprivateeq: str | Unset = UNSET,
    filterprivatenot_eq: str | Unset = UNSET,
    filterprivatein: str | Unset = UNSET,
    filterprivatenot_in: str | Unset = UNSET,
    filteruser_ideq: str | Unset = UNSET,
    filteruser_idnot_eq: str | Unset = UNSET,
    filteruser_idin: str | Unset = UNSET,
    filteruser_idnot_in: str | Unset = UNSET,
    filterseverityeq: str | Unset = UNSET,
    filterseveritynot_eq: str | Unset = UNSET,
    filterseverityin: str | Unset = UNSET,
    filterseveritynot_in: str | Unset = UNSET,
    filterseverity_ideq: str | Unset = UNSET,
    filterseverity_idnot_eq: str | Unset = UNSET,
    filterseverity_idin: str | Unset = UNSET,
    filterseverity_idnot_in: str | Unset = UNSET,
    filterlabelseq: str | Unset = UNSET,
    filterlabelsnot_eq: str | Unset = UNSET,
    filterlabelsin: str | Unset = UNSET,
    filterlabelsnot_in: str | Unset = UNSET,
    filterzendesk_ticket_ideq: str | Unset = UNSET,
    filterzendesk_ticket_idnot_eq: str | Unset = UNSET,
    filterzendesk_ticket_idin: str | Unset = UNSET,
    filterzendesk_ticket_idnot_in: str | Unset = UNSET,
    filtersequential_ideq: str | Unset = UNSET,
    filtersequential_idnot_eq: str | Unset = UNSET,
    filtersequential_idin: str | Unset = UNSET,
    filtersequential_idnot_in: str | Unset = UNSET,
    filtertypeseq: str | Unset = UNSET,
    filtertypesnot_eq: str | Unset = UNSET,
    filtertypesin: str | Unset = UNSET,
    filtertypesnot_in: str | Unset = UNSET,
    filtertype_idseq: str | Unset = UNSET,
    filtertype_idsnot_eq: str | Unset = UNSET,
    filtertype_idsin: str | Unset = UNSET,
    filtertype_idsnot_in: str | Unset = UNSET,
    filterenvironmentseq: str | Unset = UNSET,
    filterenvironmentsnot_eq: str | Unset = UNSET,
    filterenvironmentsin: str | Unset = UNSET,
    filterenvironmentsnot_in: str | Unset = UNSET,
    filterenvironment_idseq: str | Unset = UNSET,
    filterenvironment_idsnot_eq: str | Unset = UNSET,
    filterenvironment_idsin: str | Unset = UNSET,
    filterenvironment_idsnot_in: str | Unset = UNSET,
    filterserviceseq: str | Unset = UNSET,
    filterservicesnot_eq: str | Unset = UNSET,
    filterservicesin: str | Unset = UNSET,
    filterservicesnot_in: str | Unset = UNSET,
    filterservice_idseq: str | Unset = UNSET,
    filterservice_idsnot_eq: str | Unset = UNSET,
    filterservice_idsin: str | Unset = UNSET,
    filterservice_idsnot_in: str | Unset = UNSET,
    filterservice_nameseq: str | Unset = UNSET,
    filterservice_namesnot_eq: str | Unset = UNSET,
    filterservice_namesin: str | Unset = UNSET,
    filterservice_namesnot_in: str | Unset = UNSET,
    filterfunctionalitieseq: str | Unset = UNSET,
    filterfunctionalitiesnot_eq: str | Unset = UNSET,
    filterfunctionalitiesin: str | Unset = UNSET,
    filterfunctionalitiesnot_in: str | Unset = UNSET,
    filterfunctionality_idseq: str | Unset = UNSET,
    filterfunctionality_idsnot_eq: str | Unset = UNSET,
    filterfunctionality_idsin: str | Unset = UNSET,
    filterfunctionality_idsnot_in: str | Unset = UNSET,
    filterfunctionality_nameseq: str | Unset = UNSET,
    filterfunctionality_namesnot_eq: str | Unset = UNSET,
    filterfunctionality_namesin: str | Unset = UNSET,
    filterfunctionality_namesnot_in: str | Unset = UNSET,
    filtercauseseq: str | Unset = UNSET,
    filtercausesnot_eq: str | Unset = UNSET,
    filtercausesin: str | Unset = UNSET,
    filtercausesnot_in: str | Unset = UNSET,
    filtercause_idseq: str | Unset = UNSET,
    filtercause_idsnot_eq: str | Unset = UNSET,
    filtercause_idsin: str | Unset = UNSET,
    filtercause_idsnot_in: str | Unset = UNSET,
    filterteamseq: str | Unset = UNSET,
    filterteamsnot_eq: str | Unset = UNSET,
    filterteamsin: str | Unset = UNSET,
    filterteamsnot_in: str | Unset = UNSET,
    filterteam_idseq: str | Unset = UNSET,
    filterteam_idsnot_eq: str | Unset = UNSET,
    filterteam_idsin: str | Unset = UNSET,
    filterteam_idsnot_in: str | Unset = UNSET,
    filterteam_nameseq: str | Unset = UNSET,
    filterteam_namesnot_eq: str | Unset = UNSET,
    filterteam_namesin: str | Unset = UNSET,
    filterteam_namesnot_in: str | Unset = UNSET,
    sort: ListIncidentsSort | Unset = UNSET,
    include: ListIncidentsInclude | Unset = UNSET,
) -> ErrorsList | IncidentList | None:
    """List incidents

     List incidents

    Args:
        pageafter (str | Unset):
        pagenumber (int | Unset):
        pagesize (int | Unset):
        filtersearch (str | Unset):
        filterkind (str | Unset):
        filterstatus (str | Unset):
        filterprivate (str | Unset):
        filteruser_id (int | Unset):
        filterseverity (str | Unset):
        filterseverity_id (str | Unset):
        filterlabels (str | Unset):
        filtertypes (str | Unset):
        filtertype_ids (str | Unset):
        filterenvironments (str | Unset):
        filterenvironment_ids (str | Unset):
        filterfunctionalities (str | Unset):
        filterfunctionality_ids (str | Unset):
        filterfunctionality_names (str | Unset):
        filterservices (str | Unset):
        filterservice_ids (str | Unset):
        filterservice_names (str | Unset):
        filterteams (str | Unset):
        filterteam_ids (str | Unset):
        filterteam_names (str | Unset):
        filtercause (str | Unset):
        filtercause_ids (str | Unset):
        filtercustom_field_selected_option_ids (str | Unset):
        filterslack_channel_id (str | Unset):
        filtersequential_id (str | Unset):
        filtercreated_atgt (str | Unset):
        filtercreated_atgte (str | Unset):
        filtercreated_atlt (str | Unset):
        filtercreated_atlte (str | Unset):
        filterupdated_atgt (str | Unset):
        filterupdated_atgte (str | Unset):
        filterupdated_atlt (str | Unset):
        filterupdated_atlte (str | Unset):
        filterstarted_atgt (str | Unset):
        filterstarted_atgte (str | Unset):
        filterstarted_atlt (str | Unset):
        filterstarted_atlte (str | Unset):
        filterdetected_atgt (str | Unset):
        filterdetected_atgte (str | Unset):
        filterdetected_atlt (str | Unset):
        filterdetected_atlte (str | Unset):
        filteracknowledged_atgt (str | Unset):
        filteracknowledged_atgte (str | Unset):
        filteracknowledged_atlt (str | Unset):
        filteracknowledged_atlte (str | Unset):
        filtermitigated_atgt (str | Unset):
        filtermitigated_atgte (str | Unset):
        filtermitigated_atlt (str | Unset):
        filtermitigated_atlte (str | Unset):
        filterresolved_atgt (str | Unset):
        filterresolved_atgte (str | Unset):
        filterresolved_atlt (str | Unset):
        filterresolved_atlte (str | Unset):
        filterclosed_atgt (str | Unset):
        filterclosed_atgte (str | Unset):
        filterclosed_atlt (str | Unset):
        filterclosed_atlte (str | Unset):
        filterin_triage_atgt (str | Unset):
        filterin_triage_atgte (str | Unset):
        filterin_triage_atlt (str | Unset):
        filterin_triage_atlte (str | Unset):
        filterkindeq (str | Unset):
        filterkindnot_eq (str | Unset):
        filterkindin (str | Unset):
        filterkindnot_in (str | Unset):
        filterstatuseq (str | Unset):
        filterstatusnot_eq (str | Unset):
        filterstatusin (str | Unset):
        filterstatusnot_in (str | Unset):
        filterprivateeq (str | Unset):
        filterprivatenot_eq (str | Unset):
        filterprivatein (str | Unset):
        filterprivatenot_in (str | Unset):
        filteruser_ideq (str | Unset):
        filteruser_idnot_eq (str | Unset):
        filteruser_idin (str | Unset):
        filteruser_idnot_in (str | Unset):
        filterseverityeq (str | Unset):
        filterseveritynot_eq (str | Unset):
        filterseverityin (str | Unset):
        filterseveritynot_in (str | Unset):
        filterseverity_ideq (str | Unset):
        filterseverity_idnot_eq (str | Unset):
        filterseverity_idin (str | Unset):
        filterseverity_idnot_in (str | Unset):
        filterlabelseq (str | Unset):
        filterlabelsnot_eq (str | Unset):
        filterlabelsin (str | Unset):
        filterlabelsnot_in (str | Unset):
        filterzendesk_ticket_ideq (str | Unset):
        filterzendesk_ticket_idnot_eq (str | Unset):
        filterzendesk_ticket_idin (str | Unset):
        filterzendesk_ticket_idnot_in (str | Unset):
        filtersequential_ideq (str | Unset):
        filtersequential_idnot_eq (str | Unset):
        filtersequential_idin (str | Unset):
        filtersequential_idnot_in (str | Unset):
        filtertypeseq (str | Unset):
        filtertypesnot_eq (str | Unset):
        filtertypesin (str | Unset):
        filtertypesnot_in (str | Unset):
        filtertype_idseq (str | Unset):
        filtertype_idsnot_eq (str | Unset):
        filtertype_idsin (str | Unset):
        filtertype_idsnot_in (str | Unset):
        filterenvironmentseq (str | Unset):
        filterenvironmentsnot_eq (str | Unset):
        filterenvironmentsin (str | Unset):
        filterenvironmentsnot_in (str | Unset):
        filterenvironment_idseq (str | Unset):
        filterenvironment_idsnot_eq (str | Unset):
        filterenvironment_idsin (str | Unset):
        filterenvironment_idsnot_in (str | Unset):
        filterserviceseq (str | Unset):
        filterservicesnot_eq (str | Unset):
        filterservicesin (str | Unset):
        filterservicesnot_in (str | Unset):
        filterservice_idseq (str | Unset):
        filterservice_idsnot_eq (str | Unset):
        filterservice_idsin (str | Unset):
        filterservice_idsnot_in (str | Unset):
        filterservice_nameseq (str | Unset):
        filterservice_namesnot_eq (str | Unset):
        filterservice_namesin (str | Unset):
        filterservice_namesnot_in (str | Unset):
        filterfunctionalitieseq (str | Unset):
        filterfunctionalitiesnot_eq (str | Unset):
        filterfunctionalitiesin (str | Unset):
        filterfunctionalitiesnot_in (str | Unset):
        filterfunctionality_idseq (str | Unset):
        filterfunctionality_idsnot_eq (str | Unset):
        filterfunctionality_idsin (str | Unset):
        filterfunctionality_idsnot_in (str | Unset):
        filterfunctionality_nameseq (str | Unset):
        filterfunctionality_namesnot_eq (str | Unset):
        filterfunctionality_namesin (str | Unset):
        filterfunctionality_namesnot_in (str | Unset):
        filtercauseseq (str | Unset):
        filtercausesnot_eq (str | Unset):
        filtercausesin (str | Unset):
        filtercausesnot_in (str | Unset):
        filtercause_idseq (str | Unset):
        filtercause_idsnot_eq (str | Unset):
        filtercause_idsin (str | Unset):
        filtercause_idsnot_in (str | Unset):
        filterteamseq (str | Unset):
        filterteamsnot_eq (str | Unset):
        filterteamsin (str | Unset):
        filterteamsnot_in (str | Unset):
        filterteam_idseq (str | Unset):
        filterteam_idsnot_eq (str | Unset):
        filterteam_idsin (str | Unset):
        filterteam_idsnot_in (str | Unset):
        filterteam_nameseq (str | Unset):
        filterteam_namesnot_eq (str | Unset):
        filterteam_namesin (str | Unset):
        filterteam_namesnot_in (str | Unset):
        sort (ListIncidentsSort | Unset):
        include (ListIncidentsInclude | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorsList | IncidentList
    """

    return sync_detailed(
        client=client,
        pageafter=pageafter,
        pagenumber=pagenumber,
        pagesize=pagesize,
        filtersearch=filtersearch,
        filterkind=filterkind,
        filterstatus=filterstatus,
        filterprivate=filterprivate,
        filteruser_id=filteruser_id,
        filterseverity=filterseverity,
        filterseverity_id=filterseverity_id,
        filterlabels=filterlabels,
        filtertypes=filtertypes,
        filtertype_ids=filtertype_ids,
        filterenvironments=filterenvironments,
        filterenvironment_ids=filterenvironment_ids,
        filterfunctionalities=filterfunctionalities,
        filterfunctionality_ids=filterfunctionality_ids,
        filterfunctionality_names=filterfunctionality_names,
        filterservices=filterservices,
        filterservice_ids=filterservice_ids,
        filterservice_names=filterservice_names,
        filterteams=filterteams,
        filterteam_ids=filterteam_ids,
        filterteam_names=filterteam_names,
        filtercause=filtercause,
        filtercause_ids=filtercause_ids,
        filtercustom_field_selected_option_ids=filtercustom_field_selected_option_ids,
        filterslack_channel_id=filterslack_channel_id,
        filtersequential_id=filtersequential_id,
        filtercreated_atgt=filtercreated_atgt,
        filtercreated_atgte=filtercreated_atgte,
        filtercreated_atlt=filtercreated_atlt,
        filtercreated_atlte=filtercreated_atlte,
        filterupdated_atgt=filterupdated_atgt,
        filterupdated_atgte=filterupdated_atgte,
        filterupdated_atlt=filterupdated_atlt,
        filterupdated_atlte=filterupdated_atlte,
        filterstarted_atgt=filterstarted_atgt,
        filterstarted_atgte=filterstarted_atgte,
        filterstarted_atlt=filterstarted_atlt,
        filterstarted_atlte=filterstarted_atlte,
        filterdetected_atgt=filterdetected_atgt,
        filterdetected_atgte=filterdetected_atgte,
        filterdetected_atlt=filterdetected_atlt,
        filterdetected_atlte=filterdetected_atlte,
        filteracknowledged_atgt=filteracknowledged_atgt,
        filteracknowledged_atgte=filteracknowledged_atgte,
        filteracknowledged_atlt=filteracknowledged_atlt,
        filteracknowledged_atlte=filteracknowledged_atlte,
        filtermitigated_atgt=filtermitigated_atgt,
        filtermitigated_atgte=filtermitigated_atgte,
        filtermitigated_atlt=filtermitigated_atlt,
        filtermitigated_atlte=filtermitigated_atlte,
        filterresolved_atgt=filterresolved_atgt,
        filterresolved_atgte=filterresolved_atgte,
        filterresolved_atlt=filterresolved_atlt,
        filterresolved_atlte=filterresolved_atlte,
        filterclosed_atgt=filterclosed_atgt,
        filterclosed_atgte=filterclosed_atgte,
        filterclosed_atlt=filterclosed_atlt,
        filterclosed_atlte=filterclosed_atlte,
        filterin_triage_atgt=filterin_triage_atgt,
        filterin_triage_atgte=filterin_triage_atgte,
        filterin_triage_atlt=filterin_triage_atlt,
        filterin_triage_atlte=filterin_triage_atlte,
        filterkindeq=filterkindeq,
        filterkindnot_eq=filterkindnot_eq,
        filterkindin=filterkindin,
        filterkindnot_in=filterkindnot_in,
        filterstatuseq=filterstatuseq,
        filterstatusnot_eq=filterstatusnot_eq,
        filterstatusin=filterstatusin,
        filterstatusnot_in=filterstatusnot_in,
        filterprivateeq=filterprivateeq,
        filterprivatenot_eq=filterprivatenot_eq,
        filterprivatein=filterprivatein,
        filterprivatenot_in=filterprivatenot_in,
        filteruser_ideq=filteruser_ideq,
        filteruser_idnot_eq=filteruser_idnot_eq,
        filteruser_idin=filteruser_idin,
        filteruser_idnot_in=filteruser_idnot_in,
        filterseverityeq=filterseverityeq,
        filterseveritynot_eq=filterseveritynot_eq,
        filterseverityin=filterseverityin,
        filterseveritynot_in=filterseveritynot_in,
        filterseverity_ideq=filterseverity_ideq,
        filterseverity_idnot_eq=filterseverity_idnot_eq,
        filterseverity_idin=filterseverity_idin,
        filterseverity_idnot_in=filterseverity_idnot_in,
        filterlabelseq=filterlabelseq,
        filterlabelsnot_eq=filterlabelsnot_eq,
        filterlabelsin=filterlabelsin,
        filterlabelsnot_in=filterlabelsnot_in,
        filterzendesk_ticket_ideq=filterzendesk_ticket_ideq,
        filterzendesk_ticket_idnot_eq=filterzendesk_ticket_idnot_eq,
        filterzendesk_ticket_idin=filterzendesk_ticket_idin,
        filterzendesk_ticket_idnot_in=filterzendesk_ticket_idnot_in,
        filtersequential_ideq=filtersequential_ideq,
        filtersequential_idnot_eq=filtersequential_idnot_eq,
        filtersequential_idin=filtersequential_idin,
        filtersequential_idnot_in=filtersequential_idnot_in,
        filtertypeseq=filtertypeseq,
        filtertypesnot_eq=filtertypesnot_eq,
        filtertypesin=filtertypesin,
        filtertypesnot_in=filtertypesnot_in,
        filtertype_idseq=filtertype_idseq,
        filtertype_idsnot_eq=filtertype_idsnot_eq,
        filtertype_idsin=filtertype_idsin,
        filtertype_idsnot_in=filtertype_idsnot_in,
        filterenvironmentseq=filterenvironmentseq,
        filterenvironmentsnot_eq=filterenvironmentsnot_eq,
        filterenvironmentsin=filterenvironmentsin,
        filterenvironmentsnot_in=filterenvironmentsnot_in,
        filterenvironment_idseq=filterenvironment_idseq,
        filterenvironment_idsnot_eq=filterenvironment_idsnot_eq,
        filterenvironment_idsin=filterenvironment_idsin,
        filterenvironment_idsnot_in=filterenvironment_idsnot_in,
        filterserviceseq=filterserviceseq,
        filterservicesnot_eq=filterservicesnot_eq,
        filterservicesin=filterservicesin,
        filterservicesnot_in=filterservicesnot_in,
        filterservice_idseq=filterservice_idseq,
        filterservice_idsnot_eq=filterservice_idsnot_eq,
        filterservice_idsin=filterservice_idsin,
        filterservice_idsnot_in=filterservice_idsnot_in,
        filterservice_nameseq=filterservice_nameseq,
        filterservice_namesnot_eq=filterservice_namesnot_eq,
        filterservice_namesin=filterservice_namesin,
        filterservice_namesnot_in=filterservice_namesnot_in,
        filterfunctionalitieseq=filterfunctionalitieseq,
        filterfunctionalitiesnot_eq=filterfunctionalitiesnot_eq,
        filterfunctionalitiesin=filterfunctionalitiesin,
        filterfunctionalitiesnot_in=filterfunctionalitiesnot_in,
        filterfunctionality_idseq=filterfunctionality_idseq,
        filterfunctionality_idsnot_eq=filterfunctionality_idsnot_eq,
        filterfunctionality_idsin=filterfunctionality_idsin,
        filterfunctionality_idsnot_in=filterfunctionality_idsnot_in,
        filterfunctionality_nameseq=filterfunctionality_nameseq,
        filterfunctionality_namesnot_eq=filterfunctionality_namesnot_eq,
        filterfunctionality_namesin=filterfunctionality_namesin,
        filterfunctionality_namesnot_in=filterfunctionality_namesnot_in,
        filtercauseseq=filtercauseseq,
        filtercausesnot_eq=filtercausesnot_eq,
        filtercausesin=filtercausesin,
        filtercausesnot_in=filtercausesnot_in,
        filtercause_idseq=filtercause_idseq,
        filtercause_idsnot_eq=filtercause_idsnot_eq,
        filtercause_idsin=filtercause_idsin,
        filtercause_idsnot_in=filtercause_idsnot_in,
        filterteamseq=filterteamseq,
        filterteamsnot_eq=filterteamsnot_eq,
        filterteamsin=filterteamsin,
        filterteamsnot_in=filterteamsnot_in,
        filterteam_idseq=filterteam_idseq,
        filterteam_idsnot_eq=filterteam_idsnot_eq,
        filterteam_idsin=filterteam_idsin,
        filterteam_idsnot_in=filterteam_idsnot_in,
        filterteam_nameseq=filterteam_nameseq,
        filterteam_namesnot_eq=filterteam_namesnot_eq,
        filterteam_namesin=filterteam_namesin,
        filterteam_namesnot_in=filterteam_namesnot_in,
        sort=sort,
        include=include,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    pageafter: str | Unset = UNSET,
    pagenumber: int | Unset = UNSET,
    pagesize: int | Unset = UNSET,
    filtersearch: str | Unset = UNSET,
    filterkind: str | Unset = UNSET,
    filterstatus: str | Unset = UNSET,
    filterprivate: str | Unset = UNSET,
    filteruser_id: int | Unset = UNSET,
    filterseverity: str | Unset = UNSET,
    filterseverity_id: str | Unset = UNSET,
    filterlabels: str | Unset = UNSET,
    filtertypes: str | Unset = UNSET,
    filtertype_ids: str | Unset = UNSET,
    filterenvironments: str | Unset = UNSET,
    filterenvironment_ids: str | Unset = UNSET,
    filterfunctionalities: str | Unset = UNSET,
    filterfunctionality_ids: str | Unset = UNSET,
    filterfunctionality_names: str | Unset = UNSET,
    filterservices: str | Unset = UNSET,
    filterservice_ids: str | Unset = UNSET,
    filterservice_names: str | Unset = UNSET,
    filterteams: str | Unset = UNSET,
    filterteam_ids: str | Unset = UNSET,
    filterteam_names: str | Unset = UNSET,
    filtercause: str | Unset = UNSET,
    filtercause_ids: str | Unset = UNSET,
    filtercustom_field_selected_option_ids: str | Unset = UNSET,
    filterslack_channel_id: str | Unset = UNSET,
    filtersequential_id: str | Unset = UNSET,
    filtercreated_atgt: str | Unset = UNSET,
    filtercreated_atgte: str | Unset = UNSET,
    filtercreated_atlt: str | Unset = UNSET,
    filtercreated_atlte: str | Unset = UNSET,
    filterupdated_atgt: str | Unset = UNSET,
    filterupdated_atgte: str | Unset = UNSET,
    filterupdated_atlt: str | Unset = UNSET,
    filterupdated_atlte: str | Unset = UNSET,
    filterstarted_atgt: str | Unset = UNSET,
    filterstarted_atgte: str | Unset = UNSET,
    filterstarted_atlt: str | Unset = UNSET,
    filterstarted_atlte: str | Unset = UNSET,
    filterdetected_atgt: str | Unset = UNSET,
    filterdetected_atgte: str | Unset = UNSET,
    filterdetected_atlt: str | Unset = UNSET,
    filterdetected_atlte: str | Unset = UNSET,
    filteracknowledged_atgt: str | Unset = UNSET,
    filteracknowledged_atgte: str | Unset = UNSET,
    filteracknowledged_atlt: str | Unset = UNSET,
    filteracknowledged_atlte: str | Unset = UNSET,
    filtermitigated_atgt: str | Unset = UNSET,
    filtermitigated_atgte: str | Unset = UNSET,
    filtermitigated_atlt: str | Unset = UNSET,
    filtermitigated_atlte: str | Unset = UNSET,
    filterresolved_atgt: str | Unset = UNSET,
    filterresolved_atgte: str | Unset = UNSET,
    filterresolved_atlt: str | Unset = UNSET,
    filterresolved_atlte: str | Unset = UNSET,
    filterclosed_atgt: str | Unset = UNSET,
    filterclosed_atgte: str | Unset = UNSET,
    filterclosed_atlt: str | Unset = UNSET,
    filterclosed_atlte: str | Unset = UNSET,
    filterin_triage_atgt: str | Unset = UNSET,
    filterin_triage_atgte: str | Unset = UNSET,
    filterin_triage_atlt: str | Unset = UNSET,
    filterin_triage_atlte: str | Unset = UNSET,
    filterkindeq: str | Unset = UNSET,
    filterkindnot_eq: str | Unset = UNSET,
    filterkindin: str | Unset = UNSET,
    filterkindnot_in: str | Unset = UNSET,
    filterstatuseq: str | Unset = UNSET,
    filterstatusnot_eq: str | Unset = UNSET,
    filterstatusin: str | Unset = UNSET,
    filterstatusnot_in: str | Unset = UNSET,
    filterprivateeq: str | Unset = UNSET,
    filterprivatenot_eq: str | Unset = UNSET,
    filterprivatein: str | Unset = UNSET,
    filterprivatenot_in: str | Unset = UNSET,
    filteruser_ideq: str | Unset = UNSET,
    filteruser_idnot_eq: str | Unset = UNSET,
    filteruser_idin: str | Unset = UNSET,
    filteruser_idnot_in: str | Unset = UNSET,
    filterseverityeq: str | Unset = UNSET,
    filterseveritynot_eq: str | Unset = UNSET,
    filterseverityin: str | Unset = UNSET,
    filterseveritynot_in: str | Unset = UNSET,
    filterseverity_ideq: str | Unset = UNSET,
    filterseverity_idnot_eq: str | Unset = UNSET,
    filterseverity_idin: str | Unset = UNSET,
    filterseverity_idnot_in: str | Unset = UNSET,
    filterlabelseq: str | Unset = UNSET,
    filterlabelsnot_eq: str | Unset = UNSET,
    filterlabelsin: str | Unset = UNSET,
    filterlabelsnot_in: str | Unset = UNSET,
    filterzendesk_ticket_ideq: str | Unset = UNSET,
    filterzendesk_ticket_idnot_eq: str | Unset = UNSET,
    filterzendesk_ticket_idin: str | Unset = UNSET,
    filterzendesk_ticket_idnot_in: str | Unset = UNSET,
    filtersequential_ideq: str | Unset = UNSET,
    filtersequential_idnot_eq: str | Unset = UNSET,
    filtersequential_idin: str | Unset = UNSET,
    filtersequential_idnot_in: str | Unset = UNSET,
    filtertypeseq: str | Unset = UNSET,
    filtertypesnot_eq: str | Unset = UNSET,
    filtertypesin: str | Unset = UNSET,
    filtertypesnot_in: str | Unset = UNSET,
    filtertype_idseq: str | Unset = UNSET,
    filtertype_idsnot_eq: str | Unset = UNSET,
    filtertype_idsin: str | Unset = UNSET,
    filtertype_idsnot_in: str | Unset = UNSET,
    filterenvironmentseq: str | Unset = UNSET,
    filterenvironmentsnot_eq: str | Unset = UNSET,
    filterenvironmentsin: str | Unset = UNSET,
    filterenvironmentsnot_in: str | Unset = UNSET,
    filterenvironment_idseq: str | Unset = UNSET,
    filterenvironment_idsnot_eq: str | Unset = UNSET,
    filterenvironment_idsin: str | Unset = UNSET,
    filterenvironment_idsnot_in: str | Unset = UNSET,
    filterserviceseq: str | Unset = UNSET,
    filterservicesnot_eq: str | Unset = UNSET,
    filterservicesin: str | Unset = UNSET,
    filterservicesnot_in: str | Unset = UNSET,
    filterservice_idseq: str | Unset = UNSET,
    filterservice_idsnot_eq: str | Unset = UNSET,
    filterservice_idsin: str | Unset = UNSET,
    filterservice_idsnot_in: str | Unset = UNSET,
    filterservice_nameseq: str | Unset = UNSET,
    filterservice_namesnot_eq: str | Unset = UNSET,
    filterservice_namesin: str | Unset = UNSET,
    filterservice_namesnot_in: str | Unset = UNSET,
    filterfunctionalitieseq: str | Unset = UNSET,
    filterfunctionalitiesnot_eq: str | Unset = UNSET,
    filterfunctionalitiesin: str | Unset = UNSET,
    filterfunctionalitiesnot_in: str | Unset = UNSET,
    filterfunctionality_idseq: str | Unset = UNSET,
    filterfunctionality_idsnot_eq: str | Unset = UNSET,
    filterfunctionality_idsin: str | Unset = UNSET,
    filterfunctionality_idsnot_in: str | Unset = UNSET,
    filterfunctionality_nameseq: str | Unset = UNSET,
    filterfunctionality_namesnot_eq: str | Unset = UNSET,
    filterfunctionality_namesin: str | Unset = UNSET,
    filterfunctionality_namesnot_in: str | Unset = UNSET,
    filtercauseseq: str | Unset = UNSET,
    filtercausesnot_eq: str | Unset = UNSET,
    filtercausesin: str | Unset = UNSET,
    filtercausesnot_in: str | Unset = UNSET,
    filtercause_idseq: str | Unset = UNSET,
    filtercause_idsnot_eq: str | Unset = UNSET,
    filtercause_idsin: str | Unset = UNSET,
    filtercause_idsnot_in: str | Unset = UNSET,
    filterteamseq: str | Unset = UNSET,
    filterteamsnot_eq: str | Unset = UNSET,
    filterteamsin: str | Unset = UNSET,
    filterteamsnot_in: str | Unset = UNSET,
    filterteam_idseq: str | Unset = UNSET,
    filterteam_idsnot_eq: str | Unset = UNSET,
    filterteam_idsin: str | Unset = UNSET,
    filterteam_idsnot_in: str | Unset = UNSET,
    filterteam_nameseq: str | Unset = UNSET,
    filterteam_namesnot_eq: str | Unset = UNSET,
    filterteam_namesin: str | Unset = UNSET,
    filterteam_namesnot_in: str | Unset = UNSET,
    sort: ListIncidentsSort | Unset = UNSET,
    include: ListIncidentsInclude | Unset = UNSET,
) -> Response[ErrorsList | IncidentList]:
    """List incidents

     List incidents

    Args:
        pageafter (str | Unset):
        pagenumber (int | Unset):
        pagesize (int | Unset):
        filtersearch (str | Unset):
        filterkind (str | Unset):
        filterstatus (str | Unset):
        filterprivate (str | Unset):
        filteruser_id (int | Unset):
        filterseverity (str | Unset):
        filterseverity_id (str | Unset):
        filterlabels (str | Unset):
        filtertypes (str | Unset):
        filtertype_ids (str | Unset):
        filterenvironments (str | Unset):
        filterenvironment_ids (str | Unset):
        filterfunctionalities (str | Unset):
        filterfunctionality_ids (str | Unset):
        filterfunctionality_names (str | Unset):
        filterservices (str | Unset):
        filterservice_ids (str | Unset):
        filterservice_names (str | Unset):
        filterteams (str | Unset):
        filterteam_ids (str | Unset):
        filterteam_names (str | Unset):
        filtercause (str | Unset):
        filtercause_ids (str | Unset):
        filtercustom_field_selected_option_ids (str | Unset):
        filterslack_channel_id (str | Unset):
        filtersequential_id (str | Unset):
        filtercreated_atgt (str | Unset):
        filtercreated_atgte (str | Unset):
        filtercreated_atlt (str | Unset):
        filtercreated_atlte (str | Unset):
        filterupdated_atgt (str | Unset):
        filterupdated_atgte (str | Unset):
        filterupdated_atlt (str | Unset):
        filterupdated_atlte (str | Unset):
        filterstarted_atgt (str | Unset):
        filterstarted_atgte (str | Unset):
        filterstarted_atlt (str | Unset):
        filterstarted_atlte (str | Unset):
        filterdetected_atgt (str | Unset):
        filterdetected_atgte (str | Unset):
        filterdetected_atlt (str | Unset):
        filterdetected_atlte (str | Unset):
        filteracknowledged_atgt (str | Unset):
        filteracknowledged_atgte (str | Unset):
        filteracknowledged_atlt (str | Unset):
        filteracknowledged_atlte (str | Unset):
        filtermitigated_atgt (str | Unset):
        filtermitigated_atgte (str | Unset):
        filtermitigated_atlt (str | Unset):
        filtermitigated_atlte (str | Unset):
        filterresolved_atgt (str | Unset):
        filterresolved_atgte (str | Unset):
        filterresolved_atlt (str | Unset):
        filterresolved_atlte (str | Unset):
        filterclosed_atgt (str | Unset):
        filterclosed_atgte (str | Unset):
        filterclosed_atlt (str | Unset):
        filterclosed_atlte (str | Unset):
        filterin_triage_atgt (str | Unset):
        filterin_triage_atgte (str | Unset):
        filterin_triage_atlt (str | Unset):
        filterin_triage_atlte (str | Unset):
        filterkindeq (str | Unset):
        filterkindnot_eq (str | Unset):
        filterkindin (str | Unset):
        filterkindnot_in (str | Unset):
        filterstatuseq (str | Unset):
        filterstatusnot_eq (str | Unset):
        filterstatusin (str | Unset):
        filterstatusnot_in (str | Unset):
        filterprivateeq (str | Unset):
        filterprivatenot_eq (str | Unset):
        filterprivatein (str | Unset):
        filterprivatenot_in (str | Unset):
        filteruser_ideq (str | Unset):
        filteruser_idnot_eq (str | Unset):
        filteruser_idin (str | Unset):
        filteruser_idnot_in (str | Unset):
        filterseverityeq (str | Unset):
        filterseveritynot_eq (str | Unset):
        filterseverityin (str | Unset):
        filterseveritynot_in (str | Unset):
        filterseverity_ideq (str | Unset):
        filterseverity_idnot_eq (str | Unset):
        filterseverity_idin (str | Unset):
        filterseverity_idnot_in (str | Unset):
        filterlabelseq (str | Unset):
        filterlabelsnot_eq (str | Unset):
        filterlabelsin (str | Unset):
        filterlabelsnot_in (str | Unset):
        filterzendesk_ticket_ideq (str | Unset):
        filterzendesk_ticket_idnot_eq (str | Unset):
        filterzendesk_ticket_idin (str | Unset):
        filterzendesk_ticket_idnot_in (str | Unset):
        filtersequential_ideq (str | Unset):
        filtersequential_idnot_eq (str | Unset):
        filtersequential_idin (str | Unset):
        filtersequential_idnot_in (str | Unset):
        filtertypeseq (str | Unset):
        filtertypesnot_eq (str | Unset):
        filtertypesin (str | Unset):
        filtertypesnot_in (str | Unset):
        filtertype_idseq (str | Unset):
        filtertype_idsnot_eq (str | Unset):
        filtertype_idsin (str | Unset):
        filtertype_idsnot_in (str | Unset):
        filterenvironmentseq (str | Unset):
        filterenvironmentsnot_eq (str | Unset):
        filterenvironmentsin (str | Unset):
        filterenvironmentsnot_in (str | Unset):
        filterenvironment_idseq (str | Unset):
        filterenvironment_idsnot_eq (str | Unset):
        filterenvironment_idsin (str | Unset):
        filterenvironment_idsnot_in (str | Unset):
        filterserviceseq (str | Unset):
        filterservicesnot_eq (str | Unset):
        filterservicesin (str | Unset):
        filterservicesnot_in (str | Unset):
        filterservice_idseq (str | Unset):
        filterservice_idsnot_eq (str | Unset):
        filterservice_idsin (str | Unset):
        filterservice_idsnot_in (str | Unset):
        filterservice_nameseq (str | Unset):
        filterservice_namesnot_eq (str | Unset):
        filterservice_namesin (str | Unset):
        filterservice_namesnot_in (str | Unset):
        filterfunctionalitieseq (str | Unset):
        filterfunctionalitiesnot_eq (str | Unset):
        filterfunctionalitiesin (str | Unset):
        filterfunctionalitiesnot_in (str | Unset):
        filterfunctionality_idseq (str | Unset):
        filterfunctionality_idsnot_eq (str | Unset):
        filterfunctionality_idsin (str | Unset):
        filterfunctionality_idsnot_in (str | Unset):
        filterfunctionality_nameseq (str | Unset):
        filterfunctionality_namesnot_eq (str | Unset):
        filterfunctionality_namesin (str | Unset):
        filterfunctionality_namesnot_in (str | Unset):
        filtercauseseq (str | Unset):
        filtercausesnot_eq (str | Unset):
        filtercausesin (str | Unset):
        filtercausesnot_in (str | Unset):
        filtercause_idseq (str | Unset):
        filtercause_idsnot_eq (str | Unset):
        filtercause_idsin (str | Unset):
        filtercause_idsnot_in (str | Unset):
        filterteamseq (str | Unset):
        filterteamsnot_eq (str | Unset):
        filterteamsin (str | Unset):
        filterteamsnot_in (str | Unset):
        filterteam_idseq (str | Unset):
        filterteam_idsnot_eq (str | Unset):
        filterteam_idsin (str | Unset):
        filterteam_idsnot_in (str | Unset):
        filterteam_nameseq (str | Unset):
        filterteam_namesnot_eq (str | Unset):
        filterteam_namesin (str | Unset):
        filterteam_namesnot_in (str | Unset):
        sort (ListIncidentsSort | Unset):
        include (ListIncidentsInclude | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorsList | IncidentList]
    """

    kwargs = _get_kwargs(
        pageafter=pageafter,
        pagenumber=pagenumber,
        pagesize=pagesize,
        filtersearch=filtersearch,
        filterkind=filterkind,
        filterstatus=filterstatus,
        filterprivate=filterprivate,
        filteruser_id=filteruser_id,
        filterseverity=filterseverity,
        filterseverity_id=filterseverity_id,
        filterlabels=filterlabels,
        filtertypes=filtertypes,
        filtertype_ids=filtertype_ids,
        filterenvironments=filterenvironments,
        filterenvironment_ids=filterenvironment_ids,
        filterfunctionalities=filterfunctionalities,
        filterfunctionality_ids=filterfunctionality_ids,
        filterfunctionality_names=filterfunctionality_names,
        filterservices=filterservices,
        filterservice_ids=filterservice_ids,
        filterservice_names=filterservice_names,
        filterteams=filterteams,
        filterteam_ids=filterteam_ids,
        filterteam_names=filterteam_names,
        filtercause=filtercause,
        filtercause_ids=filtercause_ids,
        filtercustom_field_selected_option_ids=filtercustom_field_selected_option_ids,
        filterslack_channel_id=filterslack_channel_id,
        filtersequential_id=filtersequential_id,
        filtercreated_atgt=filtercreated_atgt,
        filtercreated_atgte=filtercreated_atgte,
        filtercreated_atlt=filtercreated_atlt,
        filtercreated_atlte=filtercreated_atlte,
        filterupdated_atgt=filterupdated_atgt,
        filterupdated_atgte=filterupdated_atgte,
        filterupdated_atlt=filterupdated_atlt,
        filterupdated_atlte=filterupdated_atlte,
        filterstarted_atgt=filterstarted_atgt,
        filterstarted_atgte=filterstarted_atgte,
        filterstarted_atlt=filterstarted_atlt,
        filterstarted_atlte=filterstarted_atlte,
        filterdetected_atgt=filterdetected_atgt,
        filterdetected_atgte=filterdetected_atgte,
        filterdetected_atlt=filterdetected_atlt,
        filterdetected_atlte=filterdetected_atlte,
        filteracknowledged_atgt=filteracknowledged_atgt,
        filteracknowledged_atgte=filteracknowledged_atgte,
        filteracknowledged_atlt=filteracknowledged_atlt,
        filteracknowledged_atlte=filteracknowledged_atlte,
        filtermitigated_atgt=filtermitigated_atgt,
        filtermitigated_atgte=filtermitigated_atgte,
        filtermitigated_atlt=filtermitigated_atlt,
        filtermitigated_atlte=filtermitigated_atlte,
        filterresolved_atgt=filterresolved_atgt,
        filterresolved_atgte=filterresolved_atgte,
        filterresolved_atlt=filterresolved_atlt,
        filterresolved_atlte=filterresolved_atlte,
        filterclosed_atgt=filterclosed_atgt,
        filterclosed_atgte=filterclosed_atgte,
        filterclosed_atlt=filterclosed_atlt,
        filterclosed_atlte=filterclosed_atlte,
        filterin_triage_atgt=filterin_triage_atgt,
        filterin_triage_atgte=filterin_triage_atgte,
        filterin_triage_atlt=filterin_triage_atlt,
        filterin_triage_atlte=filterin_triage_atlte,
        filterkindeq=filterkindeq,
        filterkindnot_eq=filterkindnot_eq,
        filterkindin=filterkindin,
        filterkindnot_in=filterkindnot_in,
        filterstatuseq=filterstatuseq,
        filterstatusnot_eq=filterstatusnot_eq,
        filterstatusin=filterstatusin,
        filterstatusnot_in=filterstatusnot_in,
        filterprivateeq=filterprivateeq,
        filterprivatenot_eq=filterprivatenot_eq,
        filterprivatein=filterprivatein,
        filterprivatenot_in=filterprivatenot_in,
        filteruser_ideq=filteruser_ideq,
        filteruser_idnot_eq=filteruser_idnot_eq,
        filteruser_idin=filteruser_idin,
        filteruser_idnot_in=filteruser_idnot_in,
        filterseverityeq=filterseverityeq,
        filterseveritynot_eq=filterseveritynot_eq,
        filterseverityin=filterseverityin,
        filterseveritynot_in=filterseveritynot_in,
        filterseverity_ideq=filterseverity_ideq,
        filterseverity_idnot_eq=filterseverity_idnot_eq,
        filterseverity_idin=filterseverity_idin,
        filterseverity_idnot_in=filterseverity_idnot_in,
        filterlabelseq=filterlabelseq,
        filterlabelsnot_eq=filterlabelsnot_eq,
        filterlabelsin=filterlabelsin,
        filterlabelsnot_in=filterlabelsnot_in,
        filterzendesk_ticket_ideq=filterzendesk_ticket_ideq,
        filterzendesk_ticket_idnot_eq=filterzendesk_ticket_idnot_eq,
        filterzendesk_ticket_idin=filterzendesk_ticket_idin,
        filterzendesk_ticket_idnot_in=filterzendesk_ticket_idnot_in,
        filtersequential_ideq=filtersequential_ideq,
        filtersequential_idnot_eq=filtersequential_idnot_eq,
        filtersequential_idin=filtersequential_idin,
        filtersequential_idnot_in=filtersequential_idnot_in,
        filtertypeseq=filtertypeseq,
        filtertypesnot_eq=filtertypesnot_eq,
        filtertypesin=filtertypesin,
        filtertypesnot_in=filtertypesnot_in,
        filtertype_idseq=filtertype_idseq,
        filtertype_idsnot_eq=filtertype_idsnot_eq,
        filtertype_idsin=filtertype_idsin,
        filtertype_idsnot_in=filtertype_idsnot_in,
        filterenvironmentseq=filterenvironmentseq,
        filterenvironmentsnot_eq=filterenvironmentsnot_eq,
        filterenvironmentsin=filterenvironmentsin,
        filterenvironmentsnot_in=filterenvironmentsnot_in,
        filterenvironment_idseq=filterenvironment_idseq,
        filterenvironment_idsnot_eq=filterenvironment_idsnot_eq,
        filterenvironment_idsin=filterenvironment_idsin,
        filterenvironment_idsnot_in=filterenvironment_idsnot_in,
        filterserviceseq=filterserviceseq,
        filterservicesnot_eq=filterservicesnot_eq,
        filterservicesin=filterservicesin,
        filterservicesnot_in=filterservicesnot_in,
        filterservice_idseq=filterservice_idseq,
        filterservice_idsnot_eq=filterservice_idsnot_eq,
        filterservice_idsin=filterservice_idsin,
        filterservice_idsnot_in=filterservice_idsnot_in,
        filterservice_nameseq=filterservice_nameseq,
        filterservice_namesnot_eq=filterservice_namesnot_eq,
        filterservice_namesin=filterservice_namesin,
        filterservice_namesnot_in=filterservice_namesnot_in,
        filterfunctionalitieseq=filterfunctionalitieseq,
        filterfunctionalitiesnot_eq=filterfunctionalitiesnot_eq,
        filterfunctionalitiesin=filterfunctionalitiesin,
        filterfunctionalitiesnot_in=filterfunctionalitiesnot_in,
        filterfunctionality_idseq=filterfunctionality_idseq,
        filterfunctionality_idsnot_eq=filterfunctionality_idsnot_eq,
        filterfunctionality_idsin=filterfunctionality_idsin,
        filterfunctionality_idsnot_in=filterfunctionality_idsnot_in,
        filterfunctionality_nameseq=filterfunctionality_nameseq,
        filterfunctionality_namesnot_eq=filterfunctionality_namesnot_eq,
        filterfunctionality_namesin=filterfunctionality_namesin,
        filterfunctionality_namesnot_in=filterfunctionality_namesnot_in,
        filtercauseseq=filtercauseseq,
        filtercausesnot_eq=filtercausesnot_eq,
        filtercausesin=filtercausesin,
        filtercausesnot_in=filtercausesnot_in,
        filtercause_idseq=filtercause_idseq,
        filtercause_idsnot_eq=filtercause_idsnot_eq,
        filtercause_idsin=filtercause_idsin,
        filtercause_idsnot_in=filtercause_idsnot_in,
        filterteamseq=filterteamseq,
        filterteamsnot_eq=filterteamsnot_eq,
        filterteamsin=filterteamsin,
        filterteamsnot_in=filterteamsnot_in,
        filterteam_idseq=filterteam_idseq,
        filterteam_idsnot_eq=filterteam_idsnot_eq,
        filterteam_idsin=filterteam_idsin,
        filterteam_idsnot_in=filterteam_idsnot_in,
        filterteam_nameseq=filterteam_nameseq,
        filterteam_namesnot_eq=filterteam_namesnot_eq,
        filterteam_namesin=filterteam_namesin,
        filterteam_namesnot_in=filterteam_namesnot_in,
        sort=sort,
        include=include,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    pageafter: str | Unset = UNSET,
    pagenumber: int | Unset = UNSET,
    pagesize: int | Unset = UNSET,
    filtersearch: str | Unset = UNSET,
    filterkind: str | Unset = UNSET,
    filterstatus: str | Unset = UNSET,
    filterprivate: str | Unset = UNSET,
    filteruser_id: int | Unset = UNSET,
    filterseverity: str | Unset = UNSET,
    filterseverity_id: str | Unset = UNSET,
    filterlabels: str | Unset = UNSET,
    filtertypes: str | Unset = UNSET,
    filtertype_ids: str | Unset = UNSET,
    filterenvironments: str | Unset = UNSET,
    filterenvironment_ids: str | Unset = UNSET,
    filterfunctionalities: str | Unset = UNSET,
    filterfunctionality_ids: str | Unset = UNSET,
    filterfunctionality_names: str | Unset = UNSET,
    filterservices: str | Unset = UNSET,
    filterservice_ids: str | Unset = UNSET,
    filterservice_names: str | Unset = UNSET,
    filterteams: str | Unset = UNSET,
    filterteam_ids: str | Unset = UNSET,
    filterteam_names: str | Unset = UNSET,
    filtercause: str | Unset = UNSET,
    filtercause_ids: str | Unset = UNSET,
    filtercustom_field_selected_option_ids: str | Unset = UNSET,
    filterslack_channel_id: str | Unset = UNSET,
    filtersequential_id: str | Unset = UNSET,
    filtercreated_atgt: str | Unset = UNSET,
    filtercreated_atgte: str | Unset = UNSET,
    filtercreated_atlt: str | Unset = UNSET,
    filtercreated_atlte: str | Unset = UNSET,
    filterupdated_atgt: str | Unset = UNSET,
    filterupdated_atgte: str | Unset = UNSET,
    filterupdated_atlt: str | Unset = UNSET,
    filterupdated_atlte: str | Unset = UNSET,
    filterstarted_atgt: str | Unset = UNSET,
    filterstarted_atgte: str | Unset = UNSET,
    filterstarted_atlt: str | Unset = UNSET,
    filterstarted_atlte: str | Unset = UNSET,
    filterdetected_atgt: str | Unset = UNSET,
    filterdetected_atgte: str | Unset = UNSET,
    filterdetected_atlt: str | Unset = UNSET,
    filterdetected_atlte: str | Unset = UNSET,
    filteracknowledged_atgt: str | Unset = UNSET,
    filteracknowledged_atgte: str | Unset = UNSET,
    filteracknowledged_atlt: str | Unset = UNSET,
    filteracknowledged_atlte: str | Unset = UNSET,
    filtermitigated_atgt: str | Unset = UNSET,
    filtermitigated_atgte: str | Unset = UNSET,
    filtermitigated_atlt: str | Unset = UNSET,
    filtermitigated_atlte: str | Unset = UNSET,
    filterresolved_atgt: str | Unset = UNSET,
    filterresolved_atgte: str | Unset = UNSET,
    filterresolved_atlt: str | Unset = UNSET,
    filterresolved_atlte: str | Unset = UNSET,
    filterclosed_atgt: str | Unset = UNSET,
    filterclosed_atgte: str | Unset = UNSET,
    filterclosed_atlt: str | Unset = UNSET,
    filterclosed_atlte: str | Unset = UNSET,
    filterin_triage_atgt: str | Unset = UNSET,
    filterin_triage_atgte: str | Unset = UNSET,
    filterin_triage_atlt: str | Unset = UNSET,
    filterin_triage_atlte: str | Unset = UNSET,
    filterkindeq: str | Unset = UNSET,
    filterkindnot_eq: str | Unset = UNSET,
    filterkindin: str | Unset = UNSET,
    filterkindnot_in: str | Unset = UNSET,
    filterstatuseq: str | Unset = UNSET,
    filterstatusnot_eq: str | Unset = UNSET,
    filterstatusin: str | Unset = UNSET,
    filterstatusnot_in: str | Unset = UNSET,
    filterprivateeq: str | Unset = UNSET,
    filterprivatenot_eq: str | Unset = UNSET,
    filterprivatein: str | Unset = UNSET,
    filterprivatenot_in: str | Unset = UNSET,
    filteruser_ideq: str | Unset = UNSET,
    filteruser_idnot_eq: str | Unset = UNSET,
    filteruser_idin: str | Unset = UNSET,
    filteruser_idnot_in: str | Unset = UNSET,
    filterseverityeq: str | Unset = UNSET,
    filterseveritynot_eq: str | Unset = UNSET,
    filterseverityin: str | Unset = UNSET,
    filterseveritynot_in: str | Unset = UNSET,
    filterseverity_ideq: str | Unset = UNSET,
    filterseverity_idnot_eq: str | Unset = UNSET,
    filterseverity_idin: str | Unset = UNSET,
    filterseverity_idnot_in: str | Unset = UNSET,
    filterlabelseq: str | Unset = UNSET,
    filterlabelsnot_eq: str | Unset = UNSET,
    filterlabelsin: str | Unset = UNSET,
    filterlabelsnot_in: str | Unset = UNSET,
    filterzendesk_ticket_ideq: str | Unset = UNSET,
    filterzendesk_ticket_idnot_eq: str | Unset = UNSET,
    filterzendesk_ticket_idin: str | Unset = UNSET,
    filterzendesk_ticket_idnot_in: str | Unset = UNSET,
    filtersequential_ideq: str | Unset = UNSET,
    filtersequential_idnot_eq: str | Unset = UNSET,
    filtersequential_idin: str | Unset = UNSET,
    filtersequential_idnot_in: str | Unset = UNSET,
    filtertypeseq: str | Unset = UNSET,
    filtertypesnot_eq: str | Unset = UNSET,
    filtertypesin: str | Unset = UNSET,
    filtertypesnot_in: str | Unset = UNSET,
    filtertype_idseq: str | Unset = UNSET,
    filtertype_idsnot_eq: str | Unset = UNSET,
    filtertype_idsin: str | Unset = UNSET,
    filtertype_idsnot_in: str | Unset = UNSET,
    filterenvironmentseq: str | Unset = UNSET,
    filterenvironmentsnot_eq: str | Unset = UNSET,
    filterenvironmentsin: str | Unset = UNSET,
    filterenvironmentsnot_in: str | Unset = UNSET,
    filterenvironment_idseq: str | Unset = UNSET,
    filterenvironment_idsnot_eq: str | Unset = UNSET,
    filterenvironment_idsin: str | Unset = UNSET,
    filterenvironment_idsnot_in: str | Unset = UNSET,
    filterserviceseq: str | Unset = UNSET,
    filterservicesnot_eq: str | Unset = UNSET,
    filterservicesin: str | Unset = UNSET,
    filterservicesnot_in: str | Unset = UNSET,
    filterservice_idseq: str | Unset = UNSET,
    filterservice_idsnot_eq: str | Unset = UNSET,
    filterservice_idsin: str | Unset = UNSET,
    filterservice_idsnot_in: str | Unset = UNSET,
    filterservice_nameseq: str | Unset = UNSET,
    filterservice_namesnot_eq: str | Unset = UNSET,
    filterservice_namesin: str | Unset = UNSET,
    filterservice_namesnot_in: str | Unset = UNSET,
    filterfunctionalitieseq: str | Unset = UNSET,
    filterfunctionalitiesnot_eq: str | Unset = UNSET,
    filterfunctionalitiesin: str | Unset = UNSET,
    filterfunctionalitiesnot_in: str | Unset = UNSET,
    filterfunctionality_idseq: str | Unset = UNSET,
    filterfunctionality_idsnot_eq: str | Unset = UNSET,
    filterfunctionality_idsin: str | Unset = UNSET,
    filterfunctionality_idsnot_in: str | Unset = UNSET,
    filterfunctionality_nameseq: str | Unset = UNSET,
    filterfunctionality_namesnot_eq: str | Unset = UNSET,
    filterfunctionality_namesin: str | Unset = UNSET,
    filterfunctionality_namesnot_in: str | Unset = UNSET,
    filtercauseseq: str | Unset = UNSET,
    filtercausesnot_eq: str | Unset = UNSET,
    filtercausesin: str | Unset = UNSET,
    filtercausesnot_in: str | Unset = UNSET,
    filtercause_idseq: str | Unset = UNSET,
    filtercause_idsnot_eq: str | Unset = UNSET,
    filtercause_idsin: str | Unset = UNSET,
    filtercause_idsnot_in: str | Unset = UNSET,
    filterteamseq: str | Unset = UNSET,
    filterteamsnot_eq: str | Unset = UNSET,
    filterteamsin: str | Unset = UNSET,
    filterteamsnot_in: str | Unset = UNSET,
    filterteam_idseq: str | Unset = UNSET,
    filterteam_idsnot_eq: str | Unset = UNSET,
    filterteam_idsin: str | Unset = UNSET,
    filterteam_idsnot_in: str | Unset = UNSET,
    filterteam_nameseq: str | Unset = UNSET,
    filterteam_namesnot_eq: str | Unset = UNSET,
    filterteam_namesin: str | Unset = UNSET,
    filterteam_namesnot_in: str | Unset = UNSET,
    sort: ListIncidentsSort | Unset = UNSET,
    include: ListIncidentsInclude | Unset = UNSET,
) -> ErrorsList | IncidentList | None:
    """List incidents

     List incidents

    Args:
        pageafter (str | Unset):
        pagenumber (int | Unset):
        pagesize (int | Unset):
        filtersearch (str | Unset):
        filterkind (str | Unset):
        filterstatus (str | Unset):
        filterprivate (str | Unset):
        filteruser_id (int | Unset):
        filterseverity (str | Unset):
        filterseverity_id (str | Unset):
        filterlabels (str | Unset):
        filtertypes (str | Unset):
        filtertype_ids (str | Unset):
        filterenvironments (str | Unset):
        filterenvironment_ids (str | Unset):
        filterfunctionalities (str | Unset):
        filterfunctionality_ids (str | Unset):
        filterfunctionality_names (str | Unset):
        filterservices (str | Unset):
        filterservice_ids (str | Unset):
        filterservice_names (str | Unset):
        filterteams (str | Unset):
        filterteam_ids (str | Unset):
        filterteam_names (str | Unset):
        filtercause (str | Unset):
        filtercause_ids (str | Unset):
        filtercustom_field_selected_option_ids (str | Unset):
        filterslack_channel_id (str | Unset):
        filtersequential_id (str | Unset):
        filtercreated_atgt (str | Unset):
        filtercreated_atgte (str | Unset):
        filtercreated_atlt (str | Unset):
        filtercreated_atlte (str | Unset):
        filterupdated_atgt (str | Unset):
        filterupdated_atgte (str | Unset):
        filterupdated_atlt (str | Unset):
        filterupdated_atlte (str | Unset):
        filterstarted_atgt (str | Unset):
        filterstarted_atgte (str | Unset):
        filterstarted_atlt (str | Unset):
        filterstarted_atlte (str | Unset):
        filterdetected_atgt (str | Unset):
        filterdetected_atgte (str | Unset):
        filterdetected_atlt (str | Unset):
        filterdetected_atlte (str | Unset):
        filteracknowledged_atgt (str | Unset):
        filteracknowledged_atgte (str | Unset):
        filteracknowledged_atlt (str | Unset):
        filteracknowledged_atlte (str | Unset):
        filtermitigated_atgt (str | Unset):
        filtermitigated_atgte (str | Unset):
        filtermitigated_atlt (str | Unset):
        filtermitigated_atlte (str | Unset):
        filterresolved_atgt (str | Unset):
        filterresolved_atgte (str | Unset):
        filterresolved_atlt (str | Unset):
        filterresolved_atlte (str | Unset):
        filterclosed_atgt (str | Unset):
        filterclosed_atgte (str | Unset):
        filterclosed_atlt (str | Unset):
        filterclosed_atlte (str | Unset):
        filterin_triage_atgt (str | Unset):
        filterin_triage_atgte (str | Unset):
        filterin_triage_atlt (str | Unset):
        filterin_triage_atlte (str | Unset):
        filterkindeq (str | Unset):
        filterkindnot_eq (str | Unset):
        filterkindin (str | Unset):
        filterkindnot_in (str | Unset):
        filterstatuseq (str | Unset):
        filterstatusnot_eq (str | Unset):
        filterstatusin (str | Unset):
        filterstatusnot_in (str | Unset):
        filterprivateeq (str | Unset):
        filterprivatenot_eq (str | Unset):
        filterprivatein (str | Unset):
        filterprivatenot_in (str | Unset):
        filteruser_ideq (str | Unset):
        filteruser_idnot_eq (str | Unset):
        filteruser_idin (str | Unset):
        filteruser_idnot_in (str | Unset):
        filterseverityeq (str | Unset):
        filterseveritynot_eq (str | Unset):
        filterseverityin (str | Unset):
        filterseveritynot_in (str | Unset):
        filterseverity_ideq (str | Unset):
        filterseverity_idnot_eq (str | Unset):
        filterseverity_idin (str | Unset):
        filterseverity_idnot_in (str | Unset):
        filterlabelseq (str | Unset):
        filterlabelsnot_eq (str | Unset):
        filterlabelsin (str | Unset):
        filterlabelsnot_in (str | Unset):
        filterzendesk_ticket_ideq (str | Unset):
        filterzendesk_ticket_idnot_eq (str | Unset):
        filterzendesk_ticket_idin (str | Unset):
        filterzendesk_ticket_idnot_in (str | Unset):
        filtersequential_ideq (str | Unset):
        filtersequential_idnot_eq (str | Unset):
        filtersequential_idin (str | Unset):
        filtersequential_idnot_in (str | Unset):
        filtertypeseq (str | Unset):
        filtertypesnot_eq (str | Unset):
        filtertypesin (str | Unset):
        filtertypesnot_in (str | Unset):
        filtertype_idseq (str | Unset):
        filtertype_idsnot_eq (str | Unset):
        filtertype_idsin (str | Unset):
        filtertype_idsnot_in (str | Unset):
        filterenvironmentseq (str | Unset):
        filterenvironmentsnot_eq (str | Unset):
        filterenvironmentsin (str | Unset):
        filterenvironmentsnot_in (str | Unset):
        filterenvironment_idseq (str | Unset):
        filterenvironment_idsnot_eq (str | Unset):
        filterenvironment_idsin (str | Unset):
        filterenvironment_idsnot_in (str | Unset):
        filterserviceseq (str | Unset):
        filterservicesnot_eq (str | Unset):
        filterservicesin (str | Unset):
        filterservicesnot_in (str | Unset):
        filterservice_idseq (str | Unset):
        filterservice_idsnot_eq (str | Unset):
        filterservice_idsin (str | Unset):
        filterservice_idsnot_in (str | Unset):
        filterservice_nameseq (str | Unset):
        filterservice_namesnot_eq (str | Unset):
        filterservice_namesin (str | Unset):
        filterservice_namesnot_in (str | Unset):
        filterfunctionalitieseq (str | Unset):
        filterfunctionalitiesnot_eq (str | Unset):
        filterfunctionalitiesin (str | Unset):
        filterfunctionalitiesnot_in (str | Unset):
        filterfunctionality_idseq (str | Unset):
        filterfunctionality_idsnot_eq (str | Unset):
        filterfunctionality_idsin (str | Unset):
        filterfunctionality_idsnot_in (str | Unset):
        filterfunctionality_nameseq (str | Unset):
        filterfunctionality_namesnot_eq (str | Unset):
        filterfunctionality_namesin (str | Unset):
        filterfunctionality_namesnot_in (str | Unset):
        filtercauseseq (str | Unset):
        filtercausesnot_eq (str | Unset):
        filtercausesin (str | Unset):
        filtercausesnot_in (str | Unset):
        filtercause_idseq (str | Unset):
        filtercause_idsnot_eq (str | Unset):
        filtercause_idsin (str | Unset):
        filtercause_idsnot_in (str | Unset):
        filterteamseq (str | Unset):
        filterteamsnot_eq (str | Unset):
        filterteamsin (str | Unset):
        filterteamsnot_in (str | Unset):
        filterteam_idseq (str | Unset):
        filterteam_idsnot_eq (str | Unset):
        filterteam_idsin (str | Unset):
        filterteam_idsnot_in (str | Unset):
        filterteam_nameseq (str | Unset):
        filterteam_namesnot_eq (str | Unset):
        filterteam_namesin (str | Unset):
        filterteam_namesnot_in (str | Unset):
        sort (ListIncidentsSort | Unset):
        include (ListIncidentsInclude | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorsList | IncidentList
    """

    return (
        await asyncio_detailed(
            client=client,
            pageafter=pageafter,
            pagenumber=pagenumber,
            pagesize=pagesize,
            filtersearch=filtersearch,
            filterkind=filterkind,
            filterstatus=filterstatus,
            filterprivate=filterprivate,
            filteruser_id=filteruser_id,
            filterseverity=filterseverity,
            filterseverity_id=filterseverity_id,
            filterlabels=filterlabels,
            filtertypes=filtertypes,
            filtertype_ids=filtertype_ids,
            filterenvironments=filterenvironments,
            filterenvironment_ids=filterenvironment_ids,
            filterfunctionalities=filterfunctionalities,
            filterfunctionality_ids=filterfunctionality_ids,
            filterfunctionality_names=filterfunctionality_names,
            filterservices=filterservices,
            filterservice_ids=filterservice_ids,
            filterservice_names=filterservice_names,
            filterteams=filterteams,
            filterteam_ids=filterteam_ids,
            filterteam_names=filterteam_names,
            filtercause=filtercause,
            filtercause_ids=filtercause_ids,
            filtercustom_field_selected_option_ids=filtercustom_field_selected_option_ids,
            filterslack_channel_id=filterslack_channel_id,
            filtersequential_id=filtersequential_id,
            filtercreated_atgt=filtercreated_atgt,
            filtercreated_atgte=filtercreated_atgte,
            filtercreated_atlt=filtercreated_atlt,
            filtercreated_atlte=filtercreated_atlte,
            filterupdated_atgt=filterupdated_atgt,
            filterupdated_atgte=filterupdated_atgte,
            filterupdated_atlt=filterupdated_atlt,
            filterupdated_atlte=filterupdated_atlte,
            filterstarted_atgt=filterstarted_atgt,
            filterstarted_atgte=filterstarted_atgte,
            filterstarted_atlt=filterstarted_atlt,
            filterstarted_atlte=filterstarted_atlte,
            filterdetected_atgt=filterdetected_atgt,
            filterdetected_atgte=filterdetected_atgte,
            filterdetected_atlt=filterdetected_atlt,
            filterdetected_atlte=filterdetected_atlte,
            filteracknowledged_atgt=filteracknowledged_atgt,
            filteracknowledged_atgte=filteracknowledged_atgte,
            filteracknowledged_atlt=filteracknowledged_atlt,
            filteracknowledged_atlte=filteracknowledged_atlte,
            filtermitigated_atgt=filtermitigated_atgt,
            filtermitigated_atgte=filtermitigated_atgte,
            filtermitigated_atlt=filtermitigated_atlt,
            filtermitigated_atlte=filtermitigated_atlte,
            filterresolved_atgt=filterresolved_atgt,
            filterresolved_atgte=filterresolved_atgte,
            filterresolved_atlt=filterresolved_atlt,
            filterresolved_atlte=filterresolved_atlte,
            filterclosed_atgt=filterclosed_atgt,
            filterclosed_atgte=filterclosed_atgte,
            filterclosed_atlt=filterclosed_atlt,
            filterclosed_atlte=filterclosed_atlte,
            filterin_triage_atgt=filterin_triage_atgt,
            filterin_triage_atgte=filterin_triage_atgte,
            filterin_triage_atlt=filterin_triage_atlt,
            filterin_triage_atlte=filterin_triage_atlte,
            filterkindeq=filterkindeq,
            filterkindnot_eq=filterkindnot_eq,
            filterkindin=filterkindin,
            filterkindnot_in=filterkindnot_in,
            filterstatuseq=filterstatuseq,
            filterstatusnot_eq=filterstatusnot_eq,
            filterstatusin=filterstatusin,
            filterstatusnot_in=filterstatusnot_in,
            filterprivateeq=filterprivateeq,
            filterprivatenot_eq=filterprivatenot_eq,
            filterprivatein=filterprivatein,
            filterprivatenot_in=filterprivatenot_in,
            filteruser_ideq=filteruser_ideq,
            filteruser_idnot_eq=filteruser_idnot_eq,
            filteruser_idin=filteruser_idin,
            filteruser_idnot_in=filteruser_idnot_in,
            filterseverityeq=filterseverityeq,
            filterseveritynot_eq=filterseveritynot_eq,
            filterseverityin=filterseverityin,
            filterseveritynot_in=filterseveritynot_in,
            filterseverity_ideq=filterseverity_ideq,
            filterseverity_idnot_eq=filterseverity_idnot_eq,
            filterseverity_idin=filterseverity_idin,
            filterseverity_idnot_in=filterseverity_idnot_in,
            filterlabelseq=filterlabelseq,
            filterlabelsnot_eq=filterlabelsnot_eq,
            filterlabelsin=filterlabelsin,
            filterlabelsnot_in=filterlabelsnot_in,
            filterzendesk_ticket_ideq=filterzendesk_ticket_ideq,
            filterzendesk_ticket_idnot_eq=filterzendesk_ticket_idnot_eq,
            filterzendesk_ticket_idin=filterzendesk_ticket_idin,
            filterzendesk_ticket_idnot_in=filterzendesk_ticket_idnot_in,
            filtersequential_ideq=filtersequential_ideq,
            filtersequential_idnot_eq=filtersequential_idnot_eq,
            filtersequential_idin=filtersequential_idin,
            filtersequential_idnot_in=filtersequential_idnot_in,
            filtertypeseq=filtertypeseq,
            filtertypesnot_eq=filtertypesnot_eq,
            filtertypesin=filtertypesin,
            filtertypesnot_in=filtertypesnot_in,
            filtertype_idseq=filtertype_idseq,
            filtertype_idsnot_eq=filtertype_idsnot_eq,
            filtertype_idsin=filtertype_idsin,
            filtertype_idsnot_in=filtertype_idsnot_in,
            filterenvironmentseq=filterenvironmentseq,
            filterenvironmentsnot_eq=filterenvironmentsnot_eq,
            filterenvironmentsin=filterenvironmentsin,
            filterenvironmentsnot_in=filterenvironmentsnot_in,
            filterenvironment_idseq=filterenvironment_idseq,
            filterenvironment_idsnot_eq=filterenvironment_idsnot_eq,
            filterenvironment_idsin=filterenvironment_idsin,
            filterenvironment_idsnot_in=filterenvironment_idsnot_in,
            filterserviceseq=filterserviceseq,
            filterservicesnot_eq=filterservicesnot_eq,
            filterservicesin=filterservicesin,
            filterservicesnot_in=filterservicesnot_in,
            filterservice_idseq=filterservice_idseq,
            filterservice_idsnot_eq=filterservice_idsnot_eq,
            filterservice_idsin=filterservice_idsin,
            filterservice_idsnot_in=filterservice_idsnot_in,
            filterservice_nameseq=filterservice_nameseq,
            filterservice_namesnot_eq=filterservice_namesnot_eq,
            filterservice_namesin=filterservice_namesin,
            filterservice_namesnot_in=filterservice_namesnot_in,
            filterfunctionalitieseq=filterfunctionalitieseq,
            filterfunctionalitiesnot_eq=filterfunctionalitiesnot_eq,
            filterfunctionalitiesin=filterfunctionalitiesin,
            filterfunctionalitiesnot_in=filterfunctionalitiesnot_in,
            filterfunctionality_idseq=filterfunctionality_idseq,
            filterfunctionality_idsnot_eq=filterfunctionality_idsnot_eq,
            filterfunctionality_idsin=filterfunctionality_idsin,
            filterfunctionality_idsnot_in=filterfunctionality_idsnot_in,
            filterfunctionality_nameseq=filterfunctionality_nameseq,
            filterfunctionality_namesnot_eq=filterfunctionality_namesnot_eq,
            filterfunctionality_namesin=filterfunctionality_namesin,
            filterfunctionality_namesnot_in=filterfunctionality_namesnot_in,
            filtercauseseq=filtercauseseq,
            filtercausesnot_eq=filtercausesnot_eq,
            filtercausesin=filtercausesin,
            filtercausesnot_in=filtercausesnot_in,
            filtercause_idseq=filtercause_idseq,
            filtercause_idsnot_eq=filtercause_idsnot_eq,
            filtercause_idsin=filtercause_idsin,
            filtercause_idsnot_in=filtercause_idsnot_in,
            filterteamseq=filterteamseq,
            filterteamsnot_eq=filterteamsnot_eq,
            filterteamsin=filterteamsin,
            filterteamsnot_in=filterteamsnot_in,
            filterteam_idseq=filterteam_idseq,
            filterteam_idsnot_eq=filterteam_idsnot_eq,
            filterteam_idsin=filterteam_idsin,
            filterteam_idsnot_in=filterteam_idsnot_in,
            filterteam_nameseq=filterteam_nameseq,
            filterteam_namesnot_eq=filterteam_namesnot_eq,
            filterteam_namesin=filterteam_namesin,
            filterteam_namesnot_in=filterteam_namesnot_in,
            sort=sort,
            include=include,
        )
    ).parsed
