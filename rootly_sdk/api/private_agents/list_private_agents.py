from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.private_agent_list import PrivateAgentList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    pagenumber: int | Unset = UNSET,
    pagesize: int | Unset = 50,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["page[number]"] = pagenumber

    params["page[size]"] = pagesize

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/private_agents",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | PrivateAgentList | None:
    if response.status_code == 200:
        response_200 = PrivateAgentList.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | PrivateAgentList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    pagenumber: int | Unset = UNSET,
    pagesize: int | Unset = 50,
) -> Response[Any | PrivateAgentList]:
    """List private agents

     List this tenant's agents, including revoked and offline agents. Inventory pages omit provider
    snapshots to bound database and response costs; use Get private agent for provider inventory and
    last-reported health. Requires Private Agent management access plus the Private Agents and AI SRE
    features. Credentials and capability schemas are never returned.

    Args:
        pagenumber (int | Unset):
        pagesize (int | Unset):  Default: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PrivateAgentList]
    """

    kwargs = _get_kwargs(
        pagenumber=pagenumber,
        pagesize=pagesize,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    pagenumber: int | Unset = UNSET,
    pagesize: int | Unset = 50,
) -> Any | PrivateAgentList | None:
    """List private agents

     List this tenant's agents, including revoked and offline agents. Inventory pages omit provider
    snapshots to bound database and response costs; use Get private agent for provider inventory and
    last-reported health. Requires Private Agent management access plus the Private Agents and AI SRE
    features. Credentials and capability schemas are never returned.

    Args:
        pagenumber (int | Unset):
        pagesize (int | Unset):  Default: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PrivateAgentList
    """

    return sync_detailed(
        client=client,
        pagenumber=pagenumber,
        pagesize=pagesize,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    pagenumber: int | Unset = UNSET,
    pagesize: int | Unset = 50,
) -> Response[Any | PrivateAgentList]:
    """List private agents

     List this tenant's agents, including revoked and offline agents. Inventory pages omit provider
    snapshots to bound database and response costs; use Get private agent for provider inventory and
    last-reported health. Requires Private Agent management access plus the Private Agents and AI SRE
    features. Credentials and capability schemas are never returned.

    Args:
        pagenumber (int | Unset):
        pagesize (int | Unset):  Default: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PrivateAgentList]
    """

    kwargs = _get_kwargs(
        pagenumber=pagenumber,
        pagesize=pagesize,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    pagenumber: int | Unset = UNSET,
    pagesize: int | Unset = 50,
) -> Any | PrivateAgentList | None:
    """List private agents

     List this tenant's agents, including revoked and offline agents. Inventory pages omit provider
    snapshots to bound database and response costs; use Get private agent for provider inventory and
    last-reported health. Requires Private Agent management access plus the Private Agents and AI SRE
    features. Credentials and capability schemas are never returned.

    Args:
        pagenumber (int | Unset):
        pagesize (int | Unset):  Default: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PrivateAgentList
    """

    return (
        await asyncio_detailed(
            client=client,
            pagenumber=pagenumber,
            pagesize=pagesize,
        )
    ).parsed
