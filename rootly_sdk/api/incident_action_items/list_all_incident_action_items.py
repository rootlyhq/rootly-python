from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.incident_action_item_list import IncidentActionItemList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    include: str | Unset = UNSET,
    pagenumber: int | Unset = UNSET,
    pagesize: int | Unset = UNSET,
    filterkind: str | Unset = UNSET,
    filterpriority: str | Unset = UNSET,
    filterstatus: str | Unset = UNSET,
    filterincident_status: str | Unset = UNSET,
    filterincident_created_atgt: str | Unset = UNSET,
    filterincident_created_atgte: str | Unset = UNSET,
    filterincident_created_atlt: str | Unset = UNSET,
    filterincident_created_atlte: str | Unset = UNSET,
    filterdue_dategt: str | Unset = UNSET,
    filterdue_dategte: str | Unset = UNSET,
    filterdue_datelt: str | Unset = UNSET,
    filterdue_datelte: str | Unset = UNSET,
    filtercreated_atgt: str | Unset = UNSET,
    filtercreated_atgte: str | Unset = UNSET,
    filtercreated_atlt: str | Unset = UNSET,
    filtercreated_atlte: str | Unset = UNSET,
    sort: str | Unset = UNSET,
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

    params["sort"] = sort

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/action_items",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> IncidentActionItemList | None:
    if response.status_code == 200:
        response_200 = IncidentActionItemList.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
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
    include: str | Unset = UNSET,
    pagenumber: int | Unset = UNSET,
    pagesize: int | Unset = UNSET,
    filterkind: str | Unset = UNSET,
    filterpriority: str | Unset = UNSET,
    filterstatus: str | Unset = UNSET,
    filterincident_status: str | Unset = UNSET,
    filterincident_created_atgt: str | Unset = UNSET,
    filterincident_created_atgte: str | Unset = UNSET,
    filterincident_created_atlt: str | Unset = UNSET,
    filterincident_created_atlte: str | Unset = UNSET,
    filterdue_dategt: str | Unset = UNSET,
    filterdue_dategte: str | Unset = UNSET,
    filterdue_datelt: str | Unset = UNSET,
    filterdue_datelte: str | Unset = UNSET,
    filtercreated_atgt: str | Unset = UNSET,
    filtercreated_atgte: str | Unset = UNSET,
    filtercreated_atlt: str | Unset = UNSET,
    filtercreated_atlte: str | Unset = UNSET,
    sort: str | Unset = UNSET,
) -> Response[IncidentActionItemList]:
    """List all action items for an organization

     List all action items for an organization

    Args:
        include (str | Unset):
        pagenumber (int | Unset):
        pagesize (int | Unset):
        filterkind (str | Unset):
        filterpriority (str | Unset):
        filterstatus (str | Unset):
        filterincident_status (str | Unset):
        filterincident_created_atgt (str | Unset):
        filterincident_created_atgte (str | Unset):
        filterincident_created_atlt (str | Unset):
        filterincident_created_atlte (str | Unset):
        filterdue_dategt (str | Unset):
        filterdue_dategte (str | Unset):
        filterdue_datelt (str | Unset):
        filterdue_datelte (str | Unset):
        filtercreated_atgt (str | Unset):
        filtercreated_atgte (str | Unset):
        filtercreated_atlt (str | Unset):
        filtercreated_atlte (str | Unset):
        sort (str | Unset):

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
        sort=sort,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    include: str | Unset = UNSET,
    pagenumber: int | Unset = UNSET,
    pagesize: int | Unset = UNSET,
    filterkind: str | Unset = UNSET,
    filterpriority: str | Unset = UNSET,
    filterstatus: str | Unset = UNSET,
    filterincident_status: str | Unset = UNSET,
    filterincident_created_atgt: str | Unset = UNSET,
    filterincident_created_atgte: str | Unset = UNSET,
    filterincident_created_atlt: str | Unset = UNSET,
    filterincident_created_atlte: str | Unset = UNSET,
    filterdue_dategt: str | Unset = UNSET,
    filterdue_dategte: str | Unset = UNSET,
    filterdue_datelt: str | Unset = UNSET,
    filterdue_datelte: str | Unset = UNSET,
    filtercreated_atgt: str | Unset = UNSET,
    filtercreated_atgte: str | Unset = UNSET,
    filtercreated_atlt: str | Unset = UNSET,
    filtercreated_atlte: str | Unset = UNSET,
    sort: str | Unset = UNSET,
) -> IncidentActionItemList | None:
    """List all action items for an organization

     List all action items for an organization

    Args:
        include (str | Unset):
        pagenumber (int | Unset):
        pagesize (int | Unset):
        filterkind (str | Unset):
        filterpriority (str | Unset):
        filterstatus (str | Unset):
        filterincident_status (str | Unset):
        filterincident_created_atgt (str | Unset):
        filterincident_created_atgte (str | Unset):
        filterincident_created_atlt (str | Unset):
        filterincident_created_atlte (str | Unset):
        filterdue_dategt (str | Unset):
        filterdue_dategte (str | Unset):
        filterdue_datelt (str | Unset):
        filterdue_datelte (str | Unset):
        filtercreated_atgt (str | Unset):
        filtercreated_atgte (str | Unset):
        filtercreated_atlt (str | Unset):
        filtercreated_atlte (str | Unset):
        sort (str | Unset):

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
        sort=sort,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    include: str | Unset = UNSET,
    pagenumber: int | Unset = UNSET,
    pagesize: int | Unset = UNSET,
    filterkind: str | Unset = UNSET,
    filterpriority: str | Unset = UNSET,
    filterstatus: str | Unset = UNSET,
    filterincident_status: str | Unset = UNSET,
    filterincident_created_atgt: str | Unset = UNSET,
    filterincident_created_atgte: str | Unset = UNSET,
    filterincident_created_atlt: str | Unset = UNSET,
    filterincident_created_atlte: str | Unset = UNSET,
    filterdue_dategt: str | Unset = UNSET,
    filterdue_dategte: str | Unset = UNSET,
    filterdue_datelt: str | Unset = UNSET,
    filterdue_datelte: str | Unset = UNSET,
    filtercreated_atgt: str | Unset = UNSET,
    filtercreated_atgte: str | Unset = UNSET,
    filtercreated_atlt: str | Unset = UNSET,
    filtercreated_atlte: str | Unset = UNSET,
    sort: str | Unset = UNSET,
) -> Response[IncidentActionItemList]:
    """List all action items for an organization

     List all action items for an organization

    Args:
        include (str | Unset):
        pagenumber (int | Unset):
        pagesize (int | Unset):
        filterkind (str | Unset):
        filterpriority (str | Unset):
        filterstatus (str | Unset):
        filterincident_status (str | Unset):
        filterincident_created_atgt (str | Unset):
        filterincident_created_atgte (str | Unset):
        filterincident_created_atlt (str | Unset):
        filterincident_created_atlte (str | Unset):
        filterdue_dategt (str | Unset):
        filterdue_dategte (str | Unset):
        filterdue_datelt (str | Unset):
        filterdue_datelte (str | Unset):
        filtercreated_atgt (str | Unset):
        filtercreated_atgte (str | Unset):
        filtercreated_atlt (str | Unset):
        filtercreated_atlte (str | Unset):
        sort (str | Unset):

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
        sort=sort,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    include: str | Unset = UNSET,
    pagenumber: int | Unset = UNSET,
    pagesize: int | Unset = UNSET,
    filterkind: str | Unset = UNSET,
    filterpriority: str | Unset = UNSET,
    filterstatus: str | Unset = UNSET,
    filterincident_status: str | Unset = UNSET,
    filterincident_created_atgt: str | Unset = UNSET,
    filterincident_created_atgte: str | Unset = UNSET,
    filterincident_created_atlt: str | Unset = UNSET,
    filterincident_created_atlte: str | Unset = UNSET,
    filterdue_dategt: str | Unset = UNSET,
    filterdue_dategte: str | Unset = UNSET,
    filterdue_datelt: str | Unset = UNSET,
    filterdue_datelte: str | Unset = UNSET,
    filtercreated_atgt: str | Unset = UNSET,
    filtercreated_atgte: str | Unset = UNSET,
    filtercreated_atlt: str | Unset = UNSET,
    filtercreated_atlte: str | Unset = UNSET,
    sort: str | Unset = UNSET,
) -> IncidentActionItemList | None:
    """List all action items for an organization

     List all action items for an organization

    Args:
        include (str | Unset):
        pagenumber (int | Unset):
        pagesize (int | Unset):
        filterkind (str | Unset):
        filterpriority (str | Unset):
        filterstatus (str | Unset):
        filterincident_status (str | Unset):
        filterincident_created_atgt (str | Unset):
        filterincident_created_atgte (str | Unset):
        filterincident_created_atlt (str | Unset):
        filterincident_created_atlte (str | Unset):
        filterdue_dategt (str | Unset):
        filterdue_dategte (str | Unset):
        filterdue_datelt (str | Unset):
        filterdue_datelte (str | Unset):
        filtercreated_atgt (str | Unset):
        filtercreated_atgte (str | Unset):
        filtercreated_atlt (str | Unset):
        filtercreated_atlte (str | Unset):
        sort (str | Unset):

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
            sort=sort,
        )
    ).parsed
