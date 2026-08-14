from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.form_field_placement_condition_list import FormFieldPlacementConditionList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    form_field_placement_id: str,
    *,
    include: Unset | str = UNSET,
    pagenumber: Unset | int = UNSET,
    pagesize: Unset | int = UNSET,
    filterform_field_id: Unset | str = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["include"] = include

    params["page[number]"] = pagenumber

    params["page[size]"] = pagesize

    params["filter[form_field_id]"] = filterform_field_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/v1/form_field_placements/{form_field_placement_id}/conditions",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> FormFieldPlacementConditionList | None:
    if response.status_code == 200:
        response_200 = FormFieldPlacementConditionList.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[FormFieldPlacementConditionList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    form_field_placement_id: str,
    *,
    client: AuthenticatedClient,
    include: Unset | str = UNSET,
    pagenumber: Unset | int = UNSET,
    pagesize: Unset | int = UNSET,
    filterform_field_id: Unset | str = UNSET,
) -> Response[FormFieldPlacementConditionList]:
    """List Form Set Conditions

     List form_field_placement_conditions

    Args:
        form_field_placement_id (str):
        include (Union[Unset, str]):
        pagenumber (Union[Unset, int]):
        pagesize (Union[Unset, int]):
        filterform_field_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FormFieldPlacementConditionList]
    """

    kwargs = _get_kwargs(
        form_field_placement_id=form_field_placement_id,
        include=include,
        pagenumber=pagenumber,
        pagesize=pagesize,
        filterform_field_id=filterform_field_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    form_field_placement_id: str,
    *,
    client: AuthenticatedClient,
    include: Unset | str = UNSET,
    pagenumber: Unset | int = UNSET,
    pagesize: Unset | int = UNSET,
    filterform_field_id: Unset | str = UNSET,
) -> FormFieldPlacementConditionList | None:
    """List Form Set Conditions

     List form_field_placement_conditions

    Args:
        form_field_placement_id (str):
        include (Union[Unset, str]):
        pagenumber (Union[Unset, int]):
        pagesize (Union[Unset, int]):
        filterform_field_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FormFieldPlacementConditionList
    """

    return sync_detailed(
        form_field_placement_id=form_field_placement_id,
        client=client,
        include=include,
        pagenumber=pagenumber,
        pagesize=pagesize,
        filterform_field_id=filterform_field_id,
    ).parsed


async def asyncio_detailed(
    form_field_placement_id: str,
    *,
    client: AuthenticatedClient,
    include: Unset | str = UNSET,
    pagenumber: Unset | int = UNSET,
    pagesize: Unset | int = UNSET,
    filterform_field_id: Unset | str = UNSET,
) -> Response[FormFieldPlacementConditionList]:
    """List Form Set Conditions

     List form_field_placement_conditions

    Args:
        form_field_placement_id (str):
        include (Union[Unset, str]):
        pagenumber (Union[Unset, int]):
        pagesize (Union[Unset, int]):
        filterform_field_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FormFieldPlacementConditionList]
    """

    kwargs = _get_kwargs(
        form_field_placement_id=form_field_placement_id,
        include=include,
        pagenumber=pagenumber,
        pagesize=pagesize,
        filterform_field_id=filterform_field_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    form_field_placement_id: str,
    *,
    client: AuthenticatedClient,
    include: Unset | str = UNSET,
    pagenumber: Unset | int = UNSET,
    pagesize: Unset | int = UNSET,
    filterform_field_id: Unset | str = UNSET,
) -> FormFieldPlacementConditionList | None:
    """List Form Set Conditions

     List form_field_placement_conditions

    Args:
        form_field_placement_id (str):
        include (Union[Unset, str]):
        pagenumber (Union[Unset, int]):
        pagesize (Union[Unset, int]):
        filterform_field_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FormFieldPlacementConditionList
    """

    return (
        await asyncio_detailed(
            form_field_placement_id=form_field_placement_id,
            client=client,
            include=include,
            pagenumber=pagenumber,
            pagesize=pagesize,
            filterform_field_id=filterform_field_id,
        )
    ).parsed
