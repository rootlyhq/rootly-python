from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.errors_list import ErrorsList
from ...models.new_status_page_component_group import NewStatusPageComponentGroup
from ...models.status_page_component_group_response import StatusPageComponentGroupResponse
from ...types import Response


def _get_kwargs(
    status_page_id: str,
    *,
    body: NewStatusPageComponentGroup,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/v1/status-pages/{status_page_id}/component-groups",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/vnd.api+json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorsList, StatusPageComponentGroupResponse]]:
    if response.status_code == 201:
        response_201 = StatusPageComponentGroupResponse.from_dict(response.json())

        return response_201

    if response.status_code == 401:
        response_401 = ErrorsList.from_dict(response.json())

        return response_401

    if response.status_code == 422:
        response_422 = ErrorsList.from_dict(response.json())

        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[ErrorsList, StatusPageComponentGroupResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    status_page_id: str,
    *,
    client: AuthenticatedClient,
    body: NewStatusPageComponentGroup,
) -> Response[Union[ErrorsList, StatusPageComponentGroupResponse]]:
    """Creates a status page component group

     Creates a new status page component group from provided data

    Args:
        status_page_id (str):
        body (NewStatusPageComponentGroup):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorsList, StatusPageComponentGroupResponse]]
    """

    kwargs = _get_kwargs(
        status_page_id=status_page_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    status_page_id: str,
    *,
    client: AuthenticatedClient,
    body: NewStatusPageComponentGroup,
) -> Optional[Union[ErrorsList, StatusPageComponentGroupResponse]]:
    """Creates a status page component group

     Creates a new status page component group from provided data

    Args:
        status_page_id (str):
        body (NewStatusPageComponentGroup):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorsList, StatusPageComponentGroupResponse]
    """

    return sync_detailed(
        status_page_id=status_page_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    status_page_id: str,
    *,
    client: AuthenticatedClient,
    body: NewStatusPageComponentGroup,
) -> Response[Union[ErrorsList, StatusPageComponentGroupResponse]]:
    """Creates a status page component group

     Creates a new status page component group from provided data

    Args:
        status_page_id (str):
        body (NewStatusPageComponentGroup):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorsList, StatusPageComponentGroupResponse]]
    """

    kwargs = _get_kwargs(
        status_page_id=status_page_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    status_page_id: str,
    *,
    client: AuthenticatedClient,
    body: NewStatusPageComponentGroup,
) -> Optional[Union[ErrorsList, StatusPageComponentGroupResponse]]:
    """Creates a status page component group

     Creates a new status page component group from provided data

    Args:
        status_page_id (str):
        body (NewStatusPageComponentGroup):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorsList, StatusPageComponentGroupResponse]
    """

    return (
        await asyncio_detailed(
            status_page_id=status_page_id,
            client=client,
            body=body,
        )
    ).parsed
