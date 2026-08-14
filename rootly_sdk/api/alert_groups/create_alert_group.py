from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.alert_group_response import AlertGroupResponse
from ...models.errors_list import ErrorsList
from ...models.new_alert_group import NewAlertGroup
from ...types import Response


def _get_kwargs(
    *,
    body: NewAlertGroup,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/alert_groups",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/vnd.api+json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AlertGroupResponse | ErrorsList | None:
    if response.status_code == 201:
        response_201 = AlertGroupResponse.from_dict(response.json())

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
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[AlertGroupResponse | ErrorsList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: NewAlertGroup,
) -> Response[AlertGroupResponse | ErrorsList]:
    """Creates an alert group

     Creates a new alert group. **Note**: For enhanced functionality and future compatibility, consider
    using the advanced alert grouping with `conditions` field instead of the legacy
    `group_by_alert_title`, `group_by_alert_urgency`, and `attributes` fields.

    Args:
        body (NewAlertGroup):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[AlertGroupResponse, ErrorsList]]
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
    body: NewAlertGroup,
) -> AlertGroupResponse | ErrorsList | None:
    """Creates an alert group

     Creates a new alert group. **Note**: For enhanced functionality and future compatibility, consider
    using the advanced alert grouping with `conditions` field instead of the legacy
    `group_by_alert_title`, `group_by_alert_urgency`, and `attributes` fields.

    Args:
        body (NewAlertGroup):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[AlertGroupResponse, ErrorsList]
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: NewAlertGroup,
) -> Response[AlertGroupResponse | ErrorsList]:
    """Creates an alert group

     Creates a new alert group. **Note**: For enhanced functionality and future compatibility, consider
    using the advanced alert grouping with `conditions` field instead of the legacy
    `group_by_alert_title`, `group_by_alert_urgency`, and `attributes` fields.

    Args:
        body (NewAlertGroup):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[AlertGroupResponse, ErrorsList]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: NewAlertGroup,
) -> AlertGroupResponse | ErrorsList | None:
    """Creates an alert group

     Creates a new alert group. **Note**: For enhanced functionality and future compatibility, consider
    using the advanced alert grouping with `conditions` field instead of the legacy
    `group_by_alert_title`, `group_by_alert_urgency`, and `attributes` fields.

    Args:
        body (NewAlertGroup):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[AlertGroupResponse, ErrorsList]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
