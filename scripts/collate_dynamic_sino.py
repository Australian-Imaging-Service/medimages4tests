from pathlib import Path
from collections import defaultdict
from importlib import import_module


def collate_dynamic_sinograms(dpath: Path, image_type: str):
    """Return

    Parameters
    ----------
    dpath : Path
        Path to the directory holding the DICOM files
    image_type : str
        Name of the image type, used to name the generator that derives the
        image

    Returns
    -------
    str
        Python code that generates a version of the imported image with
        dummy data.
    """
    collated_hdr = defaultdict(dict)
    collated_data = defaultdict(dict)
    num_vols = 0
    for i, fpath in enumerate(dpath.iterdir()):
        if fpath.name.startswith("."):
            continue
        header, data = read_dicom(fpath)
        for k, v in header.items():
            collated_hdr[k][i] = v
        for k, v in data.items():
            collated_data[k][i] = v
        num_vols += 1
    constant_hdr = {
        k: v[0]
        for k, v in collated_hdr.items()
        if (len(v) == num_vols and all(v[0] == x for x in v.values()))
    }
    varying_hdr = {k: v for k, v in collated_hdr.items() if k not in constant_hdr}

    constant_hdr.update(ANONYMOUS_TAGS)

    return DICOM_FILE_TEMPLATE.format(
        num_vols=num_vols,
        image_type=image_type,
        constant_hdr=json.dumps(constant_hdr, indent="    "),
        varying_hdr=json.dumps(varying_hdr),
        collated_data=json.dumps(collated_data),
    )
