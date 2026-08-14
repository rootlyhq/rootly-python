from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.errors_list import ErrorsList
from ...models.new_retrospective_process_group import NewRetrospectiveProcessGroup
from ...models.retrospective_process_group_response import RetrospectiveProcessGroupResponse
from ...types import Response


def _get_kwargs(
    retrospective_process_id: str,
    *,
    body: NewRetrospectiveProcessGroup,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/v1/retrospective_processes/{retrospective_process_id}/groups",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/vnd.api+json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorsList | RetrospectiveProcessGroupResponse | None:
    if response.status_code == 201:
        response_201 = RetrospectiveProcessGroupResponse.from_dict(response.json())

        return response_201

    if response.status_code == 401:
        response_401 = ErrorsList.from_dict(response.json())

        return response_401

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ErrorsList | RetrospectiveProcessGroupResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    retrospective_process_id: str,
    *,
    client: AuthenticatedClient,
    body: NewRetrospectiveProcessGroup,
) -> Response[ErrorsList | RetrospectiveProcessGroupResponse]:
    """Creates a retrospective process group

     Creates a new retrospective process group from provided data

    Args:
        retrospective_process_id (str):
        body (NewRetrospectiveProcessGroup):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorsList, RetrospectiveProcessGroupResponse]]
    """

    kwargs = _get_kwargs(
        retrospective_process_id=retrospective_process_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    retrospective_process_id: str,
    *,
    client: AuthenticatedClient,
    body: NewRetrospectiveProcessGroup,
) -> ErrorsList | RetrospectiveProcessGroupResponse | None:
    """Creates a retrospective process group

     Creates a new retrospective process group from provided data

    Args:
        retrospective_process_id (str):
        body (NewRetrospectiveProcessGroup):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorsList, RetrospectiveProcessGroupResponse]
    """

    return sync_detailed(
        retrospective_process_id=retrospective_process_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    retrospective_process_id: str,
    *,
    client: AuthenticatedClient,
    body: NewRetrospectiveProcessGroup,
) -> Response[ErrorsList | RetrospectiveProcessGroupResponse]:
    """Creates a retrospective process group

     Creates a new retrospective process group from provided data

    Args:
        retrospective_process_id (str):
        body (NewRetrospectiveProcessGroup):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorsList, RetrospectiveProcessGroupResponse]]
    """

    kwargs = _get_kwargs(
        retrospective_process_id=retrospective_process_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    retrospective_process_id: str,
    *,
    client: AuthenticatedClient,
    body: NewRetrospectiveProcessGroup,
) -> ErrorsList | RetrospectiveProcessGroupResponse | None:
    """Creates a retrospective process group

     Creates a new retrospective process group from provided data

    Args:
        retrospective_process_id (str):
        body (NewRetrospectiveProcessGroup):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorsList, RetrospectiveProcessGroupResponse]
    """

    return (
        await asyncio_detailed(
            retrospective_process_id=retrospective_process_id,
            client=client,
            body=body,
        )
    ).parsed
