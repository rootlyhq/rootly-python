from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.list_retrospective_configurations_include import (
    ListRetrospectiveConfigurationsInclude,
)
from ...models.retrospective_configuration_list import RetrospectiveConfigurationList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    include: Unset | ListRetrospectiveConfigurationsInclude = UNSET,
    pagenumber: Unset | int = UNSET,
    pagesize: Unset | int = UNSET,
    filterkind: Unset | str = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_include: Unset | str = UNSET
    if not isinstance(include, Unset):
        json_include = include

    params["include"] = json_include

    params["page[number]"] = pagenumber

    params["page[size]"] = pagesize

    params["filter[kind]"] = filterkind

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/retrospective_configurations",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> RetrospectiveConfigurationList | None:
    if response.status_code == 200:
        response_200 = RetrospectiveConfigurationList.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[RetrospectiveConfigurationList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    include: Unset | ListRetrospectiveConfigurationsInclude = UNSET,
    pagenumber: Unset | int = UNSET,
    pagesize: Unset | int = UNSET,
    filterkind: Unset | str = UNSET,
) -> Response[RetrospectiveConfigurationList]:
    """List retrospective configurations

     List retrospective configurations

    Args:
        include (Union[Unset, ListRetrospectiveConfigurationsInclude]):
        pagenumber (Union[Unset, int]):
        pagesize (Union[Unset, int]):
        filterkind (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RetrospectiveConfigurationList]
    """

    kwargs = _get_kwargs(
        include=include,
        pagenumber=pagenumber,
        pagesize=pagesize,
        filterkind=filterkind,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    include: Unset | ListRetrospectiveConfigurationsInclude = UNSET,
    pagenumber: Unset | int = UNSET,
    pagesize: Unset | int = UNSET,
    filterkind: Unset | str = UNSET,
) -> RetrospectiveConfigurationList | None:
    """List retrospective configurations

     List retrospective configurations

    Args:
        include (Union[Unset, ListRetrospectiveConfigurationsInclude]):
        pagenumber (Union[Unset, int]):
        pagesize (Union[Unset, int]):
        filterkind (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RetrospectiveConfigurationList
    """

    return sync_detailed(
        client=client,
        include=include,
        pagenumber=pagenumber,
        pagesize=pagesize,
        filterkind=filterkind,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    include: Unset | ListRetrospectiveConfigurationsInclude = UNSET,
    pagenumber: Unset | int = UNSET,
    pagesize: Unset | int = UNSET,
    filterkind: Unset | str = UNSET,
) -> Response[RetrospectiveConfigurationList]:
    """List retrospective configurations

     List retrospective configurations

    Args:
        include (Union[Unset, ListRetrospectiveConfigurationsInclude]):
        pagenumber (Union[Unset, int]):
        pagesize (Union[Unset, int]):
        filterkind (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RetrospectiveConfigurationList]
    """

    kwargs = _get_kwargs(
        include=include,
        pagenumber=pagenumber,
        pagesize=pagesize,
        filterkind=filterkind,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    include: Unset | ListRetrospectiveConfigurationsInclude = UNSET,
    pagenumber: Unset | int = UNSET,
    pagesize: Unset | int = UNSET,
    filterkind: Unset | str = UNSET,
) -> RetrospectiveConfigurationList | None:
    """List retrospective configurations

     List retrospective configurations

    Args:
        include (Union[Unset, ListRetrospectiveConfigurationsInclude]):
        pagenumber (Union[Unset, int]):
        pagesize (Union[Unset, int]):
        filterkind (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RetrospectiveConfigurationList
    """

    return (
        await asyncio_detailed(
            client=client,
            include=include,
            pagenumber=pagenumber,
            pagesize=pagesize,
            filterkind=filterkind,
        )
    ).parsed
