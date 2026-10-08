from typing import Literal

ProblemResponseDataType = Literal["problems"]

PROBLEM_RESPONSE_DATA_TYPE_VALUES: set[ProblemResponseDataType] = {
    "problems",
}


def check_problem_response_data_type(value: str | None) -> ProblemResponseDataType | None:
    if value is None:
        return None
    if value in PROBLEM_RESPONSE_DATA_TYPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PROBLEM_RESPONSE_DATA_TYPE_VALUES!r}")
