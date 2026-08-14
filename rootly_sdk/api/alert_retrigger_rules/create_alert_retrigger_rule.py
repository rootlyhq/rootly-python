from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.alert_retrigger_rule_response import AlertRetriggerRuleResponse
from ...models.errors_list import ErrorsList
from ...models.new_alert_retrigger_rule import NewAlertRetriggerRule
from ...types import Response


def _get_kwargs(
    *,
    body: NewAlertRetriggerRule,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/alert_retrigger_rules",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/vnd.api+json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[AlertRetriggerRuleResponse, ErrorsList]]:
    if response.status_code == 201:
        response_201 = AlertRetriggerRuleResponse.from_dict(response.json())

        return response_201

    if response.status_code == 422:
        response_422 = ErrorsList.from_dict(response.json())

        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[AlertRetriggerRuleResponse, ErrorsList]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: NewAlertRetriggerRule,
) -> Response[Union[AlertRetriggerRuleResponse, ErrorsList]]:
    """Creates an alert re-trigger rule

    Args:
        body (NewAlertRetriggerRule):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[AlertRetriggerRuleResponse, ErrorsList]]
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
    body: NewAlertRetriggerRule,
) -> Optional[Union[AlertRetriggerRuleResponse, ErrorsList]]:
    """Creates an alert re-trigger rule

    Args:
        body (NewAlertRetriggerRule):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[AlertRetriggerRuleResponse, ErrorsList]
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: NewAlertRetriggerRule,
) -> Response[Union[AlertRetriggerRuleResponse, ErrorsList]]:
    """Creates an alert re-trigger rule

    Args:
        body (NewAlertRetriggerRule):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[AlertRetriggerRuleResponse, ErrorsList]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: NewAlertRetriggerRule,
) -> Optional[Union[AlertRetriggerRuleResponse, ErrorsList]]:
    """Creates an alert re-trigger rule

    Args:
        body (NewAlertRetriggerRule):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[AlertRetriggerRuleResponse, ErrorsList]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
