import pytest
from medimages4tests.utils import retrieve_from_github
from fileformats.medimage import NiftiGz


@pytest.mark.xfail
def test_github_retrieve():

    path = retrieve_from_github(
        org="nipype", repo="pydra-fsl-testdata", path="melodic_ica"
    )
    nifti = NiftiGz(path)

    assert nifti.shape == (204, 256, 256)
