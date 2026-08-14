from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.retrospective_process_group_response import RetrospectiveProcessGroupResponse
from ...models.update_retrospective_process_group import UpdateRetrospectiveProcessGroup
from ...types import Response


def _get_kwargs(
    id: str,
    *,
    body: UpdateRetrospectiveProcessGroup,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": f"/v1/retrospective_process_groups/{id}",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/vnd.api+json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> RetrospectiveProcessGroupResponse | None:
    if response.status_code == 200:
        response_200 = RetrospectiveProcessGroupResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[RetrospectiveProcessGroupResponse]:
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
    body: UpdateRetrospectiveProcessGroup,
) -> Response[RetrospectiveProcessGroupResponse]:
    """Update a Retrospective Process Group

     Update a specific Retrospective Process Group by id

    Args:
        id (str):
        body (UpdateRetrospectiveProcessGroup):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RetrospectiveProcessGroupResponse]
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
    body: UpdateRetrospectiveProcessGroup,
) -> RetrospectiveProcessGroupResponse | None:
    """Update a Retrospective Process Group

     Update a specific Retrospective Process Group by id

    Args:
        id (str):
        body (UpdateRetrospectiveProcessGroup):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RetrospectiveProcessGroupResponse
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
    body: UpdateRetrospectiveProcessGroup,
) -> Response[RetrospectiveProcessGroupResponse]:
    """Update a Retrospective Process Group

     Update a specific Retrospective Process Group by id

    Args:
        id (str):
        body (UpdateRetrospectiveProcessGroup):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RetrospectiveProcessGroupResponse]
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
    body: UpdateRetrospectiveProcessGroup,
) -> RetrospectiveProcessGroupResponse | None:
    """Update a Retrospective Process Group

     Update a specific Retrospective Process Group by id

    Args:
        id (str):
        body (UpdateRetrospectiveProcessGroup):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RetrospectiveProcessGroupResponse
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
        )
    ).parsed
