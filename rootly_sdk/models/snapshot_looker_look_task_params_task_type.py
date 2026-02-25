from typing import Literal, cast

SnapshotLookerLookTaskParamsTaskType = Literal["snapshot_looker_look"]

SNAPSHOT_LOOKER_LOOK_TASK_PARAMS_TASK_TYPE_VALUES: set[SnapshotLookerLookTaskParamsTaskType] = {
    "snapshot_looker_look",
}


def check_snapshot_looker_look_task_params_task_type(value: str | None) -> SnapshotLookerLookTaskParamsTaskType | None:
    if value is None:
        return None
    if value in SNAPSHOT_LOOKER_LOOK_TASK_PARAMS_TASK_TYPE_VALUES:
        return cast(SnapshotLookerLookTaskParamsTaskType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {SNAPSHOT_LOOKER_LOOK_TASK_PARAMS_TASK_TYPE_VALUES!r}"
    )
