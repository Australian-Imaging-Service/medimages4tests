from pathlib import Path
import numpy as np
import nibabel as nb


def sample_image(
    out_file: Path,
    data: np.ndarray = None,
    vox_sizes=(1.0, 1.0, 1.0),
    qform=(1, 2, 3, 1),
):
    """Create a random Nifti file to satisfy BIDS parsers"""
    if data is None:
        data = np.random.randint(0, 1, size=[10, 10, 10])
    hdr = nb.Nifti1Header()
    hdr.set_data_shape(data.shape)
    hdr.set_zooms(vox_sizes)  # set voxel size
    hdr.set_xyzt_units(2)  # millimeters
    hdr.set_qform(np.diag(qform))
    nb.save(
        nb.Nifti1Image(
            data,
            hdr.get_best_affine(),
            header=hdr,
        ),
        out_file,
    )
