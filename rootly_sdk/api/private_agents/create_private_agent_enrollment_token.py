from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.private_agent_enrollment_token_response import PrivateAgentEnrollmentTokenResponse
from ...types import Response


def _get_kwargs() -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/private_agents/enrollment_tokens",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | PrivateAgentEnrollmentTokenResponse | None:
    if response.status_code == 201:
        response_201 = PrivateAgentEnrollmentTokenResponse.from_dict(response.json())

        return response_201

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
) -> Response[Any | PrivateAgentEnrollmentTokenResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[Any | PrivateAgentEnrollmentTokenResponse]:
    """Create a one-time token for agent enrollment

     Issue a one-time token valid for 24 hours. No request body is required. Requires Private Agent
    management permission plus the Private Agents and AI SRE features. The agent uses this token for
    gRPC Enroll; the agent record is created on enrollment, not by this request. The plaintext is
    returned only here and is not recoverable. Repeated requests issue distinct tokens; this endpoint is
    not idempotent.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PrivateAgentEnrollmentTokenResponse]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
) -> Any | PrivateAgentEnrollmentTokenResponse | None:
    """Create a one-time token for agent enrollment

     Issue a one-time token valid for 24 hours. No request body is required. Requires Private Agent
    management permission plus the Private Agents and AI SRE features. The agent uses this token for
    gRPC Enroll; the agent record is created on enrollment, not by this request. The plaintext is
    returned only here and is not recoverable. Repeated requests issue distinct tokens; this endpoint is
    not idempotent.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PrivateAgentEnrollmentTokenResponse
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[Any | PrivateAgentEnrollmentTokenResponse]:
    """Create a one-time token for agent enrollment

     Issue a one-time token valid for 24 hours. No request body is required. Requires Private Agent
    management permission plus the Private Agents and AI SRE features. The agent uses this token for
    gRPC Enroll; the agent record is created on enrollment, not by this request. The plaintext is
    returned only here and is not recoverable. Repeated requests issue distinct tokens; this endpoint is
    not idempotent.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PrivateAgentEnrollmentTokenResponse]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
) -> Any | PrivateAgentEnrollmentTokenResponse | None:
    """Create a one-time token for agent enrollment

     Issue a one-time token valid for 24 hours. No request body is required. Requires Private Agent
    management permission plus the Private Agents and AI SRE features. The agent uses this token for
    gRPC Enroll; the agent record is created on enrollment, not by this request. The plaintext is
    returned only here and is not recoverable. Repeated requests issue distinct tokens; this endpoint is
    not idempotent.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PrivateAgentEnrollmentTokenResponse
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
