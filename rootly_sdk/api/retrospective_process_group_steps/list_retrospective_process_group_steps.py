from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.retrospective_process_group_step_list import RetrospectiveProcessGroupStepList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    retrospective_process_group_id: str,
    *,
    include: Unset | str = UNSET,
    pagenumber: Unset | int = UNSET,
    pagesize: Unset | int = UNSET,
    filterretrospective_step_id: Unset | str = UNSET,
    filtercreated_atgt: Unset | str = UNSET,
    filtercreated_atgte: Unset | str = UNSET,
    filtercreated_atlt: Unset | str = UNSET,
    filtercreated_atlte: Unset | str = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["include"] = include

    params["page[number]"] = pagenumber

    params["page[size]"] = pagesize

    params["filter[retrospective_step_id]"] = filterretrospective_step_id

    params["filter[created_at][gt]"] = filtercreated_atgt

    params["filter[created_at][gte]"] = filtercreated_atgte

    params["filter[created_at][lt]"] = filtercreated_atlt

    params["filter[created_at][lte]"] = filtercreated_atlte

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/v1/retrospective_process_groups/{retrospective_process_group_id}/steps",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> RetrospectiveProcessGroupStepList | None:
    if response.status_code == 200:
        response_200 = RetrospectiveProcessGroupStepList.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[RetrospectiveProcessGroupStepList]:
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
    include: Unset | str = UNSET,
    pagenumber: Unset | int = UNSET,
    pagesize: Unset | int = UNSET,
    filterretrospective_step_id: Unset | str = UNSET,
    filtercreated_atgt: Unset | str = UNSET,
    filtercreated_atgte: Unset | str = UNSET,
    filtercreated_atlt: Unset | str = UNSET,
    filtercreated_atlte: Unset | str = UNSET,
) -> Response[RetrospectiveProcessGroupStepList]:
    """List RetrospectiveProcessGroup Steps

     List RetrospectiveProcessGroup Steps

    Args:
        retrospective_process_group_id (str):
        include (Union[Unset, str]):
        pagenumber (Union[Unset, int]):
        pagesize (Union[Unset, int]):
        filterretrospective_step_id (Union[Unset, str]):
        filtercreated_atgt (Union[Unset, str]):
        filtercreated_atgte (Union[Unset, str]):
        filtercreated_atlt (Union[Unset, str]):
        filtercreated_atlte (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RetrospectiveProcessGroupStepList]
    """

    kwargs = _get_kwargs(
        retrospective_process_group_id=retrospective_process_group_id,
        include=include,
        pagenumber=pagenumber,
        pagesize=pagesize,
        filterretrospective_step_id=filterretrospective_step_id,
        filtercreated_atgt=filtercreated_atgt,
        filtercreated_atgte=filtercreated_atgte,
        filtercreated_atlt=filtercreated_atlt,
        filtercreated_atlte=filtercreated_atlte,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    retrospective_process_group_id: str,
    *,
    client: AuthenticatedClient,
    include: Unset | str = UNSET,
    pagenumber: Unset | int = UNSET,
    pagesize: Unset | int = UNSET,
    filterretrospective_step_id: Unset | str = UNSET,
    filtercreated_atgt: Unset | str = UNSET,
    filtercreated_atgte: Unset | str = UNSET,
    filtercreated_atlt: Unset | str = UNSET,
    filtercreated_atlte: Unset | str = UNSET,
) -> RetrospectiveProcessGroupStepList | None:
    """List RetrospectiveProcessGroup Steps

     List RetrospectiveProcessGroup Steps

    Args:
        retrospective_process_group_id (str):
        include (Union[Unset, str]):
        pagenumber (Union[Unset, int]):
        pagesize (Union[Unset, int]):
        filterretrospective_step_id (Union[Unset, str]):
        filtercreated_atgt (Union[Unset, str]):
        filtercreated_atgte (Union[Unset, str]):
        filtercreated_atlt (Union[Unset, str]):
        filtercreated_atlte (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RetrospectiveProcessGroupStepList
    """

    return sync_detailed(
        retrospective_process_group_id=retrospective_process_group_id,
        client=client,
        include=include,
        pagenumber=pagenumber,
        pagesize=pagesize,
        filterretrospective_step_id=filterretrospective_step_id,
        filtercreated_atgt=filtercreated_atgt,
        filtercreated_atgte=filtercreated_atgte,
        filtercreated_atlt=filtercreated_atlt,
        filtercreated_atlte=filtercreated_atlte,
    ).parsed


async def asyncio_detailed(
    retrospective_process_group_id: str,
    *,
    client: AuthenticatedClient,
    include: Unset | str = UNSET,
    pagenumber: Unset | int = UNSET,
    pagesize: Unset | int = UNSET,
    filterretrospective_step_id: Unset | str = UNSET,
    filtercreated_atgt: Unset | str = UNSET,
    filtercreated_atgte: Unset | str = UNSET,
    filtercreated_atlt: Unset | str = UNSET,
    filtercreated_atlte: Unset | str = UNSET,
) -> Response[RetrospectiveProcessGroupStepList]:
    """List RetrospectiveProcessGroup Steps

     List RetrospectiveProcessGroup Steps

    Args:
        retrospective_process_group_id (str):
        include (Union[Unset, str]):
        pagenumber (Union[Unset, int]):
        pagesize (Union[Unset, int]):
        filterretrospective_step_id (Union[Unset, str]):
        filtercreated_atgt (Union[Unset, str]):
        filtercreated_atgte (Union[Unset, str]):
        filtercreated_atlt (Union[Unset, str]):
        filtercreated_atlte (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RetrospectiveProcessGroupStepList]
    """

    kwargs = _get_kwargs(
        retrospective_process_group_id=retrospective_process_group_id,
        include=include,
        pagenumber=pagenumber,
        pagesize=pagesize,
        filterretrospective_step_id=filterretrospective_step_id,
        filtercreated_atgt=filtercreated_atgt,
        filtercreated_atgte=filtercreated_atgte,
        filtercreated_atlt=filtercreated_atlt,
        filtercreated_atlte=filtercreated_atlte,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    retrospective_process_group_id: str,
    *,
    client: AuthenticatedClient,
    include: Unset | str = UNSET,
    pagenumber: Unset | int = UNSET,
    pagesize: Unset | int = UNSET,
    filterretrospective_step_id: Unset | str = UNSET,
    filtercreated_atgt: Unset | str = UNSET,
    filtercreated_atgte: Unset | str = UNSET,
    filtercreated_atlt: Unset | str = UNSET,
    filtercreated_atlte: Unset | str = UNSET,
) -> RetrospectiveProcessGroupStepList | None:
    """List RetrospectiveProcessGroup Steps

     List RetrospectiveProcessGroup Steps

    Args:
        retrospective_process_group_id (str):
        include (Union[Unset, str]):
        pagenumber (Union[Unset, int]):
        pagesize (Union[Unset, int]):
        filterretrospective_step_id (Union[Unset, str]):
        filtercreated_atgt (Union[Unset, str]):
        filtercreated_atgte (Union[Unset, str]):
        filtercreated_atlt (Union[Unset, str]):
        filtercreated_atlte (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RetrospectiveProcessGroupStepList
    """

    return (
        await asyncio_detailed(
            retrospective_process_group_id=retrospective_process_group_id,
            client=client,
            include=include,
            pagenumber=pagenumber,
            pagesize=pagesize,
            filterretrospective_step_id=filterretrospective_step_id,
            filtercreated_atgt=filtercreated_atgt,
            filtercreated_atgte=filtercreated_atgte,
            filtercreated_atlt=filtercreated_atlt,
            filtercreated_atlte=filtercreated_atlte,
        )
    ).parsed
