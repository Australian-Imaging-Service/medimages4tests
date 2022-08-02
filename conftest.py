from pathlib import Path
from importlib import import_module
import pytest

base_dicom_dir = Path(__file__).parent / 'medimages4tests' / 'dicom'
dicom_modules = ['__'.join(p.relative_to(base_dicom_dir).with_suffix('').parts)
                 for p in base_dicom_dir.glob('**/*.py')
                 if p.stem != 'base']


@pytest.fixture(params=dicom_modules)
def dicom_module(request):
    module_path = 'medimages4tests.dicom.' + '.'.join(request.param.split('__'))
    return import_module(module_path)
    
