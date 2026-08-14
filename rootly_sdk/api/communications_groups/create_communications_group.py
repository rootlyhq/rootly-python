from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.communications_group_response import CommunicationsGroupResponse
from ...models.errors_list import ErrorsList
from ...models.new_communications_group import NewCommunicationsGroup
from ...types import Response


def _get_kwargs(
    *,
    body: NewCommunicationsGroup,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/communications/groups",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/vnd.api+json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> CommunicationsGroupResponse | ErrorsList | None:
    if response.status_code == 201:
        response_201 = CommunicationsGroupResponse.from_dict(response.json())

        return response_201

    if response.status_code == 422:
        response_422 = ErrorsList.from_dict(response.json())

        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[CommunicationsGroupResponse | ErrorsList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: NewCommunicationsGroup,
) -> Response[CommunicationsGroupResponse | ErrorsList]:
    """Creates a communications group

     Creates a new communications group from provided data

    Args:
        body (NewCommunicationsGroup):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[CommunicationsGroupResponse, ErrorsList]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: NewCommunicationsGroup,
) -> CommunicationsGroupResponse | ErrorsList | None:
    """Creates a communications group

     Creates a new communications group from provided data

    Args:
        body (NewCommunicationsGroup):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[CommunicationsGroupResponse, ErrorsList]
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: NewCommunicationsGroup,
) -> Response[CommunicationsGroupResponse | ErrorsList]:
    """Creates a communications group

     Creates a new communications group from provided data

    Args:
        body (NewCommunicationsGroup):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[CommunicationsGroupResponse, ErrorsList]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: NewCommunicationsGroup,
) -> CommunicationsGroupResponse | ErrorsList | None:
    """Creates a communications group

     Creates a new communications group from provided data

    Args:
        body (NewCommunicationsGroup):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[CommunicationsGroupResponse, ErrorsList]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
