from pathlib import Path
import shutil
from copy import copy
import pydicom.dataset


cache_dir = Path.home() / '.medimage4tests ' / 'cache' / 'dicom'


def generate_test_dicom(path: str, num_vols: int, constant_hdr: dict,
                        collated_data: dict, varying_hdr: dict):
    """Generates a dummy DICOM dataset for a test fixture

    Parameters
    ----------
    path : str
        Path (name) for the generated Dicom object
    num_vols : int
        Number of volumes in the set
    constant_hdr : dict[str, Any]
        constant header values
    collated_data : dict[str, int]
        data array lengths
    varying_hdr : dict[str, list], optional
        varying header values across a multi-volume set

    Returns
    -------
    Dicom
        Dicom dataset
    """

    dicom_dir = cache_dir / path

    if not dicom_dir.exists():  # Check for cached version
        dicom_dir.mkdir(parents=True)

        try:
            for i in range(num_vols):
                i = str(i)
                vol_json = copy(constant_hdr)
                if varying_hdr is not None:
                    vol_json.update({k: v[i] for k, v in varying_hdr.items() if i in v})
                # Reconstitute large binary fields with dummy data filled with \3 bytes
                vol_json.update({k: {'vr': v[i]['vr'],
                                     'InlineBinary': "X" * v[i]['BinaryLength']}
                                for k, v in collated_data.items() if i in v})

                ds = pydicom.dataset.Dataset.from_json(vol_json)
                ds.is_implicit_VR = True
                ds.is_little_endian = True

                ds.save_as(dicom_dir / f"{i}.dcm")
        except:
            shutil.rmtree(dicom_dir)  # Remove directory from cache on error
            raise

    return dicom_dir
