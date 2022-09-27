import nibabel as nb
import gzip
import shutil
from medimages4tests.nifti import sample_image


def test_nifti():

    nifti_fpath = sample_image()

    nifti = nb.load(nifti_fpath)

    assert nifti.get_header()["dim"][:4] == [3, 10, 10, 10]


def test_nifti_compressed(work_dir):

    gz_fpath = sample_image(compressed=True)
    uncompressed_fpath = work_dir / "nifti.nii"

    with gzip.open(gz_fpath, 'rb') as f_in:
        with open(uncompressed_fpath, 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)
    nifti = nb.load(uncompressed_fpath)

    assert nifti.get_header()["dim"][:4] == [3, 10, 10, 10]
