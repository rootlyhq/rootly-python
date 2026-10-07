from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.private_agent_response import PrivateAgentResponse
from ...types import Response


def _get_kwargs(
    id: UUID,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/private_agents/{id}/revoke".format(
            id=quote(str(id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | PrivateAgentResponse | None:
    if response.status_code == 200:
        response_200 = PrivateAgentResponse.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | PrivateAgentResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: UUID,
    *,
    client: AuthenticatedClient,
) -> Response[Any | PrivateAgentResponse]:
    """Revoke private agent

     Invalidate access and refresh credentials and remove provider routing registrations. Requires
    Private Agent delete permission plus the Private Agents and AI SRE features. Retains the agent and
    invocation history. Repeated revocation is safe. An executing customer-side operation is not
    guaranteed to stop immediately. Use a new enrollment token to re-enroll a revoked installation.

    Args:
        id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PrivateAgentResponse]
    """

    kwargs = _get_kwargs(
        id=id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: UUID,
    *,
    client: AuthenticatedClient,
) -> Any | PrivateAgentResponse | None:
    """Revoke private agent

     Invalidate access and refresh credentials and remove provider routing registrations. Requires
    Private Agent delete permission plus the Private Agents and AI SRE features. Retains the agent and
    invocation history. Repeated revocation is safe. An executing customer-side operation is not
    guaranteed to stop immediately. Use a new enrollment token to re-enroll a revoked installation.

    Args:
        id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PrivateAgentResponse
    """

    return sync_detailed(
        id=id,
        client=client,
    ).parsed


async def asyncio_detailed(
    id: UUID,
    *,
    client: AuthenticatedClient,
) -> Response[Any | PrivateAgentResponse]:
    """Revoke private agent

     Invalidate access and refresh credentials and remove provider routing registrations. Requires
    Private Agent delete permission plus the Private Agents and AI SRE features. Retains the agent and
    invocation history. Repeated revocation is safe. An executing customer-side operation is not
    guaranteed to stop immediately. Use a new enrollment token to re-enroll a revoked installation.

    Args:
        id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PrivateAgentResponse]
    """

    kwargs = _get_kwargs(
        id=id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: UUID,
    *,
    client: AuthenticatedClient,
) -> Any | PrivateAgentResponse | None:
    """Revoke private agent

     Invalidate access and refresh credentials and remove provider routing registrations. Requires
    Private Agent delete permission plus the Private Agents and AI SRE features. Retains the agent and
    invocation history. Repeated revocation is safe. An executing customer-side operation is not
    guaranteed to stop immediately. Use a new enrollment token to re-enroll a revoked installation.

    Args:
        id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PrivateAgentResponse
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
        )
    ).parsed
