from typing import Any

__all__ = ["dict_exclude_none"]


def dict_exclude_none(d: dict[str, Any]) -> dict[str, Any]:
    """
    辞書型の値から None 値を除外する
    """
    result: dict[str, Any] = {}

    for k, v in d.items():
        if v is not None:
            result[k] = v

        elif v is dict:
            result[k] = dict_exclude_none(v)

        elif v is list and len(v) > 0:
            if v[0] is not dict:
                result[k] = v

            else:
                result[k] = [dict_exclude_none(v_item) for v_item in v]

    return result
