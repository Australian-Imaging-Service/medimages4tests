import tempfile
from pathlib import Path


def test_dicom_creation(dicom_module):

    out_dir = Path(tempfile.mkdtemp())

    # Generate DICOM files
    dicom_module.sample_image(out_dir)

    assert len(list(out_dir.glob('*.dcm'))) == dicom_module.num_vols
