from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.alert_route_response import AlertRouteResponse
from ...models.errors_list import ErrorsList
from ...models.new_alert_route import NewAlertRoute
from ...types import Response


def _get_kwargs(
    *,
    body: NewAlertRoute,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/alert_routes",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/vnd.api+json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[AlertRouteResponse, ErrorsList]]:
    if response.status_code == 201:
        response_201 = AlertRouteResponse.from_dict(response.json())

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
) -> Response[Union[AlertRouteResponse, ErrorsList]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: NewAlertRoute,
) -> Response[Union[AlertRouteResponse, ErrorsList]]:
    """Creates an alert route

     Creates a new alert route from provided data. **Note: This endpoint requires access to Advanced
    Alert Routing. If you're unsure whether you have access to this feature, please contact Rootly
    customer support.**

    ## Asynchronous Rule Creation

    For organizations with large numbers of routing rules, Rootly supports asynchronous rule processing
    to improve performance. When enabled, rule creation happens in the background.

    **Important**: When async processing is enabled, the rules list in the API response will not be up-
    to-date immediately after creation. You should refetch the alert route after a few minutes to get
    the updated rules.

    If you experience slow operations when managing alert routes with many rules, contact Rootly
    customer support to enable asynchronous rule processing for your organization.

    Args:
        body (NewAlertRoute):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[AlertRouteResponse, ErrorsList]]
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
    body: NewAlertRoute,
) -> Optional[Union[AlertRouteResponse, ErrorsList]]:
    """Creates an alert route

     Creates a new alert route from provided data. **Note: This endpoint requires access to Advanced
    Alert Routing. If you're unsure whether you have access to this feature, please contact Rootly
    customer support.**

    ## Asynchronous Rule Creation

    For organizations with large numbers of routing rules, Rootly supports asynchronous rule processing
    to improve performance. When enabled, rule creation happens in the background.

    **Important**: When async processing is enabled, the rules list in the API response will not be up-
    to-date immediately after creation. You should refetch the alert route after a few minutes to get
    the updated rules.

    If you experience slow operations when managing alert routes with many rules, contact Rootly
    customer support to enable asynchronous rule processing for your organization.

    Args:
        body (NewAlertRoute):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[AlertRouteResponse, ErrorsList]
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: NewAlertRoute,
) -> Response[Union[AlertRouteResponse, ErrorsList]]:
    """Creates an alert route

     Creates a new alert route from provided data. **Note: This endpoint requires access to Advanced
    Alert Routing. If you're unsure whether you have access to this feature, please contact Rootly
    customer support.**

    ## Asynchronous Rule Creation

    For organizations with large numbers of routing rules, Rootly supports asynchronous rule processing
    to improve performance. When enabled, rule creation happens in the background.

    **Important**: When async processing is enabled, the rules list in the API response will not be up-
    to-date immediately after creation. You should refetch the alert route after a few minutes to get
    the updated rules.

    If you experience slow operations when managing alert routes with many rules, contact Rootly
    customer support to enable asynchronous rule processing for your organization.

    Args:
        body (NewAlertRoute):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[AlertRouteResponse, ErrorsList]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: NewAlertRoute,
) -> Optional[Union[AlertRouteResponse, ErrorsList]]:
    """Creates an alert route

     Creates a new alert route from provided data. **Note: This endpoint requires access to Advanced
    Alert Routing. If you're unsure whether you have access to this feature, please contact Rootly
    customer support.**

    ## Asynchronous Rule Creation

    For organizations with large numbers of routing rules, Rootly supports asynchronous rule processing
    to improve performance. When enabled, rule creation happens in the background.

    **Important**: When async processing is enabled, the rules list in the API response will not be up-
    to-date immediately after creation. You should refetch the alert route after a few minutes to get
    the updated rules.

    If you experience slow operations when managing alert routes with many rules, contact Rootly
    customer support to enable asynchronous rule processing for your organization.

    Args:
        body (NewAlertRoute):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[AlertRouteResponse, ErrorsList]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
