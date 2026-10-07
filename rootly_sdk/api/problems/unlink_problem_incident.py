from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.errors_list import ErrorsList
from ...models.problem_response import ProblemResponse
from ...types import Response


def _get_kwargs(
    id: str,
    incident_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/v1/problems/{id}/incidents/{incident_id}".format(
            id=quote(str(id), safe=""),
            incident_id=quote(str(incident_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorsList | ProblemResponse | None:
    if response.status_code == 200:
        response_200 = ProblemResponse.from_dict(response.json())

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
) -> Response[ErrorsList | ProblemResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: str,
    incident_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[ErrorsList | ProblemResponse]:
    """Unlinks an incident from a problem

     Unlinks an incident from a problem

    Args:
        id (str):
        incident_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorsList | ProblemResponse]
    """

    kwargs = _get_kwargs(
        id=id,
        incident_id=incident_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    incident_id: str,
    *,
    client: AuthenticatedClient,
) -> ErrorsList | ProblemResponse | None:
    """Unlinks an incident from a problem

     Unlinks an incident from a problem

    Args:
        id (str):
        incident_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorsList | ProblemResponse
    """

    return sync_detailed(
        id=id,
        incident_id=incident_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    id: str,
    incident_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[ErrorsList | ProblemResponse]:
    """Unlinks an incident from a problem

     Unlinks an incident from a problem

    Args:
        id (str):
        incident_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorsList | ProblemResponse]
    """

    kwargs = _get_kwargs(
        id=id,
        incident_id=incident_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    incident_id: str,
    *,
    client: AuthenticatedClient,
) -> ErrorsList | ProblemResponse | None:
    """Unlinks an incident from a problem

     Unlinks an incident from a problem

    Args:
        id (str):
        incident_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorsList | ProblemResponse
    """

    return (
        await asyncio_detailed(
            id=id,
            incident_id=incident_id,
            client=client,
        )
    ).parsed
