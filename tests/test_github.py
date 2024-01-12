from medimages4tests.utils import retrieve_from_github


def test_github_retrieve():

    path = retrieve_from_github(org="nipype", repo="pydra-fsl-testdata", path="melodic_ica")

    assert nifti.shape == (204, 256, 256)
