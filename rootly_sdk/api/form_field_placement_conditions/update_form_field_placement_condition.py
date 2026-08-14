from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.errors_list import ErrorsList
from ...models.form_field_placement_condition_response import FormFieldPlacementConditionResponse
from ...models.update_form_field_placement_condition import UpdateFormFieldPlacementCondition
from ...types import Response


def _get_kwargs(
    id: str,
    *,
    body: UpdateFormFieldPlacementCondition,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": f"/v1/form_field_placement_conditions/{id}",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/vnd.api+json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorsList | FormFieldPlacementConditionResponse | None:
    if response.status_code == 200:
        response_200 = FormFieldPlacementConditionResponse.from_dict(response.json())

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
) -> Response[ErrorsList | FormFieldPlacementConditionResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    body: UpdateFormFieldPlacementCondition,
) -> Response[ErrorsList | FormFieldPlacementConditionResponse]:
    """Update a Form Set Condition

     Update a specific form_field_placement_condition by id

    Args:
        id (str):
        body (UpdateFormFieldPlacementCondition):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorsList, FormFieldPlacementConditionResponse]]
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
    id: str,
    *,
    client: AuthenticatedClient,
    body: UpdateFormFieldPlacementCondition,
) -> ErrorsList | FormFieldPlacementConditionResponse | None:
    """Update a Form Set Condition

     Update a specific form_field_placement_condition by id

    Args:
        id (str):
        body (UpdateFormFieldPlacementCondition):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorsList, FormFieldPlacementConditionResponse]
    """

    return sync_detailed(
        id=id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    body: UpdateFormFieldPlacementCondition,
) -> Response[ErrorsList | FormFieldPlacementConditionResponse]:
    """Update a Form Set Condition

     Update a specific form_field_placement_condition by id

    Args:
        id (str):
        body (UpdateFormFieldPlacementCondition):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorsList, FormFieldPlacementConditionResponse]]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient,
    body: UpdateFormFieldPlacementCondition,
) -> ErrorsList | FormFieldPlacementConditionResponse | None:
    """Update a Form Set Condition

     Update a specific form_field_placement_condition by id

    Args:
        id (str):
        body (UpdateFormFieldPlacementCondition):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorsList, FormFieldPlacementConditionResponse]
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
        )
    ).parsed
