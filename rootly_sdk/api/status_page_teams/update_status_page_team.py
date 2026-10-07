from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.errors_list import ErrorsList
from ...models.status_page_team_response import StatusPageTeamResponse
from ...models.update_status_page_team import UpdateStatusPageTeam
from ...types import Response


def _get_kwargs(
    status_page_id: str,
    id: str,
    *,
    body: UpdateStatusPageTeam,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/v1/status-pages/{status_page_id}/teams/{id}".format(
            status_page_id=quote(str(status_page_id), safe=""),
            id=quote(str(id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/vnd.api+json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorsList | StatusPageTeamResponse | None:
    if response.status_code == 200:
        response_200 = StatusPageTeamResponse.from_dict(response.json())

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
) -> Response[ErrorsList | StatusPageTeamResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    status_page_id: str,
    id: str,
    *,
    client: AuthenticatedClient,
    body: UpdateStatusPageTeam,
) -> Response[ErrorsList | StatusPageTeamResponse]:
    """Updates a status page team assignment

     Changes the permission level of a team on a status page. Requires an owner or admin role. To move
    the grant to another team, delete it and create a new one.

    Args:
        status_page_id (str):
        id (str):
        body (UpdateStatusPageTeam):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorsList | StatusPageTeamResponse]
    """

    kwargs = _get_kwargs(
        status_page_id=status_page_id,
        id=id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    status_page_id: str,
    id: str,
    *,
    client: AuthenticatedClient,
    body: UpdateStatusPageTeam,
) -> ErrorsList | StatusPageTeamResponse | None:
    """Updates a status page team assignment

     Changes the permission level of a team on a status page. Requires an owner or admin role. To move
    the grant to another team, delete it and create a new one.

    Args:
        status_page_id (str):
        id (str):
        body (UpdateStatusPageTeam):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorsList | StatusPageTeamResponse
    """

    return sync_detailed(
        status_page_id=status_page_id,
        id=id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    status_page_id: str,
    id: str,
    *,
    client: AuthenticatedClient,
    body: UpdateStatusPageTeam,
) -> Response[ErrorsList | StatusPageTeamResponse]:
    """Updates a status page team assignment

     Changes the permission level of a team on a status page. Requires an owner or admin role. To move
    the grant to another team, delete it and create a new one.

    Args:
        status_page_id (str):
        id (str):
        body (UpdateStatusPageTeam):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorsList | StatusPageTeamResponse]
    """

    kwargs = _get_kwargs(
        status_page_id=status_page_id,
        id=id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    status_page_id: str,
    id: str,
    *,
    client: AuthenticatedClient,
    body: UpdateStatusPageTeam,
) -> ErrorsList | StatusPageTeamResponse | None:
    """Updates a status page team assignment

     Changes the permission level of a team on a status page. Requires an owner or admin role. To move
    the grant to another team, delete it and create a new one.

    Args:
        status_page_id (str):
        id (str):
        body (UpdateStatusPageTeam):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorsList | StatusPageTeamResponse
    """

    return (
        await asyncio_detailed(
            status_page_id=status_page_id,
            id=id,
            client=client,
            body=body,
        )
    ).parsed
