from pathlib import Path
import attrs


@attrs.define
class OpenneuroSpec:

    dataset: str
    tag: str
    path: Path
