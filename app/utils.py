import json
from pathlib import Path

from loguru import logger


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
