import gzip
import shutil
import nibabel as nb
import numpy as np
from medimages4tests.dummy.nifti import get_image


def test_nifti(work_dir):

    nifti_fpath = get_image(work_dir / "sample.nii")

    nifti = nb.load(nifti_fpath)

    assert isinstance(nifti, nb.nifti1.Nifti1Image)
    assert not isinstance(nifti, nb.nifti2.Nifti2Image)
    assert np.array_equal(nifti.header["dim"][:4], [3, 10, 10, 10])


def test_nifti_compressed(work_dir):

    gz_fpath = get_image(work_dir / "sample.nii.gz", compressed=True)
    uncompressed_fpath = work_dir / "nifti.nii"

    with gzip.open(gz_fpath, 'rb') as f_in:
        with open(uncompressed_fpath, 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)
    nifti = nb.load(uncompressed_fpath)

    assert np.array_equal(nifti.header["dim"][:4], [3, 10, 10, 10])


def test_nifti2(work_dir):

    nifti_fpath = get_image(work_dir / "sample2.nii", nifti_version_2=True)

    nifti = nb.load(nifti_fpath)

    # We cannot test if the nifti2 is not a nifti1 as the nibabel nifti2 inherits from nifti1
    assert isinstance(nifti, nb.nifti2.Nifti2Image)
    assert np.array_equal(nifti.header["dim"][:4], [3, 10, 10, 10])

    nifti_gz_fpath = get_image(work_dir / "sample2.nii.gz", compressed=True, nifti_version_2=True)
    nifti_gz = nb.load(nifti_gz_fpath)

    assert isinstance(nifti_gz, nb.nifti2.Nifti2Image)
    assert np.array_equal(nifti_gz.header["dim"][:4], [3, 10, 10, 10])
