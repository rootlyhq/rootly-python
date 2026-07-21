from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.errors_list import ErrorsList
from ...models.escalation_policy_path_response import EscalationPolicyPathResponse
from ...models.update_escalation_policy_path import UpdateEscalationPolicyPath
from ...types import Response


def _get_kwargs(
    id: str,
    *,
    body: UpdateEscalationPolicyPath,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/v1/escalation_paths/{id}".format(
            id=quote(str(id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/vnd.api+json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorsList | EscalationPolicyPathResponse | None:
    if response.status_code == 200:
        response_200 = EscalationPolicyPathResponse.from_dict(response.json())

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
) -> Response[ErrorsList | EscalationPolicyPathResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    body: UpdateEscalationPolicyPath,
) -> Response[ErrorsList | EscalationPolicyPathResponse]:
    """Update an escalation path

     Update a specific escalation path by id

    Args:
        id (str):
        body (UpdateEscalationPolicyPath):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorsList | EscalationPolicyPathResponse]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: AuthenticatedClient,
    body: UpdateEscalationPolicyPath,
) -> ErrorsList | EscalationPolicyPathResponse | None:
    """Update an escalation path

     Update a specific escalation path by id

    Args:
        id (str):
        body (UpdateEscalationPolicyPath):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorsList | EscalationPolicyPathResponse
    """

    return sync_detailed(
        id=id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    body: UpdateEscalationPolicyPath,
) -> Response[ErrorsList | EscalationPolicyPathResponse]:
    """Update an escalation path

     Update a specific escalation path by id

    Args:
        id (str):
        body (UpdateEscalationPolicyPath):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorsList | EscalationPolicyPathResponse]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient,
    body: UpdateEscalationPolicyPath,
) -> ErrorsList | EscalationPolicyPathResponse | None:
    """Update an escalation path

     Update a specific escalation path by id

    Args:
        id (str):
        body (UpdateEscalationPolicyPath):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorsList | EscalationPolicyPathResponse
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
        )
    ).parsed
