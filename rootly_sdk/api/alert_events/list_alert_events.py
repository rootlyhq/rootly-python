from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.alert_event_list import AlertEventList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    alert_id: str,
    *,
    include: str | Unset = UNSET,
    pagenumber: int | Unset = UNSET,
    pagesize: int | Unset = UNSET,
    filterkind: str | Unset = UNSET,
    filteraction: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["include"] = include

    params["page[number]"] = pagenumber

    params["page[size]"] = pagesize

    params["filter[kind]"] = filterkind

    params["filter[action]"] = filteraction

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/alerts/{alert_id}/events".format(
            alert_id=quote(str(alert_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> AlertEventList | None:
    if response.status_code == 200:
        response_200 = AlertEventList.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[AlertEventList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    alert_id: str,
    *,
    client: AuthenticatedClient,
    include: str | Unset = UNSET,
    pagenumber: int | Unset = UNSET,
    pagesize: int | Unset = UNSET,
    filterkind: str | Unset = UNSET,
    filteraction: str | Unset = UNSET,
) -> Response[AlertEventList]:
    """List alert events

     List alert_events

    Args:
        alert_id (str):
        include (str | Unset):
        pagenumber (int | Unset):
        pagesize (int | Unset):
        filterkind (str | Unset):
        filteraction (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AlertEventList]
    """

    kwargs = _get_kwargs(
        alert_id=alert_id,
        include=include,
        pagenumber=pagenumber,
        pagesize=pagesize,
        filterkind=filterkind,
        filteraction=filteraction,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    alert_id: str,
    *,
    client: AuthenticatedClient,
    include: str | Unset = UNSET,
    pagenumber: int | Unset = UNSET,
    pagesize: int | Unset = UNSET,
    filterkind: str | Unset = UNSET,
    filteraction: str | Unset = UNSET,
) -> AlertEventList | None:
    """List alert events

     List alert_events

    Args:
        alert_id (str):
        include (str | Unset):
        pagenumber (int | Unset):
        pagesize (int | Unset):
        filterkind (str | Unset):
        filteraction (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AlertEventList
    """

    return sync_detailed(
        alert_id=alert_id,
        client=client,
        include=include,
        pagenumber=pagenumber,
        pagesize=pagesize,
        filterkind=filterkind,
        filteraction=filteraction,
    ).parsed


async def asyncio_detailed(
    alert_id: str,
    *,
    client: AuthenticatedClient,
    include: str | Unset = UNSET,
    pagenumber: int | Unset = UNSET,
    pagesize: int | Unset = UNSET,
    filterkind: str | Unset = UNSET,
    filteraction: str | Unset = UNSET,
) -> Response[AlertEventList]:
    """List alert events

     List alert_events

    Args:
        alert_id (str):
        include (str | Unset):
        pagenumber (int | Unset):
        pagesize (int | Unset):
        filterkind (str | Unset):
        filteraction (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AlertEventList]
    """

    kwargs = _get_kwargs(
        alert_id=alert_id,
        include=include,
        pagenumber=pagenumber,
        pagesize=pagesize,
        filterkind=filterkind,
        filteraction=filteraction,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    alert_id: str,
    *,
    client: AuthenticatedClient,
    include: str | Unset = UNSET,
    pagenumber: int | Unset = UNSET,
    pagesize: int | Unset = UNSET,
    filterkind: str | Unset = UNSET,
    filteraction: str | Unset = UNSET,
) -> AlertEventList | None:
    """List alert events

     List alert_events

    Args:
        alert_id (str):
        include (str | Unset):
        pagenumber (int | Unset):
        pagesize (int | Unset):
        filterkind (str | Unset):
        filteraction (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AlertEventList
    """

    return (
        await asyncio_detailed(
            alert_id=alert_id,
            client=client,
            include=include,
            pagenumber=pagenumber,
            pagesize=pagesize,
            filterkind=filterkind,
            filteraction=filteraction,
        )
    ).parsed
