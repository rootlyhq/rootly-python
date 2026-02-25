from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.incident_action_item_list import IncidentActionItemList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    include: Unset | str = UNSET,
    pagenumber: Unset | int = UNSET,
    pagesize: Unset | int = UNSET,
    filterkind: Unset | str = UNSET,
    filterpriority: Unset | str = UNSET,
    filterstatus: Unset | str = UNSET,
    filterincident_status: Unset | str = UNSET,
    filterincident_created_atgt: Unset | str = UNSET,
    filterincident_created_atgte: Unset | str = UNSET,
    filterincident_created_atlt: Unset | str = UNSET,
    filterincident_created_atlte: Unset | str = UNSET,
    filterdue_dategt: Unset | str = UNSET,
    filterdue_dategte: Unset | str = UNSET,
    filterdue_datelt: Unset | str = UNSET,
    filterdue_datelte: Unset | str = UNSET,
    filtercreated_atgt: Unset | str = UNSET,
    filtercreated_atgte: Unset | str = UNSET,
    filtercreated_atlt: Unset | str = UNSET,
    filtercreated_atlte: Unset | str = UNSET,
    sort: Unset | str = UNSET,
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
    include: Unset | str = UNSET,
    pagenumber: Unset | int = UNSET,
    pagesize: Unset | int = UNSET,
    filterkind: Unset | str = UNSET,
    filterpriority: Unset | str = UNSET,
    filterstatus: Unset | str = UNSET,
    filterincident_status: Unset | str = UNSET,
    filterincident_created_atgt: Unset | str = UNSET,
    filterincident_created_atgte: Unset | str = UNSET,
    filterincident_created_atlt: Unset | str = UNSET,
    filterincident_created_atlte: Unset | str = UNSET,
    filterdue_dategt: Unset | str = UNSET,
    filterdue_dategte: Unset | str = UNSET,
    filterdue_datelt: Unset | str = UNSET,
    filterdue_datelte: Unset | str = UNSET,
    filtercreated_atgt: Unset | str = UNSET,
    filtercreated_atgte: Unset | str = UNSET,
    filtercreated_atlt: Unset | str = UNSET,
    filtercreated_atlte: Unset | str = UNSET,
    sort: Unset | str = UNSET,
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
        sort=sort,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    include: Unset | str = UNSET,
    pagenumber: Unset | int = UNSET,
    pagesize: Unset | int = UNSET,
    filterkind: Unset | str = UNSET,
    filterpriority: Unset | str = UNSET,
    filterstatus: Unset | str = UNSET,
    filterincident_status: Unset | str = UNSET,
    filterincident_created_atgt: Unset | str = UNSET,
    filterincident_created_atgte: Unset | str = UNSET,
    filterincident_created_atlt: Unset | str = UNSET,
    filterincident_created_atlte: Unset | str = UNSET,
    filterdue_dategt: Unset | str = UNSET,
    filterdue_dategte: Unset | str = UNSET,
    filterdue_datelt: Unset | str = UNSET,
    filterdue_datelte: Unset | str = UNSET,
    filtercreated_atgt: Unset | str = UNSET,
    filtercreated_atgte: Unset | str = UNSET,
    filtercreated_atlt: Unset | str = UNSET,
    filtercreated_atlte: Unset | str = UNSET,
    sort: Unset | str = UNSET,
) -> IncidentActionItemList | None:
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
        sort=sort,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    include: Unset | str = UNSET,
    pagenumber: Unset | int = UNSET,
    pagesize: Unset | int = UNSET,
    filterkind: Unset | str = UNSET,
    filterpriority: Unset | str = UNSET,
    filterstatus: Unset | str = UNSET,
    filterincident_status: Unset | str = UNSET,
    filterincident_created_atgt: Unset | str = UNSET,
    filterincident_created_atgte: Unset | str = UNSET,
    filterincident_created_atlt: Unset | str = UNSET,
    filterincident_created_atlte: Unset | str = UNSET,
    filterdue_dategt: Unset | str = UNSET,
    filterdue_dategte: Unset | str = UNSET,
    filterdue_datelt: Unset | str = UNSET,
    filterdue_datelte: Unset | str = UNSET,
    filtercreated_atgt: Unset | str = UNSET,
    filtercreated_atgte: Unset | str = UNSET,
    filtercreated_atlt: Unset | str = UNSET,
    filtercreated_atlte: Unset | str = UNSET,
    sort: Unset | str = UNSET,
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
        sort=sort,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    include: Unset | str = UNSET,
    pagenumber: Unset | int = UNSET,
    pagesize: Unset | int = UNSET,
    filterkind: Unset | str = UNSET,
    filterpriority: Unset | str = UNSET,
    filterstatus: Unset | str = UNSET,
    filterincident_status: Unset | str = UNSET,
    filterincident_created_atgt: Unset | str = UNSET,
    filterincident_created_atgte: Unset | str = UNSET,
    filterincident_created_atlt: Unset | str = UNSET,
    filterincident_created_atlte: Unset | str = UNSET,
    filterdue_dategt: Unset | str = UNSET,
    filterdue_dategte: Unset | str = UNSET,
    filterdue_datelt: Unset | str = UNSET,
    filterdue_datelte: Unset | str = UNSET,
    filtercreated_atgt: Unset | str = UNSET,
    filtercreated_atgte: Unset | str = UNSET,
    filtercreated_atlt: Unset | str = UNSET,
    filtercreated_atlte: Unset | str = UNSET,
    sort: Unset | str = UNSET,
) -> IncidentActionItemList | None:
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
            sort=sort,
        )
    ).parsed
