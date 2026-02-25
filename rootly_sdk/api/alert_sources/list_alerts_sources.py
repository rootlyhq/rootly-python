from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.alerts_source_list import AlertsSourceList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    include: Union[Unset, str] = UNSET,
    pagenumber: Union[Unset, int] = UNSET,
    pagesize: Union[Unset, int] = UNSET,
    filtersearch: Union[Unset, str] = UNSET,
    filterstatuses: Union[Unset, str] = UNSET,
    filtersource_types: Union[Unset, str] = UNSET,
    filtername: Union[Unset, str] = UNSET,
    sort: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["include"] = include

    params["page[number]"] = pagenumber

    params["page[size]"] = pagesize

    params["filter[search]"] = filtersearch

    params["filter[statuses]"] = filterstatuses

    params["filter[source_types]"] = filtersource_types

    params["filter[name]"] = filtername

    params["sort"] = sort

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/alert_sources",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[AlertsSourceList]:
    if response.status_code == 200:
        response_200 = AlertsSourceList.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[AlertsSourceList]:
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
    filtersearch: Union[Unset, str] = UNSET,
    filterstatuses: Union[Unset, str] = UNSET,
    filtersource_types: Union[Unset, str] = UNSET,
    filtername: Union[Unset, str] = UNSET,
    sort: Union[Unset, str] = UNSET,
) -> Response[AlertsSourceList]:
    """List alert sources

     List alert sources

    Args:
        include (Union[Unset, str]):
        pagenumber (Union[Unset, int]):
        pagesize (Union[Unset, int]):
        filtersearch (Union[Unset, str]):
        filterstatuses (Union[Unset, str]):
        filtersource_types (Union[Unset, str]):
        filtername (Union[Unset, str]):
        sort (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AlertsSourceList]
    """

    kwargs = _get_kwargs(
        include=include,
        pagenumber=pagenumber,
        pagesize=pagesize,
        filtersearch=filtersearch,
        filterstatuses=filterstatuses,
        filtersource_types=filtersource_types,
        filtername=filtername,
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
    filtersearch: Union[Unset, str] = UNSET,
    filterstatuses: Union[Unset, str] = UNSET,
    filtersource_types: Union[Unset, str] = UNSET,
    filtername: Union[Unset, str] = UNSET,
    sort: Union[Unset, str] = UNSET,
) -> Optional[AlertsSourceList]:
    """List alert sources

     List alert sources

    Args:
        include (Union[Unset, str]):
        pagenumber (Union[Unset, int]):
        pagesize (Union[Unset, int]):
        filtersearch (Union[Unset, str]):
        filterstatuses (Union[Unset, str]):
        filtersource_types (Union[Unset, str]):
        filtername (Union[Unset, str]):
        sort (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AlertsSourceList
    """

    return sync_detailed(
        client=client,
        include=include,
        pagenumber=pagenumber,
        pagesize=pagesize,
        filtersearch=filtersearch,
        filterstatuses=filterstatuses,
        filtersource_types=filtersource_types,
        filtername=filtername,
        sort=sort,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    include: Union[Unset, str] = UNSET,
    pagenumber: Union[Unset, int] = UNSET,
    pagesize: Union[Unset, int] = UNSET,
    filtersearch: Union[Unset, str] = UNSET,
    filterstatuses: Union[Unset, str] = UNSET,
    filtersource_types: Union[Unset, str] = UNSET,
    filtername: Union[Unset, str] = UNSET,
    sort: Union[Unset, str] = UNSET,
) -> Response[AlertsSourceList]:
    """List alert sources

     List alert sources

    Args:
        include (Union[Unset, str]):
        pagenumber (Union[Unset, int]):
        pagesize (Union[Unset, int]):
        filtersearch (Union[Unset, str]):
        filterstatuses (Union[Unset, str]):
        filtersource_types (Union[Unset, str]):
        filtername (Union[Unset, str]):
        sort (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AlertsSourceList]
    """

    kwargs = _get_kwargs(
        include=include,
        pagenumber=pagenumber,
        pagesize=pagesize,
        filtersearch=filtersearch,
        filterstatuses=filterstatuses,
        filtersource_types=filtersource_types,
        filtername=filtername,
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
    filtersearch: Union[Unset, str] = UNSET,
    filterstatuses: Union[Unset, str] = UNSET,
    filtersource_types: Union[Unset, str] = UNSET,
    filtername: Union[Unset, str] = UNSET,
    sort: Union[Unset, str] = UNSET,
) -> Optional[AlertsSourceList]:
    """List alert sources

     List alert sources

    Args:
        include (Union[Unset, str]):
        pagenumber (Union[Unset, int]):
        pagesize (Union[Unset, int]):
        filtersearch (Union[Unset, str]):
        filterstatuses (Union[Unset, str]):
        filtersource_types (Union[Unset, str]):
        filtername (Union[Unset, str]):
        sort (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AlertsSourceList
    """

    return (
        await asyncio_detailed(
            client=client,
            include=include,
            pagenumber=pagenumber,
            pagesize=pagesize,
            filtersearch=filtersearch,
            filterstatuses=filterstatuses,
            filtersource_types=filtersource_types,
            filtername=filtername,
            sort=sort,
        )
    ).parsed
