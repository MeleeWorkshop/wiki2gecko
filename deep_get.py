from functools import reduce
from typing import Union


def deep_get(collection: Union[dict, list], *keys, default=None):
    def resolve_key(d, key):
        if isinstance(d, dict):
            return d.get(key, default)

        if isinstance(d, list):
            def get_index() -> Union[int, None]:
                if isinstance(key, int):
                    return key
                s = str(key)
                if s.isdigit():
                    return int(s)
                return None

            index = get_index()

            if index is None or index < 0 or index >= len(d):
                return default

            return d[index]

        return default

    return reduce(resolve_key, keys, collection)
