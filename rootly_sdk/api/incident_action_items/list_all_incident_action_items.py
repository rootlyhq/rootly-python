from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.incident_action_item_list import IncidentActionItemList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    include: Union[Unset, str] = UNSET,
    pagenumber: Union[Unset, int] = UNSET,
    pagesize: Union[Unset, int] = UNSET,
    filterkind: Union[Unset, str] = UNSET,
    filterpriority: Union[Unset, str] = UNSET,
    filterstatus: Union[Unset, str] = UNSET,
    filterincident_status: Union[Unset, str] = UNSET,
    filterincident_created_atgt: Union[Unset, str] = UNSET,
    filterincident_created_atgte: Union[Unset, str] = UNSET,
    filterincident_created_atlt: Union[Unset, str] = UNSET,
    filterincident_created_atlte: Union[Unset, str] = UNSET,
    filterdue_dategt: Union[Unset, str] = UNSET,
    filterdue_dategte: Union[Unset, str] = UNSET,
    filterdue_datelt: Union[Unset, str] = UNSET,
    filterdue_datelte: Union[Unset, str] = UNSET,
    filtercreated_atgt: Union[Unset, str] = UNSET,
    filtercreated_atgte: Union[Unset, str] = UNSET,
    filtercreated_atlt: Union[Unset, str] = UNSET,
    filtercreated_atlte: Union[Unset, str] = UNSET,
    filterkindeq: Union[Unset, str] = UNSET,
    filterkindnot_eq: Union[Unset, str] = UNSET,
    filterkindin: Union[Unset, str] = UNSET,
    filterkindnot_in: Union[Unset, str] = UNSET,
    filterpriorityeq: Union[Unset, str] = UNSET,
    filterprioritynot_eq: Union[Unset, str] = UNSET,
    filterpriorityin: Union[Unset, str] = UNSET,
    filterprioritynot_in: Union[Unset, str] = UNSET,
    filterstatuseq: Union[Unset, str] = UNSET,
    filterstatusnot_eq: Union[Unset, str] = UNSET,
    filterstatusin: Union[Unset, str] = UNSET,
    filterstatusnot_in: Union[Unset, str] = UNSET,
    filterincident_statuseq: Union[Unset, str] = UNSET,
    filterincident_statusnot_eq: Union[Unset, str] = UNSET,
    filterincident_statusin: Union[Unset, str] = UNSET,
    filterincident_statusnot_in: Union[Unset, str] = UNSET,
    sort: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["include"] = include

    params["page[number]"] = pagenumber

    params["page[size]"] = pagesize

    params["filter[kind]"] = filterkind

    params["filter[priority]"] = filterpriority

    params["filter[status]"] = filterstatus

    params["filter[incident_status]"] = filterincident_status

    params["filter[incident_created_at][gt]"] = filterincident_created_atgt

    params["filter[incident_created_at][gte]"] = filterincident_created_atgte

    params["filter[incident_created_at][lt]"] = filterincident_created_atlt

    params["filter[incident_created_at][lte]"] = filterincident_created_atlte

    params["filter[due_date][gt]"] = filterdue_dategt

    params["filter[due_date][gte]"] = filterdue_dategte

    params["filter[due_date][lt]"] = filterdue_datelt

    params["filter[due_date][lte]"] = filterdue_datelte

    params["filter[created_at][gt]"] = filtercreated_atgt

    params["filter[created_at][gte]"] = filtercreated_atgte

    params["filter[created_at][lt]"] = filtercreated_atlt

    params["filter[created_at][lte]"] = filtercreated_atlte

    params["filter[kind][eq]"] = filterkindeq

    params["filter[kind][not_eq]"] = filterkindnot_eq

    params["filter[kind][in]"] = filterkindin

    params["filter[kind][not_in]"] = filterkindnot_in

    params["filter[priority][eq]"] = filterpriorityeq

    params["filter[priority][not_eq]"] = filterprioritynot_eq

    params["filter[priority][in]"] = filterpriorityin

    params["filter[priority][not_in]"] = filterprioritynot_in

    params["filter[status][eq]"] = filterstatuseq

    params["filter[status][not_eq]"] = filterstatusnot_eq

    params["filter[status][in]"] = filterstatusin

    params["filter[status][not_in]"] = filterstatusnot_in

    params["filter[incident_status][eq]"] = filterincident_statuseq

    params["filter[incident_status][not_eq]"] = filterincident_statusnot_eq

    params["filter[incident_status][in]"] = filterincident_statusin

    params["filter[incident_status][not_in]"] = filterincident_statusnot_in

    params["sort"] = sort

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/action_items",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[IncidentActionItemList]:
    if response.status_code == 200:
        response_200 = IncidentActionItemList.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[IncidentActionItemList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    include: Union[Unset, str] = UNSET,
    pagenumber: Union[Unset, int] = UNSET,
    pagesize: Union[Unset, int] = UNSET,
    filterkind: Union[Unset, str] = UNSET,
    filterpriority: Union[Unset, str] = UNSET,
    filterstatus: Union[Unset, str] = UNSET,
    filterincident_status: Union[Unset, str] = UNSET,
    filterincident_created_atgt: Union[Unset, str] = UNSET,
    filterincident_created_atgte: Union[Unset, str] = UNSET,
    filterincident_created_atlt: Union[Unset, str] = UNSET,
    filterincident_created_atlte: Union[Unset, str] = UNSET,
    filterdue_dategt: Union[Unset, str] = UNSET,
    filterdue_dategte: Union[Unset, str] = UNSET,
    filterdue_datelt: Union[Unset, str] = UNSET,
    filterdue_datelte: Union[Unset, str] = UNSET,
    filtercreated_atgt: Union[Unset, str] = UNSET,
    filtercreated_atgte: Union[Unset, str] = UNSET,
    filtercreated_atlt: Union[Unset, str] = UNSET,
    filtercreated_atlte: Union[Unset, str] = UNSET,
    filterkindeq: Union[Unset, str] = UNSET,
    filterkindnot_eq: Union[Unset, str] = UNSET,
    filterkindin: Union[Unset, str] = UNSET,
    filterkindnot_in: Union[Unset, str] = UNSET,
    filterpriorityeq: Union[Unset, str] = UNSET,
    filterprioritynot_eq: Union[Unset, str] = UNSET,
    filterpriorityin: Union[Unset, str] = UNSET,
    filterprioritynot_in: Union[Unset, str] = UNSET,
    filterstatuseq: Union[Unset, str] = UNSET,
    filterstatusnot_eq: Union[Unset, str] = UNSET,
    filterstatusin: Union[Unset, str] = UNSET,
    filterstatusnot_in: Union[Unset, str] = UNSET,
    filterincident_statuseq: Union[Unset, str] = UNSET,
    filterincident_statusnot_eq: Union[Unset, str] = UNSET,
    filterincident_statusin: Union[Unset, str] = UNSET,
    filterincident_statusnot_in: Union[Unset, str] = UNSET,
    sort: Union[Unset, str] = UNSET,
) -> Response[IncidentActionItemList]:
    """List all action items for an organization

     List all action items for an organization

    Args:
        include (Union[Unset, str]):
        pagenumber (Union[Unset, int]):
        pagesize (Union[Unset, int]):
        filterkind (Union[Unset, str]):
        filterpriority (Union[Unset, str]):
        filterstatus (Union[Unset, str]):
        filterincident_status (Union[Unset, str]):
        filterincident_created_atgt (Union[Unset, str]):
        filterincident_created_atgte (Union[Unset, str]):
        filterincident_created_atlt (Union[Unset, str]):
        filterincident_created_atlte (Union[Unset, str]):
        filterdue_dategt (Union[Unset, str]):
        filterdue_dategte (Union[Unset, str]):
        filterdue_datelt (Union[Unset, str]):
        filterdue_datelte (Union[Unset, str]):
        filtercreated_atgt (Union[Unset, str]):
        filtercreated_atgte (Union[Unset, str]):
        filtercreated_atlt (Union[Unset, str]):
        filtercreated_atlte (Union[Unset, str]):
        filterkindeq (Union[Unset, str]):
        filterkindnot_eq (Union[Unset, str]):
        filterkindin (Union[Unset, str]):
        filterkindnot_in (Union[Unset, str]):
        filterpriorityeq (Union[Unset, str]):
        filterprioritynot_eq (Union[Unset, str]):
        filterpriorityin (Union[Unset, str]):
        filterprioritynot_in (Union[Unset, str]):
        filterstatuseq (Union[Unset, str]):
        filterstatusnot_eq (Union[Unset, str]):
        filterstatusin (Union[Unset, str]):
        filterstatusnot_in (Union[Unset, str]):
        filterincident_statuseq (Union[Unset, str]):
        filterincident_statusnot_eq (Union[Unset, str]):
        filterincident_statusin (Union[Unset, str]):
        filterincident_statusnot_in (Union[Unset, str]):
        sort (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[IncidentActionItemList]
    """

    kwargs = _get_kwargs(
        include=include,
        pagenumber=pagenumber,
        pagesize=pagesize,
        filterkind=filterkind,
        filterpriority=filterpriority,
        filterstatus=filterstatus,
        filterincident_status=filterincident_status,
        filterincident_created_atgt=filterincident_created_atgt,
        filterincident_created_atgte=filterincident_created_atgte,
        filterincident_created_atlt=filterincident_created_atlt,
        filterincident_created_atlte=filterincident_created_atlte,
        filterdue_dategt=filterdue_dategt,
        filterdue_dategte=filterdue_dategte,
        filterdue_datelt=filterdue_datelt,
        filterdue_datelte=filterdue_datelte,
        filtercreated_atgt=filtercreated_atgt,
        filtercreated_atgte=filtercreated_atgte,
        filtercreated_atlt=filtercreated_atlt,
        filtercreated_atlte=filtercreated_atlte,
        filterkindeq=filterkindeq,
        filterkindnot_eq=filterkindnot_eq,
        filterkindin=filterkindin,
        filterkindnot_in=filterkindnot_in,
        filterpriorityeq=filterpriorityeq,
        filterprioritynot_eq=filterprioritynot_eq,
        filterpriorityin=filterpriorityin,
        filterprioritynot_in=filterprioritynot_in,
        filterstatuseq=filterstatuseq,
        filterstatusnot_eq=filterstatusnot_eq,
        filterstatusin=filterstatusin,
        filterstatusnot_in=filterstatusnot_in,
        filterincident_statuseq=filterincident_statuseq,
        filterincident_statusnot_eq=filterincident_statusnot_eq,
        filterincident_statusin=filterincident_statusin,
        filterincident_statusnot_in=filterincident_statusnot_in,
        sort=sort,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    include: Union[Unset, str] = UNSET,
    pagenumber: Union[Unset, int] = UNSET,
    pagesize: Union[Unset, int] = UNSET,
    filterkind: Union[Unset, str] = UNSET,
    filterpriority: Union[Unset, str] = UNSET,
    filterstatus: Union[Unset, str] = UNSET,
    filterincident_status: Union[Unset, str] = UNSET,
    filterincident_created_atgt: Union[Unset, str] = UNSET,
    filterincident_created_atgte: Union[Unset, str] = UNSET,
    filterincident_created_atlt: Union[Unset, str] = UNSET,
    filterincident_created_atlte: Union[Unset, str] = UNSET,
    filterdue_dategt: Union[Unset, str] = UNSET,
    filterdue_dategte: Union[Unset, str] = UNSET,
    filterdue_datelt: Union[Unset, str] = UNSET,
    filterdue_datelte: Union[Unset, str] = UNSET,
    filtercreated_atgt: Union[Unset, str] = UNSET,
    filtercreated_atgte: Union[Unset, str] = UNSET,
    filtercreated_atlt: Union[Unset, str] = UNSET,
    filtercreated_atlte: Union[Unset, str] = UNSET,
    filterkindeq: Union[Unset, str] = UNSET,
    filterkindnot_eq: Union[Unset, str] = UNSET,
    filterkindin: Union[Unset, str] = UNSET,
    filterkindnot_in: Union[Unset, str] = UNSET,
    filterpriorityeq: Union[Unset, str] = UNSET,
    filterprioritynot_eq: Union[Unset, str] = UNSET,
    filterpriorityin: Union[Unset, str] = UNSET,
    filterprioritynot_in: Union[Unset, str] = UNSET,
    filterstatuseq: Union[Unset, str] = UNSET,
    filterstatusnot_eq: Union[Unset, str] = UNSET,
    filterstatusin: Union[Unset, str] = UNSET,
    filterstatusnot_in: Union[Unset, str] = UNSET,
    filterincident_statuseq: Union[Unset, str] = UNSET,
    filterincident_statusnot_eq: Union[Unset, str] = UNSET,
    filterincident_statusin: Union[Unset, str] = UNSET,
    filterincident_statusnot_in: Union[Unset, str] = UNSET,
    sort: Union[Unset, str] = UNSET,
) -> Optional[IncidentActionItemList]:
    """List all action items for an organization

     List all action items for an organization

    Args:
        include (Union[Unset, str]):
        pagenumber (Union[Unset, int]):
        pagesize (Union[Unset, int]):
        filterkind (Union[Unset, str]):
        filterpriority (Union[Unset, str]):
        filterstatus (Union[Unset, str]):
        filterincident_status (Union[Unset, str]):
        filterincident_created_atgt (Union[Unset, str]):
        filterincident_created_atgte (Union[Unset, str]):
        filterincident_created_atlt (Union[Unset, str]):
        filterincident_created_atlte (Union[Unset, str]):
        filterdue_dategt (Union[Unset, str]):
        filterdue_dategte (Union[Unset, str]):
        filterdue_datelt (Union[Unset, str]):
        filterdue_datelte (Union[Unset, str]):
        filtercreated_atgt (Union[Unset, str]):
        filtercreated_atgte (Union[Unset, str]):
        filtercreated_atlt (Union[Unset, str]):
        filtercreated_atlte (Union[Unset, str]):
        filterkindeq (Union[Unset, str]):
        filterkindnot_eq (Union[Unset, str]):
        filterkindin (Union[Unset, str]):
        filterkindnot_in (Union[Unset, str]):
        filterpriorityeq (Union[Unset, str]):
        filterprioritynot_eq (Union[Unset, str]):
        filterpriorityin (Union[Unset, str]):
        filterprioritynot_in (Union[Unset, str]):
        filterstatuseq (Union[Unset, str]):
        filterstatusnot_eq (Union[Unset, str]):
        filterstatusin (Union[Unset, str]):
        filterstatusnot_in (Union[Unset, str]):
        filterincident_statuseq (Union[Unset, str]):
        filterincident_statusnot_eq (Union[Unset, str]):
        filterincident_statusin (Union[Unset, str]):
        filterincident_statusnot_in (Union[Unset, str]):
        sort (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        IncidentActionItemList
    """

    return sync_detailed(
        client=client,
        include=include,
        pagenumber=pagenumber,
        pagesize=pagesize,
        filterkind=filterkind,
        filterpriority=filterpriority,
        filterstatus=filterstatus,
        filterincident_status=filterincident_status,
        filterincident_created_atgt=filterincident_created_atgt,
        filterincident_created_atgte=filterincident_created_atgte,
        filterincident_created_atlt=filterincident_created_atlt,
        filterincident_created_atlte=filterincident_created_atlte,
        filterdue_dategt=filterdue_dategt,
        filterdue_dategte=filterdue_dategte,
        filterdue_datelt=filterdue_datelt,
        filterdue_datelte=filterdue_datelte,
        filtercreated_atgt=filtercreated_atgt,
        filtercreated_atgte=filtercreated_atgte,
        filtercreated_atlt=filtercreated_atlt,
        filtercreated_atlte=filtercreated_atlte,
        filterkindeq=filterkindeq,
        filterkindnot_eq=filterkindnot_eq,
        filterkindin=filterkindin,
        filterkindnot_in=filterkindnot_in,
        filterpriorityeq=filterpriorityeq,
        filterprioritynot_eq=filterprioritynot_eq,
        filterpriorityin=filterpriorityin,
        filterprioritynot_in=filterprioritynot_in,
        filterstatuseq=filterstatuseq,
        filterstatusnot_eq=filterstatusnot_eq,
        filterstatusin=filterstatusin,
        filterstatusnot_in=filterstatusnot_in,
        filterincident_statuseq=filterincident_statuseq,
        filterincident_statusnot_eq=filterincident_statusnot_eq,
        filterincident_statusin=filterincident_statusin,
        filterincident_statusnot_in=filterincident_statusnot_in,
        sort=sort,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    include: Union[Unset, str] = UNSET,
    pagenumber: Union[Unset, int] = UNSET,
    pagesize: Union[Unset, int] = UNSET,
    filterkind: Union[Unset, str] = UNSET,
    filterpriority: Union[Unset, str] = UNSET,
    filterstatus: Union[Unset, str] = UNSET,
    filterincident_status: Union[Unset, str] = UNSET,
    filterincident_created_atgt: Union[Unset, str] = UNSET,
    filterincident_created_atgte: Union[Unset, str] = UNSET,
    filterincident_created_atlt: Union[Unset, str] = UNSET,
    filterincident_created_atlte: Union[Unset, str] = UNSET,
    filterdue_dategt: Union[Unset, str] = UNSET,
    filterdue_dategte: Union[Unset, str] = UNSET,
    filterdue_datelt: Union[Unset, str] = UNSET,
    filterdue_datelte: Union[Unset, str] = UNSET,
    filtercreated_atgt: Union[Unset, str] = UNSET,
    filtercreated_atgte: Union[Unset, str] = UNSET,
    filtercreated_atlt: Union[Unset, str] = UNSET,
    filtercreated_atlte: Union[Unset, str] = UNSET,
    filterkindeq: Union[Unset, str] = UNSET,
    filterkindnot_eq: Union[Unset, str] = UNSET,
    filterkindin: Union[Unset, str] = UNSET,
    filterkindnot_in: Union[Unset, str] = UNSET,
    filterpriorityeq: Union[Unset, str] = UNSET,
    filterprioritynot_eq: Union[Unset, str] = UNSET,
    filterpriorityin: Union[Unset, str] = UNSET,
    filterprioritynot_in: Union[Unset, str] = UNSET,
    filterstatuseq: Union[Unset, str] = UNSET,
    filterstatusnot_eq: Union[Unset, str] = UNSET,
    filterstatusin: Union[Unset, str] = UNSET,
    filterstatusnot_in: Union[Unset, str] = UNSET,
    filterincident_statuseq: Union[Unset, str] = UNSET,
    filterincident_statusnot_eq: Union[Unset, str] = UNSET,
    filterincident_statusin: Union[Unset, str] = UNSET,
    filterincident_statusnot_in: Union[Unset, str] = UNSET,
    sort: Union[Unset, str] = UNSET,
) -> Response[IncidentActionItemList]:
    """List all action items for an organization

     List all action items for an organization

    Args:
        include (Union[Unset, str]):
        pagenumber (Union[Unset, int]):
        pagesize (Union[Unset, int]):
        filterkind (Union[Unset, str]):
        filterpriority (Union[Unset, str]):
        filterstatus (Union[Unset, str]):
        filterincident_status (Union[Unset, str]):
        filterincident_created_atgt (Union[Unset, str]):
        filterincident_created_atgte (Union[Unset, str]):
        filterincident_created_atlt (Union[Unset, str]):
        filterincident_created_atlte (Union[Unset, str]):
        filterdue_dategt (Union[Unset, str]):
        filterdue_dategte (Union[Unset, str]):
        filterdue_datelt (Union[Unset, str]):
        filterdue_datelte (Union[Unset, str]):
        filtercreated_atgt (Union[Unset, str]):
        filtercreated_atgte (Union[Unset, str]):
        filtercreated_atlt (Union[Unset, str]):
        filtercreated_atlte (Union[Unset, str]):
        filterkindeq (Union[Unset, str]):
        filterkindnot_eq (Union[Unset, str]):
        filterkindin (Union[Unset, str]):
        filterkindnot_in (Union[Unset, str]):
        filterpriorityeq (Union[Unset, str]):
        filterprioritynot_eq (Union[Unset, str]):
        filterpriorityin (Union[Unset, str]):
        filterprioritynot_in (Union[Unset, str]):
        filterstatuseq (Union[Unset, str]):
        filterstatusnot_eq (Union[Unset, str]):
        filterstatusin (Union[Unset, str]):
        filterstatusnot_in (Union[Unset, str]):
        filterincident_statuseq (Union[Unset, str]):
        filterincident_statusnot_eq (Union[Unset, str]):
        filterincident_statusin (Union[Unset, str]):
        filterincident_statusnot_in (Union[Unset, str]):
        sort (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[IncidentActionItemList]
    """

    kwargs = _get_kwargs(
        include=include,
        pagenumber=pagenumber,
        pagesize=pagesize,
        filterkind=filterkind,
        filterpriority=filterpriority,
        filterstatus=filterstatus,
        filterincident_status=filterincident_status,
        filterincident_created_atgt=filterincident_created_atgt,
        filterincident_created_atgte=filterincident_created_atgte,
        filterincident_created_atlt=filterincident_created_atlt,
        filterincident_created_atlte=filterincident_created_atlte,
        filterdue_dategt=filterdue_dategt,
        filterdue_dategte=filterdue_dategte,
        filterdue_datelt=filterdue_datelt,
        filterdue_datelte=filterdue_datelte,
        filtercreated_atgt=filtercreated_atgt,
        filtercreated_atgte=filtercreated_atgte,
        filtercreated_atlt=filtercreated_atlt,
        filtercreated_atlte=filtercreated_atlte,
        filterkindeq=filterkindeq,
        filterkindnot_eq=filterkindnot_eq,
        filterkindin=filterkindin,
        filterkindnot_in=filterkindnot_in,
        filterpriorityeq=filterpriorityeq,
        filterprioritynot_eq=filterprioritynot_eq,
        filterpriorityin=filterpriorityin,
        filterprioritynot_in=filterprioritynot_in,
        filterstatuseq=filterstatuseq,
        filterstatusnot_eq=filterstatusnot_eq,
        filterstatusin=filterstatusin,
        filterstatusnot_in=filterstatusnot_in,
        filterincident_statuseq=filterincident_statuseq,
        filterincident_statusnot_eq=filterincident_statusnot_eq,
        filterincident_statusin=filterincident_statusin,
        filterincident_statusnot_in=filterincident_statusnot_in,
        sort=sort,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    include: Union[Unset, str] = UNSET,
    pagenumber: Union[Unset, int] = UNSET,
    pagesize: Union[Unset, int] = UNSET,
    filterkind: Union[Unset, str] = UNSET,
    filterpriority: Union[Unset, str] = UNSET,
    filterstatus: Union[Unset, str] = UNSET,
    filterincident_status: Union[Unset, str] = UNSET,
    filterincident_created_atgt: Union[Unset, str] = UNSET,
    filterincident_created_atgte: Union[Unset, str] = UNSET,
    filterincident_created_atlt: Union[Unset, str] = UNSET,
    filterincident_created_atlte: Union[Unset, str] = UNSET,
    filterdue_dategt: Union[Unset, str] = UNSET,
    filterdue_dategte: Union[Unset, str] = UNSET,
    filterdue_datelt: Union[Unset, str] = UNSET,
    filterdue_datelte: Union[Unset, str] = UNSET,
    filtercreated_atgt: Union[Unset, str] = UNSET,
    filtercreated_atgte: Union[Unset, str] = UNSET,
    filtercreated_atlt: Union[Unset, str] = UNSET,
    filtercreated_atlte: Union[Unset, str] = UNSET,
    filterkindeq: Union[Unset, str] = UNSET,
    filterkindnot_eq: Union[Unset, str] = UNSET,
    filterkindin: Union[Unset, str] = UNSET,
    filterkindnot_in: Union[Unset, str] = UNSET,
    filterpriorityeq: Union[Unset, str] = UNSET,
    filterprioritynot_eq: Union[Unset, str] = UNSET,
    filterpriorityin: Union[Unset, str] = UNSET,
    filterprioritynot_in: Union[Unset, str] = UNSET,
    filterstatuseq: Union[Unset, str] = UNSET,
    filterstatusnot_eq: Union[Unset, str] = UNSET,
    filterstatusin: Union[Unset, str] = UNSET,
    filterstatusnot_in: Union[Unset, str] = UNSET,
    filterincident_statuseq: Union[Unset, str] = UNSET,
    filterincident_statusnot_eq: Union[Unset, str] = UNSET,
    filterincident_statusin: Union[Unset, str] = UNSET,
    filterincident_statusnot_in: Union[Unset, str] = UNSET,
    sort: Union[Unset, str] = UNSET,
) -> Optional[IncidentActionItemList]:
    """List all action items for an organization

     List all action items for an organization

    Args:
        include (Union[Unset, str]):
        pagenumber (Union[Unset, int]):
        pagesize (Union[Unset, int]):
        filterkind (Union[Unset, str]):
        filterpriority (Union[Unset, str]):
        filterstatus (Union[Unset, str]):
        filterincident_status (Union[Unset, str]):
        filterincident_created_atgt (Union[Unset, str]):
        filterincident_created_atgte (Union[Unset, str]):
        filterincident_created_atlt (Union[Unset, str]):
        filterincident_created_atlte (Union[Unset, str]):
        filterdue_dategt (Union[Unset, str]):
        filterdue_dategte (Union[Unset, str]):
        filterdue_datelt (Union[Unset, str]):
        filterdue_datelte (Union[Unset, str]):
        filtercreated_atgt (Union[Unset, str]):
        filtercreated_atgte (Union[Unset, str]):
        filtercreated_atlt (Union[Unset, str]):
        filtercreated_atlte (Union[Unset, str]):
        filterkindeq (Union[Unset, str]):
        filterkindnot_eq (Union[Unset, str]):
        filterkindin (Union[Unset, str]):
        filterkindnot_in (Union[Unset, str]):
        filterpriorityeq (Union[Unset, str]):
        filterprioritynot_eq (Union[Unset, str]):
        filterpriorityin (Union[Unset, str]):
        filterprioritynot_in (Union[Unset, str]):
        filterstatuseq (Union[Unset, str]):
        filterstatusnot_eq (Union[Unset, str]):
        filterstatusin (Union[Unset, str]):
        filterstatusnot_in (Union[Unset, str]):
        filterincident_statuseq (Union[Unset, str]):
        filterincident_statusnot_eq (Union[Unset, str]):
        filterincident_statusin (Union[Unset, str]):
        filterincident_statusnot_in (Union[Unset, str]):
        sort (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        IncidentActionItemList
    """

    return (
        await asyncio_detailed(
            client=client,
            include=include,
            pagenumber=pagenumber,
            pagesize=pagesize,
            filterkind=filterkind,
            filterpriority=filterpriority,
            filterstatus=filterstatus,
            filterincident_status=filterincident_status,
            filterincident_created_atgt=filterincident_created_atgt,
            filterincident_created_atgte=filterincident_created_atgte,
            filterincident_created_atlt=filterincident_created_atlt,
            filterincident_created_atlte=filterincident_created_atlte,
            filterdue_dategt=filterdue_dategt,
            filterdue_dategte=filterdue_dategte,
            filterdue_datelt=filterdue_datelt,
            filterdue_datelte=filterdue_datelte,
            filtercreated_atgt=filtercreated_atgt,
            filtercreated_atgte=filtercreated_atgte,
            filtercreated_atlt=filtercreated_atlt,
            filtercreated_atlte=filtercreated_atlte,
            filterkindeq=filterkindeq,
            filterkindnot_eq=filterkindnot_eq,
            filterkindin=filterkindin,
            filterkindnot_in=filterkindnot_in,
            filterpriorityeq=filterpriorityeq,
            filterprioritynot_eq=filterprioritynot_eq,
            filterpriorityin=filterpriorityin,
            filterprioritynot_in=filterprioritynot_in,
            filterstatuseq=filterstatuseq,
            filterstatusnot_eq=filterstatusnot_eq,
            filterstatusin=filterstatusin,
            filterstatusnot_in=filterstatusnot_in,
            filterincident_statuseq=filterincident_statuseq,
            filterincident_statusnot_eq=filterincident_statusnot_eq,
            filterincident_statusin=filterincident_statusin,
            filterincident_statusnot_in=filterincident_statusnot_in,
            sort=sort,
        )
    ).parsed
