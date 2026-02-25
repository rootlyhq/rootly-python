from http import HTTPStatus
from typing import Any, Optional, Union
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.errors_list import ErrorsList
from ...models.status_page_response import StatusPageResponse
from ...models.update_status_page import UpdateStatusPage
from ...types import Response


def _get_kwargs(
    id: Union[UUID, str],
    *,
    body: UpdateStatusPage,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": f"/v1/status-pages/{id}",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/vnd.api+json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorsList, StatusPageResponse]]:
    if response.status_code == 200:
        response_200 = StatusPageResponse.from_dict(response.json())

        return response_200

    if response.status_code == 404:
        response_404 = ErrorsList.from_dict(response.json())

        return response_404

    if response.status_code == 422:
        response_422 = ErrorsList.from_dict(response.json())

        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[ErrorsList, StatusPageResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: Union[UUID, str],
    *,
    client: AuthenticatedClient,
    body: UpdateStatusPage,
) -> Response[Union[ErrorsList, StatusPageResponse]]:
    """Update a status page

     Update a specific status page by id

    Args:
        id (Union[UUID, str]):
        body (UpdateStatusPage):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorsList, StatusPageResponse]]
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
    id: Union[UUID, str],
    *,
    client: AuthenticatedClient,
    body: UpdateStatusPage,
) -> Optional[Union[ErrorsList, StatusPageResponse]]:
    """Update a status page

     Update a specific status page by id

    Args:
        id (Union[UUID, str]):
        body (UpdateStatusPage):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorsList, StatusPageResponse]
    """

    return sync_detailed(
        id=id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    id: Union[UUID, str],
    *,
    client: AuthenticatedClient,
    body: UpdateStatusPage,
) -> Response[Union[ErrorsList, StatusPageResponse]]:
    """Update a status page

     Update a specific status page by id

    Args:
        id (Union[UUID, str]):
        body (UpdateStatusPage):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorsList, StatusPageResponse]]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: Union[UUID, str],
    *,
    client: AuthenticatedClient,
    body: UpdateStatusPage,
) -> Optional[Union[ErrorsList, StatusPageResponse]]:
    """Update a status page

     Update a specific status page by id

    Args:
        id (Union[UUID, str]):
        body (UpdateStatusPage):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorsList, StatusPageResponse]
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
        )
    ).parsed
