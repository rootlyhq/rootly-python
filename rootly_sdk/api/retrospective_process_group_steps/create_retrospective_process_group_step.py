from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.errors_list import ErrorsList
from ...models.new_retrospective_process_group_step import NewRetrospectiveProcessGroupStep
from ...models.retrospective_process_group_step_response import RetrospectiveProcessGroupStepResponse
from ...types import Response


def _get_kwargs(
    retrospective_process_group_id: str,
    *,
    body: NewRetrospectiveProcessGroupStep,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/v1/retrospective_process_groups/{retrospective_process_group_id}/steps",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/vnd.api+json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorsList | RetrospectiveProcessGroupStepResponse | None:
    if response.status_code == 201:
        response_201 = RetrospectiveProcessGroupStepResponse.from_dict(response.json())

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
) -> Response[ErrorsList | RetrospectiveProcessGroupStepResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    retrospective_process_group_id: str,
    *,
    client: AuthenticatedClient,
    body: NewRetrospectiveProcessGroupStep,
) -> Response[ErrorsList | RetrospectiveProcessGroupStepResponse]:
    """Creates a retrospective process group step

     Creates a new retrospective process group step from provided data

    Args:
        retrospective_process_group_id (str):
        body (NewRetrospectiveProcessGroupStep):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorsList, RetrospectiveProcessGroupStepResponse]]
    """

    kwargs = _get_kwargs(
        retrospective_process_group_id=retrospective_process_group_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    retrospective_process_group_id: str,
    *,
    client: AuthenticatedClient,
    body: NewRetrospectiveProcessGroupStep,
) -> ErrorsList | RetrospectiveProcessGroupStepResponse | None:
    """Creates a retrospective process group step

     Creates a new retrospective process group step from provided data

    Args:
        retrospective_process_group_id (str):
        body (NewRetrospectiveProcessGroupStep):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorsList, RetrospectiveProcessGroupStepResponse]
    """

    return sync_detailed(
        retrospective_process_group_id=retrospective_process_group_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    retrospective_process_group_id: str,
    *,
    client: AuthenticatedClient,
    body: NewRetrospectiveProcessGroupStep,
) -> Response[ErrorsList | RetrospectiveProcessGroupStepResponse]:
    """Creates a retrospective process group step

     Creates a new retrospective process group step from provided data

    Args:
        retrospective_process_group_id (str):
        body (NewRetrospectiveProcessGroupStep):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorsList, RetrospectiveProcessGroupStepResponse]]
    """

    kwargs = _get_kwargs(
        retrospective_process_group_id=retrospective_process_group_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    retrospective_process_group_id: str,
    *,
    client: AuthenticatedClient,
    body: NewRetrospectiveProcessGroupStep,
) -> ErrorsList | RetrospectiveProcessGroupStepResponse | None:
    """Creates a retrospective process group step

     Creates a new retrospective process group step from provided data

    Args:
        retrospective_process_group_id (str):
        body (NewRetrospectiveProcessGroupStep):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorsList, RetrospectiveProcessGroupStepResponse]
    """

    return (
        await asyncio_detailed(
            retrospective_process_group_id=retrospective_process_group_id,
            client=client,
            body=body,
        )
    ).parsed
