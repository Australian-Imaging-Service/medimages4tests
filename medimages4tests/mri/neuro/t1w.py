from tempfile import mkdtemp
import shutil
from pathlib import Path
import openneuro
from medimages4tests import base_cache_dir
from ..neuro import OpenneuroSpec


cache_dir = base_cache_dir / "mri" / "neuro" / "t1w"


SAMPLES = {
    "ds004130-ON01016": OpenneuroSpec(
        dataset="ds004130",
        tag="1.0.0",
        path="sub-ON01016/anat/sub-ON01016_acq-fspgr_run-01_T1w",
    )
}


def get_image(sample_name):
    sample = SAMPLES[sample_name]
    if cache_dir.exists():
        cache_dir.mkdir(parents=True)
    out_path = (cache_dir / sample_name).with_suffix(".nii.gz")
    if not out_path.exists():
        tmpdir = Path(mkdtemp())
        openneuro.download(
            dataset=sample.dataset,
            tag=sample.tag,
            target_dir=tmpdir,
            include=[sample.path],
        )
        for ext in (".nii.gz", ".json"):
            shutil.copyfile(
                (tmpdir / sample.path).with_suffix(ext)
                (cache_dir / sample_name).with_suffix(ext)
            )
    return out_path
