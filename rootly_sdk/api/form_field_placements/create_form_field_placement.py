from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.errors_list import ErrorsList
from ...models.form_field_placement_response import FormFieldPlacementResponse
from ...models.new_form_field_placement import NewFormFieldPlacement
from ...types import Response


def _get_kwargs(
    form_field_id: str,
    *,
    body: NewFormFieldPlacement,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/v1/form_fields/{form_field_id}/placements",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/vnd.api+json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorsList | FormFieldPlacementResponse | None:
    if response.status_code == 201:
        response_201 = FormFieldPlacementResponse.from_dict(response.json())

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
) -> Response[ErrorsList | FormFieldPlacementResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    form_field_id: str,
    *,
    client: AuthenticatedClient,
    body: NewFormFieldPlacement,
) -> Response[ErrorsList | FormFieldPlacementResponse]:
    """Creates a Form Field Placement

     Creates a new form_field_placement from provided data

    Args:
        form_field_id (str):
        body (NewFormFieldPlacement):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorsList, FormFieldPlacementResponse]]
    """

    kwargs = _get_kwargs(
        form_field_id=form_field_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    form_field_id: str,
    *,
    client: AuthenticatedClient,
    body: NewFormFieldPlacement,
) -> ErrorsList | FormFieldPlacementResponse | None:
    """Creates a Form Field Placement

     Creates a new form_field_placement from provided data

    Args:
        form_field_id (str):
        body (NewFormFieldPlacement):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorsList, FormFieldPlacementResponse]
    """

    return sync_detailed(
        form_field_id=form_field_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    form_field_id: str,
    *,
    client: AuthenticatedClient,
    body: NewFormFieldPlacement,
) -> Response[ErrorsList | FormFieldPlacementResponse]:
    """Creates a Form Field Placement

     Creates a new form_field_placement from provided data

    Args:
        form_field_id (str):
        body (NewFormFieldPlacement):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorsList, FormFieldPlacementResponse]]
    """

    kwargs = _get_kwargs(
        form_field_id=form_field_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    form_field_id: str,
    *,
    client: AuthenticatedClient,
    body: NewFormFieldPlacement,
) -> ErrorsList | FormFieldPlacementResponse | None:
    """Creates a Form Field Placement

     Creates a new form_field_placement from provided data

    Args:
        form_field_id (str):
        body (NewFormFieldPlacement):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorsList, FormFieldPlacementResponse]
    """

    return (
        await asyncio_detailed(
            form_field_id=form_field_id,
            client=client,
            body=body,
        )
    ).parsed
