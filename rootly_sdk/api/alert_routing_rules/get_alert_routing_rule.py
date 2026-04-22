from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.alert_routing_rule_response import AlertRoutingRuleResponse
from ...models.errors_list import ErrorsList
from ...types import Response


def _get_kwargs(
    id: str | UUID,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/alert_routing_rules/{id}".format(
            id=quote(str(id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AlertRoutingRuleResponse | ErrorsList | None:
    if response.status_code == 200:
        response_200 = AlertRoutingRuleResponse.from_dict(response.json())

        return response_200

    if response.status_code == 404:
        response_404 = ErrorsList.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[AlertRoutingRuleResponse | ErrorsList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: str | UUID,
    *,
    client: AuthenticatedClient,
) -> Response[AlertRoutingRuleResponse | ErrorsList]:
    """Retrieves an alert routing rule

     Retrieves a specific alert routing rule by id. **Note: If you are an advanced alert routing user,
    you should use the Alert Routes endpoint instead of this endpoint. If you don't know whether you are
    an advanced user, please contact Rootly customer support.**

    Args:
        id (str | UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AlertRoutingRuleResponse | ErrorsList]
    """

    kwargs = _get_kwargs(
        id=id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str | UUID,
    *,
    client: AuthenticatedClient,
) -> AlertRoutingRuleResponse | ErrorsList | None:
    """Retrieves an alert routing rule

     Retrieves a specific alert routing rule by id. **Note: If you are an advanced alert routing user,
    you should use the Alert Routes endpoint instead of this endpoint. If you don't know whether you are
    an advanced user, please contact Rootly customer support.**

    Args:
        id (str | UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AlertRoutingRuleResponse | ErrorsList
    """

    return sync_detailed(
        id=id,
        client=client,
    ).parsed


async def asyncio_detailed(
    id: str | UUID,
    *,
    client: AuthenticatedClient,
) -> Response[AlertRoutingRuleResponse | ErrorsList]:
    """Retrieves an alert routing rule

     Retrieves a specific alert routing rule by id. **Note: If you are an advanced alert routing user,
    you should use the Alert Routes endpoint instead of this endpoint. If you don't know whether you are
    an advanced user, please contact Rootly customer support.**

    Args:
        id (str | UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AlertRoutingRuleResponse | ErrorsList]
    """

    kwargs = _get_kwargs(
        id=id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str | UUID,
    *,
    client: AuthenticatedClient,
) -> AlertRoutingRuleResponse | ErrorsList | None:
    """Retrieves an alert routing rule

     Retrieves a specific alert routing rule by id. **Note: If you are an advanced alert routing user,
    you should use the Alert Routes endpoint instead of this endpoint. If you don't know whether you are
    an advanced user, please contact Rootly customer support.**

    Args:
        id (str | UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AlertRoutingRuleResponse | ErrorsList
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
        )
    ).parsed
