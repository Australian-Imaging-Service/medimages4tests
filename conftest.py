import os
from pathlib import Path
import tempfile
from importlib import import_module
import pytest

base_dicom_dir = Path(__file__).parent / "medimages4tests" / "dummy" / "dicom"
dicom_modules = [
    "__".join(p.relative_to(base_dicom_dir).with_suffix("").parts)
    for p in base_dicom_dir.glob("**/*.py")
    if p.stem not in ("base", "__init__")
]


@pytest.fixture
def work_dir():
    return Path(tempfile.mkdtemp())


@pytest.fixture(params=dicom_modules)
def dicom_module(request):
    module_path = "medimages4tests.dummy.dicom." + ".".join(request.param.split("__"))
    return import_module(module_path)


# For debugging in IDE's don't catch raised exceptions and let the IDE
# break at it
if os.getenv("_PYTEST_RAISE", "0") != "0":

    @pytest.hookimpl(tryfirst=True)
    def pytest_exception_interact(call):
        raise call.excinfo.value

    @pytest.hookimpl(tryfirst=True)
    def pytest_internalerror(excinfo):
        raise excinfo.value

    catch_cli_exceptions = False
else:
    catch_cli_exceptions = True
