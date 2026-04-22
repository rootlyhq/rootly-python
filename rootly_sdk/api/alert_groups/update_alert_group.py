from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.alert_group_response import AlertGroupResponse
from ...models.errors_list import ErrorsList
from ...models.update_alert_group import UpdateAlertGroup
from ...types import Response


def _get_kwargs(
    id: str | UUID,
    *,
    body: UpdateAlertGroup,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/v1/alert_groups/{id}".format(
            id=quote(str(id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/vnd.api+json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AlertGroupResponse | ErrorsList | None:
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
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[AlertGroupResponse | ErrorsList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: str | UUID,
    *,
    client: AuthenticatedClient,
    body: UpdateAlertGroup,
) -> Response[AlertGroupResponse | ErrorsList]:
    """Update an alert group

     Update a specific alert group by id. **Note**: For enhanced functionality and future compatibility,
    consider using the advanced alert grouping with `conditions` field instead of the legacy
    `group_by_alert_title`, `group_by_alert_urgency`, and `attributes` fields.

    Args:
        id (str | UUID):
        body (UpdateAlertGroup):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AlertGroupResponse | ErrorsList]
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
    id: str | UUID,
    *,
    client: AuthenticatedClient,
    body: UpdateAlertGroup,
) -> AlertGroupResponse | ErrorsList | None:
    """Update an alert group

     Update a specific alert group by id. **Note**: For enhanced functionality and future compatibility,
    consider using the advanced alert grouping with `conditions` field instead of the legacy
    `group_by_alert_title`, `group_by_alert_urgency`, and `attributes` fields.

    Args:
        id (str | UUID):
        body (UpdateAlertGroup):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AlertGroupResponse | ErrorsList
    """

    return sync_detailed(
        id=id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    id: str | UUID,
    *,
    client: AuthenticatedClient,
    body: UpdateAlertGroup,
) -> Response[AlertGroupResponse | ErrorsList]:
    """Update an alert group

     Update a specific alert group by id. **Note**: For enhanced functionality and future compatibility,
    consider using the advanced alert grouping with `conditions` field instead of the legacy
    `group_by_alert_title`, `group_by_alert_urgency`, and `attributes` fields.

    Args:
        id (str | UUID):
        body (UpdateAlertGroup):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AlertGroupResponse | ErrorsList]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str | UUID,
    *,
    client: AuthenticatedClient,
    body: UpdateAlertGroup,
) -> AlertGroupResponse | ErrorsList | None:
    """Update an alert group

     Update a specific alert group by id. **Note**: For enhanced functionality and future compatibility,
    consider using the advanced alert grouping with `conditions` field instead of the legacy
    `group_by_alert_title`, `group_by_alert_urgency`, and `attributes` fields.

    Args:
        id (str | UUID):
        body (UpdateAlertGroup):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AlertGroupResponse | ErrorsList
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
        )
    ).parsed
