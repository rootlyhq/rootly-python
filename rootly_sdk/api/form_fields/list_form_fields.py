from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.form_field_list import FormFieldList
from ...models.list_form_fields_include import ListFormFieldsInclude
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    include: Unset | ListFormFieldsInclude = UNSET,
    pagenumber: Unset | int = UNSET,
    pagesize: Unset | int = UNSET,
    filtersearch: Unset | str = UNSET,
    filterslug: Unset | str = UNSET,
    filtername: Unset | str = UNSET,
    filterkind: Unset | str = UNSET,
    filterenabled: Unset | bool = UNSET,
    filtercreated_atgt: Unset | str = UNSET,
    filtercreated_atgte: Unset | str = UNSET,
    filtercreated_atlt: Unset | str = UNSET,
    filtercreated_atlte: Unset | str = UNSET,
    filterslugeq: Unset | str = UNSET,
    filterslugnot_eq: Unset | str = UNSET,
    filterslugin: Unset | str = UNSET,
    filterslugnot_in: Unset | str = UNSET,
    filternameeq: Unset | str = UNSET,
    filternamenot_eq: Unset | str = UNSET,
    filternamein: Unset | str = UNSET,
    filternamenot_in: Unset | str = UNSET,
    filterkindeq: Unset | str = UNSET,
    filterkindnot_eq: Unset | str = UNSET,
    filterkindin: Unset | str = UNSET,
    filterkindnot_in: Unset | str = UNSET,
    filterenabledeq: Unset | str = UNSET,
    filterenablednot_eq: Unset | str = UNSET,
    filterenabledin: Unset | str = UNSET,
    filterenablednot_in: Unset | str = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_include: Unset | str = UNSET
    if not isinstance(include, Unset):
        json_include = include

    params["include"] = json_include

    params["page[number]"] = pagenumber

    params["page[size]"] = pagesize

    params["filter[search]"] = filtersearch

    params["filter[slug]"] = filterslug

    params["filter[name]"] = filtername

    params["filter[kind]"] = filterkind

    params["filter[enabled]"] = filterenabled

    params["filter[created_at][gt]"] = filtercreated_atgt

    params["filter[created_at][gte]"] = filtercreated_atgte

    params["filter[created_at][lt]"] = filtercreated_atlt

    params["filter[created_at][lte]"] = filtercreated_atlte

    params["filter[slug][eq]"] = filterslugeq

    params["filter[slug][not_eq]"] = filterslugnot_eq

    params["filter[slug][in]"] = filterslugin

    params["filter[slug][not_in]"] = filterslugnot_in

    params["filter[name][eq]"] = filternameeq

    params["filter[name][not_eq]"] = filternamenot_eq

    params["filter[name][in]"] = filternamein

    params["filter[name][not_in]"] = filternamenot_in

    params["filter[kind][eq]"] = filterkindeq

    params["filter[kind][not_eq]"] = filterkindnot_eq

    params["filter[kind][in]"] = filterkindin

    params["filter[kind][not_in]"] = filterkindnot_in

    params["filter[enabled][eq]"] = filterenabledeq

    params["filter[enabled][not_eq]"] = filterenablednot_eq

    params["filter[enabled][in]"] = filterenabledin

    params["filter[enabled][not_in]"] = filterenablednot_in

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/form_fields",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> FormFieldList | None:
    if response.status_code == 200:
        response_200 = FormFieldList.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[FormFieldList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    include: Unset | ListFormFieldsInclude = UNSET,
    pagenumber: Unset | int = UNSET,
    pagesize: Unset | int = UNSET,
    filtersearch: Unset | str = UNSET,
    filterslug: Unset | str = UNSET,
    filtername: Unset | str = UNSET,
    filterkind: Unset | str = UNSET,
    filterenabled: Unset | bool = UNSET,
    filtercreated_atgt: Unset | str = UNSET,
    filtercreated_atgte: Unset | str = UNSET,
    filtercreated_atlt: Unset | str = UNSET,
    filtercreated_atlte: Unset | str = UNSET,
    filterslugeq: Unset | str = UNSET,
    filterslugnot_eq: Unset | str = UNSET,
    filterslugin: Unset | str = UNSET,
    filterslugnot_in: Unset | str = UNSET,
    filternameeq: Unset | str = UNSET,
    filternamenot_eq: Unset | str = UNSET,
    filternamein: Unset | str = UNSET,
    filternamenot_in: Unset | str = UNSET,
    filterkindeq: Unset | str = UNSET,
    filterkindnot_eq: Unset | str = UNSET,
    filterkindin: Unset | str = UNSET,
    filterkindnot_in: Unset | str = UNSET,
    filterenabledeq: Unset | str = UNSET,
    filterenablednot_eq: Unset | str = UNSET,
    filterenabledin: Unset | str = UNSET,
    filterenablednot_in: Unset | str = UNSET,
) -> Response[FormFieldList]:
    """List Form Fields

     List form_fields

    Args:
        include (Union[Unset, ListFormFieldsInclude]):
        pagenumber (Union[Unset, int]):
        pagesize (Union[Unset, int]):
        filtersearch (Union[Unset, str]):
        filterslug (Union[Unset, str]):
        filtername (Union[Unset, str]):
        filterkind (Union[Unset, str]):
        filterenabled (Union[Unset, bool]):
        filtercreated_atgt (Union[Unset, str]):
        filtercreated_atgte (Union[Unset, str]):
        filtercreated_atlt (Union[Unset, str]):
        filtercreated_atlte (Union[Unset, str]):
        filterslugeq (Union[Unset, str]):
        filterslugnot_eq (Union[Unset, str]):
        filterslugin (Union[Unset, str]):
        filterslugnot_in (Union[Unset, str]):
        filternameeq (Union[Unset, str]):
        filternamenot_eq (Union[Unset, str]):
        filternamein (Union[Unset, str]):
        filternamenot_in (Union[Unset, str]):
        filterkindeq (Union[Unset, str]):
        filterkindnot_eq (Union[Unset, str]):
        filterkindin (Union[Unset, str]):
        filterkindnot_in (Union[Unset, str]):
        filterenabledeq (Union[Unset, str]):
        filterenablednot_eq (Union[Unset, str]):
        filterenabledin (Union[Unset, str]):
        filterenablednot_in (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FormFieldList]
    """

    kwargs = _get_kwargs(
        include=include,
        pagenumber=pagenumber,
        pagesize=pagesize,
        filtersearch=filtersearch,
        filterslug=filterslug,
        filtername=filtername,
        filterkind=filterkind,
        filterenabled=filterenabled,
        filtercreated_atgt=filtercreated_atgt,
        filtercreated_atgte=filtercreated_atgte,
        filtercreated_atlt=filtercreated_atlt,
        filtercreated_atlte=filtercreated_atlte,
        filterslugeq=filterslugeq,
        filterslugnot_eq=filterslugnot_eq,
        filterslugin=filterslugin,
        filterslugnot_in=filterslugnot_in,
        filternameeq=filternameeq,
        filternamenot_eq=filternamenot_eq,
        filternamein=filternamein,
        filternamenot_in=filternamenot_in,
        filterkindeq=filterkindeq,
        filterkindnot_eq=filterkindnot_eq,
        filterkindin=filterkindin,
        filterkindnot_in=filterkindnot_in,
        filterenabledeq=filterenabledeq,
        filterenablednot_eq=filterenablednot_eq,
        filterenabledin=filterenabledin,
        filterenablednot_in=filterenablednot_in,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    include: Unset | ListFormFieldsInclude = UNSET,
    pagenumber: Unset | int = UNSET,
    pagesize: Unset | int = UNSET,
    filtersearch: Unset | str = UNSET,
    filterslug: Unset | str = UNSET,
    filtername: Unset | str = UNSET,
    filterkind: Unset | str = UNSET,
    filterenabled: Unset | bool = UNSET,
    filtercreated_atgt: Unset | str = UNSET,
    filtercreated_atgte: Unset | str = UNSET,
    filtercreated_atlt: Unset | str = UNSET,
    filtercreated_atlte: Unset | str = UNSET,
    filterslugeq: Unset | str = UNSET,
    filterslugnot_eq: Unset | str = UNSET,
    filterslugin: Unset | str = UNSET,
    filterslugnot_in: Unset | str = UNSET,
    filternameeq: Unset | str = UNSET,
    filternamenot_eq: Unset | str = UNSET,
    filternamein: Unset | str = UNSET,
    filternamenot_in: Unset | str = UNSET,
    filterkindeq: Unset | str = UNSET,
    filterkindnot_eq: Unset | str = UNSET,
    filterkindin: Unset | str = UNSET,
    filterkindnot_in: Unset | str = UNSET,
    filterenabledeq: Unset | str = UNSET,
    filterenablednot_eq: Unset | str = UNSET,
    filterenabledin: Unset | str = UNSET,
    filterenablednot_in: Unset | str = UNSET,
) -> FormFieldList | None:
    """List Form Fields

     List form_fields

    Args:
        include (Union[Unset, ListFormFieldsInclude]):
        pagenumber (Union[Unset, int]):
        pagesize (Union[Unset, int]):
        filtersearch (Union[Unset, str]):
        filterslug (Union[Unset, str]):
        filtername (Union[Unset, str]):
        filterkind (Union[Unset, str]):
        filterenabled (Union[Unset, bool]):
        filtercreated_atgt (Union[Unset, str]):
        filtercreated_atgte (Union[Unset, str]):
        filtercreated_atlt (Union[Unset, str]):
        filtercreated_atlte (Union[Unset, str]):
        filterslugeq (Union[Unset, str]):
        filterslugnot_eq (Union[Unset, str]):
        filterslugin (Union[Unset, str]):
        filterslugnot_in (Union[Unset, str]):
        filternameeq (Union[Unset, str]):
        filternamenot_eq (Union[Unset, str]):
        filternamein (Union[Unset, str]):
        filternamenot_in (Union[Unset, str]):
        filterkindeq (Union[Unset, str]):
        filterkindnot_eq (Union[Unset, str]):
        filterkindin (Union[Unset, str]):
        filterkindnot_in (Union[Unset, str]):
        filterenabledeq (Union[Unset, str]):
        filterenablednot_eq (Union[Unset, str]):
        filterenabledin (Union[Unset, str]):
        filterenablednot_in (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FormFieldList
    """

    return sync_detailed(
        client=client,
        include=include,
        pagenumber=pagenumber,
        pagesize=pagesize,
        filtersearch=filtersearch,
        filterslug=filterslug,
        filtername=filtername,
        filterkind=filterkind,
        filterenabled=filterenabled,
        filtercreated_atgt=filtercreated_atgt,
        filtercreated_atgte=filtercreated_atgte,
        filtercreated_atlt=filtercreated_atlt,
        filtercreated_atlte=filtercreated_atlte,
        filterslugeq=filterslugeq,
        filterslugnot_eq=filterslugnot_eq,
        filterslugin=filterslugin,
        filterslugnot_in=filterslugnot_in,
        filternameeq=filternameeq,
        filternamenot_eq=filternamenot_eq,
        filternamein=filternamein,
        filternamenot_in=filternamenot_in,
        filterkindeq=filterkindeq,
        filterkindnot_eq=filterkindnot_eq,
        filterkindin=filterkindin,
        filterkindnot_in=filterkindnot_in,
        filterenabledeq=filterenabledeq,
        filterenablednot_eq=filterenablednot_eq,
        filterenabledin=filterenabledin,
        filterenablednot_in=filterenablednot_in,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    include: Unset | ListFormFieldsInclude = UNSET,
    pagenumber: Unset | int = UNSET,
    pagesize: Unset | int = UNSET,
    filtersearch: Unset | str = UNSET,
    filterslug: Unset | str = UNSET,
    filtername: Unset | str = UNSET,
    filterkind: Unset | str = UNSET,
    filterenabled: Unset | bool = UNSET,
    filtercreated_atgt: Unset | str = UNSET,
    filtercreated_atgte: Unset | str = UNSET,
    filtercreated_atlt: Unset | str = UNSET,
    filtercreated_atlte: Unset | str = UNSET,
    filterslugeq: Unset | str = UNSET,
    filterslugnot_eq: Unset | str = UNSET,
    filterslugin: Unset | str = UNSET,
    filterslugnot_in: Unset | str = UNSET,
    filternameeq: Unset | str = UNSET,
    filternamenot_eq: Unset | str = UNSET,
    filternamein: Unset | str = UNSET,
    filternamenot_in: Unset | str = UNSET,
    filterkindeq: Unset | str = UNSET,
    filterkindnot_eq: Unset | str = UNSET,
    filterkindin: Unset | str = UNSET,
    filterkindnot_in: Unset | str = UNSET,
    filterenabledeq: Unset | str = UNSET,
    filterenablednot_eq: Unset | str = UNSET,
    filterenabledin: Unset | str = UNSET,
    filterenablednot_in: Unset | str = UNSET,
) -> Response[FormFieldList]:
    """List Form Fields

     List form_fields

    Args:
        include (Union[Unset, ListFormFieldsInclude]):
        pagenumber (Union[Unset, int]):
        pagesize (Union[Unset, int]):
        filtersearch (Union[Unset, str]):
        filterslug (Union[Unset, str]):
        filtername (Union[Unset, str]):
        filterkind (Union[Unset, str]):
        filterenabled (Union[Unset, bool]):
        filtercreated_atgt (Union[Unset, str]):
        filtercreated_atgte (Union[Unset, str]):
        filtercreated_atlt (Union[Unset, str]):
        filtercreated_atlte (Union[Unset, str]):
        filterslugeq (Union[Unset, str]):
        filterslugnot_eq (Union[Unset, str]):
        filterslugin (Union[Unset, str]):
        filterslugnot_in (Union[Unset, str]):
        filternameeq (Union[Unset, str]):
        filternamenot_eq (Union[Unset, str]):
        filternamein (Union[Unset, str]):
        filternamenot_in (Union[Unset, str]):
        filterkindeq (Union[Unset, str]):
        filterkindnot_eq (Union[Unset, str]):
        filterkindin (Union[Unset, str]):
        filterkindnot_in (Union[Unset, str]):
        filterenabledeq (Union[Unset, str]):
        filterenablednot_eq (Union[Unset, str]):
        filterenabledin (Union[Unset, str]):
        filterenablednot_in (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FormFieldList]
    """

    kwargs = _get_kwargs(
        include=include,
        pagenumber=pagenumber,
        pagesize=pagesize,
        filtersearch=filtersearch,
        filterslug=filterslug,
        filtername=filtername,
        filterkind=filterkind,
        filterenabled=filterenabled,
        filtercreated_atgt=filtercreated_atgt,
        filtercreated_atgte=filtercreated_atgte,
        filtercreated_atlt=filtercreated_atlt,
        filtercreated_atlte=filtercreated_atlte,
        filterslugeq=filterslugeq,
        filterslugnot_eq=filterslugnot_eq,
        filterslugin=filterslugin,
        filterslugnot_in=filterslugnot_in,
        filternameeq=filternameeq,
        filternamenot_eq=filternamenot_eq,
        filternamein=filternamein,
        filternamenot_in=filternamenot_in,
        filterkindeq=filterkindeq,
        filterkindnot_eq=filterkindnot_eq,
        filterkindin=filterkindin,
        filterkindnot_in=filterkindnot_in,
        filterenabledeq=filterenabledeq,
        filterenablednot_eq=filterenablednot_eq,
        filterenabledin=filterenabledin,
        filterenablednot_in=filterenablednot_in,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    include: Unset | ListFormFieldsInclude = UNSET,
    pagenumber: Unset | int = UNSET,
    pagesize: Unset | int = UNSET,
    filtersearch: Unset | str = UNSET,
    filterslug: Unset | str = UNSET,
    filtername: Unset | str = UNSET,
    filterkind: Unset | str = UNSET,
    filterenabled: Unset | bool = UNSET,
    filtercreated_atgt: Unset | str = UNSET,
    filtercreated_atgte: Unset | str = UNSET,
    filtercreated_atlt: Unset | str = UNSET,
    filtercreated_atlte: Unset | str = UNSET,
    filterslugeq: Unset | str = UNSET,
    filterslugnot_eq: Unset | str = UNSET,
    filterslugin: Unset | str = UNSET,
    filterslugnot_in: Unset | str = UNSET,
    filternameeq: Unset | str = UNSET,
    filternamenot_eq: Unset | str = UNSET,
    filternamein: Unset | str = UNSET,
    filternamenot_in: Unset | str = UNSET,
    filterkindeq: Unset | str = UNSET,
    filterkindnot_eq: Unset | str = UNSET,
    filterkindin: Unset | str = UNSET,
    filterkindnot_in: Unset | str = UNSET,
    filterenabledeq: Unset | str = UNSET,
    filterenablednot_eq: Unset | str = UNSET,
    filterenabledin: Unset | str = UNSET,
    filterenablednot_in: Unset | str = UNSET,
) -> FormFieldList | None:
    """List Form Fields

     List form_fields

    Args:
        include (Union[Unset, ListFormFieldsInclude]):
        pagenumber (Union[Unset, int]):
        pagesize (Union[Unset, int]):
        filtersearch (Union[Unset, str]):
        filterslug (Union[Unset, str]):
        filtername (Union[Unset, str]):
        filterkind (Union[Unset, str]):
        filterenabled (Union[Unset, bool]):
        filtercreated_atgt (Union[Unset, str]):
        filtercreated_atgte (Union[Unset, str]):
        filtercreated_atlt (Union[Unset, str]):
        filtercreated_atlte (Union[Unset, str]):
        filterslugeq (Union[Unset, str]):
        filterslugnot_eq (Union[Unset, str]):
        filterslugin (Union[Unset, str]):
        filterslugnot_in (Union[Unset, str]):
        filternameeq (Union[Unset, str]):
        filternamenot_eq (Union[Unset, str]):
        filternamein (Union[Unset, str]):
        filternamenot_in (Union[Unset, str]):
        filterkindeq (Union[Unset, str]):
        filterkindnot_eq (Union[Unset, str]):
        filterkindin (Union[Unset, str]):
        filterkindnot_in (Union[Unset, str]):
        filterenabledeq (Union[Unset, str]):
        filterenablednot_eq (Union[Unset, str]):
        filterenabledin (Union[Unset, str]):
        filterenablednot_in (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FormFieldList
    """

    return (
        await asyncio_detailed(
            client=client,
            include=include,
            pagenumber=pagenumber,
            pagesize=pagesize,
            filtersearch=filtersearch,
            filterslug=filterslug,
            filtername=filtername,
            filterkind=filterkind,
            filterenabled=filterenabled,
            filtercreated_atgt=filtercreated_atgt,
            filtercreated_atgte=filtercreated_atgte,
            filtercreated_atlt=filtercreated_atlt,
            filtercreated_atlte=filtercreated_atlte,
            filterslugeq=filterslugeq,
            filterslugnot_eq=filterslugnot_eq,
            filterslugin=filterslugin,
            filterslugnot_in=filterslugnot_in,
            filternameeq=filternameeq,
            filternamenot_eq=filternamenot_eq,
            filternamein=filternamein,
            filternamenot_in=filternamenot_in,
            filterkindeq=filterkindeq,
            filterkindnot_eq=filterkindnot_eq,
            filterkindin=filterkindin,
            filterkindnot_in=filterkindnot_in,
            filterenabledeq=filterenabledeq,
            filterenablednot_eq=filterenablednot_eq,
            filterenabledin=filterenabledin,
            filterenablednot_in=filterenablednot_in,
        )
    ).parsed
