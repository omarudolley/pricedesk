from pathlib import Path
import json
import tracemalloc
from datetime import timedelta
from functools import wraps
from time import time
from typing import Any
from typing import Callable
from humanize import naturalsize, precisedelta
from loguru import logger

_ACTIVE_ANALYSES = 0
_DEBUG_MEMORY = True


def save_as_json(destination, data):
    logger.debug("Writing {dst}", dst=destination)
    pth = Path(destination)
    pth.write_text(
        json.dumps(data, ensure_ascii=False, indent=2, sort_keys=True).replace(
            "NaN", "null"
        ),
        encoding="utf-8",
    )


def read_json_from_file(path):
    logger.debug("Reading {path}", path=path)
    pth = Path(path)
    if not pth.exists():
        raise Exception(f"{path} not found")

    data = pth.read_text(encoding="utf-8")

    return data


# Wrapper to analyze time used by any function
def analyze_time(fn: Callable[..., Any]):
    @wraps(fn)
    def _wrap(*args, **kwargs):
        start = time()
        result = fn(*args, **kwargs)

        elapsed = time() - start
        logger.debug(
            "{name} took {time}",
            name=fn.__name__,
            time=precisedelta(timedelta(seconds=elapsed)),
        )

        return result

    return _wrap


# Wrapper to analyze memory usage of any function
def analyze_memory(fn: Callable[..., Any]):
    @wraps(fn)
    def _wrap(*args, **kwargs):
        global _ACTIVE_ANALYSES

        if _DEBUG_MEMORY:
            if _ACTIVE_ANALYSES == 0:
                tracemalloc.start()
            _ACTIVE_ANALYSES += 1

        result = fn(*args, **kwargs)

        if _DEBUG_MEMORY:
            _, peak = tracemalloc.get_traced_memory()

            _ACTIVE_ANALYSES -= 1
            if _ACTIVE_ANALYSES == 0:
                tracemalloc.stop()

            logger.debug(
                "{name} peak memory usage {peak}",
                name=fn.__name__,
                peak=naturalsize(peak, binary=True),
            )

        return result

    return _wrap
