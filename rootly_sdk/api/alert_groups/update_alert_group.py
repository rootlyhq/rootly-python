from http import HTTPStatus
from typing import Any, Optional, Union
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.alert_group_response import AlertGroupResponse
from ...models.errors_list import ErrorsList
from ...models.update_alert_group import UpdateAlertGroup
from ...types import Response


def _get_kwargs(
    id: Union[UUID, str],
    *,
    body: UpdateAlertGroup,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": f"/v1/alert_groups/{id}",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/vnd.api+json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[AlertGroupResponse, ErrorsList]]:
    if response.status_code == 200:
        response_200 = AlertGroupResponse.from_dict(response.json())

        return response_200

    if response.status_code == 404:
        response_404 = ErrorsList.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[AlertGroupResponse, ErrorsList]]:
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
    body: UpdateAlertGroup,
) -> Response[Union[AlertGroupResponse, ErrorsList]]:
    """Update an alert group

     Update a specific alert group by id. **Note**: For enhanced functionality and future compatibility,
    consider using the advanced alert grouping with `conditions` field instead of the legacy
    `group_by_alert_title`, `group_by_alert_urgency`, and `attributes` fields.

    Args:
        id (Union[UUID, str]):
        body (UpdateAlertGroup):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[AlertGroupResponse, ErrorsList]]
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
    body: UpdateAlertGroup,
) -> Optional[Union[AlertGroupResponse, ErrorsList]]:
    """Update an alert group

     Update a specific alert group by id. **Note**: For enhanced functionality and future compatibility,
    consider using the advanced alert grouping with `conditions` field instead of the legacy
    `group_by_alert_title`, `group_by_alert_urgency`, and `attributes` fields.

    Args:
        id (Union[UUID, str]):
        body (UpdateAlertGroup):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[AlertGroupResponse, ErrorsList]
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
    body: UpdateAlertGroup,
) -> Response[Union[AlertGroupResponse, ErrorsList]]:
    """Update an alert group

     Update a specific alert group by id. **Note**: For enhanced functionality and future compatibility,
    consider using the advanced alert grouping with `conditions` field instead of the legacy
    `group_by_alert_title`, `group_by_alert_urgency`, and `attributes` fields.

    Args:
        id (Union[UUID, str]):
        body (UpdateAlertGroup):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[AlertGroupResponse, ErrorsList]]
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
    body: UpdateAlertGroup,
) -> Optional[Union[AlertGroupResponse, ErrorsList]]:
    """Update an alert group

     Update a specific alert group by id. **Note**: For enhanced functionality and future compatibility,
    consider using the advanced alert grouping with `conditions` field instead of the legacy
    `group_by_alert_title`, `group_by_alert_urgency`, and `attributes` fields.

    Args:
        id (Union[UUID, str]):
        body (UpdateAlertGroup):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[AlertGroupResponse, ErrorsList]
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
        )
    ).parsed
