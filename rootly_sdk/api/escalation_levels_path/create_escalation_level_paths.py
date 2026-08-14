from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.errors_list import ErrorsList
from ...models.escalation_policy_level_response import EscalationPolicyLevelResponse
from ...models.new_escalation_policy_level import NewEscalationPolicyLevel
from ...types import Response


def _get_kwargs(
    escalation_policy_path_id: str,
    *,
    body: NewEscalationPolicyLevel,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/v1/escalation_paths/{escalation_policy_path_id}/escalation_levels",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/vnd.api+json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorsList | EscalationPolicyLevelResponse | None:
    if response.status_code == 201:
        response_201 = EscalationPolicyLevelResponse.from_dict(response.json())

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
) -> Response[ErrorsList | EscalationPolicyLevelResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    escalation_policy_path_id: str,
    *,
    client: AuthenticatedClient,
    body: NewEscalationPolicyLevel,
) -> Response[ErrorsList | EscalationPolicyLevelResponse]:
    """Creates an escalation level for an Escalation Path

     Creates a new escalation level from provided data

    Args:
        escalation_policy_path_id (str):
        body (NewEscalationPolicyLevel):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorsList, EscalationPolicyLevelResponse]]
    """

    kwargs = _get_kwargs(
        escalation_policy_path_id=escalation_policy_path_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    escalation_policy_path_id: str,
    *,
    client: AuthenticatedClient,
    body: NewEscalationPolicyLevel,
) -> ErrorsList | EscalationPolicyLevelResponse | None:
    """Creates an escalation level for an Escalation Path

     Creates a new escalation level from provided data

    Args:
        escalation_policy_path_id (str):
        body (NewEscalationPolicyLevel):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorsList, EscalationPolicyLevelResponse]
    """

    return sync_detailed(
        escalation_policy_path_id=escalation_policy_path_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    escalation_policy_path_id: str,
    *,
    client: AuthenticatedClient,
    body: NewEscalationPolicyLevel,
) -> Response[ErrorsList | EscalationPolicyLevelResponse]:
    """Creates an escalation level for an Escalation Path

     Creates a new escalation level from provided data

    Args:
        escalation_policy_path_id (str):
        body (NewEscalationPolicyLevel):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorsList, EscalationPolicyLevelResponse]]
    """

    kwargs = _get_kwargs(
        escalation_policy_path_id=escalation_policy_path_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    escalation_policy_path_id: str,
    *,
    client: AuthenticatedClient,
    body: NewEscalationPolicyLevel,
) -> ErrorsList | EscalationPolicyLevelResponse | None:
    """Creates an escalation level for an Escalation Path

     Creates a new escalation level from provided data

    Args:
        escalation_policy_path_id (str):
        body (NewEscalationPolicyLevel):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorsList, EscalationPolicyLevelResponse]
    """

    return (
        await asyncio_detailed(
            escalation_policy_path_id=escalation_policy_path_id,
            client=client,
            body=body,
        )
    ).parsed
