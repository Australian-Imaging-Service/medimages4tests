import tempfile
from pathlib import Path
from types import ModuleType
from importlib import import_module
import pytest

sub_pkg_path = [
    "medimages4tests",
    "dummy",
    "raw",
    "pet",
    "siemens",
    "biograph_vision",
    "vr20b",
]

base_raw_pet_dir = Path(__file__).parent.parent.joinpath(*sub_pkg_path)
raw_pet_modules = [
    p.name
    for p in base_raw_pet_dir.iterdir()
    if p.stem != "base" and not p.stem.startswith("__") and not p.stem.startswith(".")
]


@pytest.fixture(params=raw_pet_modules)
def siemens_raw_pet_data(request) -> ModuleType:
    module_path = ".".join(sub_pkg_path + [request.param])
    return import_module(module_path)


def test_siemens_raw_pet_data_creation(siemens_raw_pet_data: ModuleType):

    out_dir = Path(tempfile.mkdtemp())

    # Generate raw PET data files
    siemens_raw_pet_data.get_image(out_dir)
