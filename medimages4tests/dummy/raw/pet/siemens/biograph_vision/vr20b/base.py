import typing as ty
from pathlib import Path
import random
from datetime import datetime
from tempfile import mkdtemp
import string
import pydicom

MAGIC_NUMBER = b"LARGE_PET_LM_RAWDATA"

FILENAME_TEMPLATE = "{last_name}_{first_name}.PT.{acquisition_id}.{scan_id}.{image_type}.{date_time}.2.0.{timestamp}.ptd"

DEFAULT_SCAN_DATE = datetime(2023, 8, 25, 15, 50, 5, 123456)

# raw_data_files = [
#     ,
#     "{last_name}_{first_name}.PT.PET_U_FDG_SWB_LM_(Adult).602.PET_CALIBRATION.{date_time}.080000.2.0.52858842.ptd",
#     "{last_name}_{first_name}.PT.PET_U_FDG_SWB_LM_(Adult).602.PET_COUNTRATE.{date_time}.083000.2.0.52858872.ptd",
#     "{last_name}_{first_name}.PT.PET_U_FDG_SWB_LM_(Adult).602.PET_LISTMODE.{date_time}.080000.2.0.52858858.ptd",
#     "{last_name}_{first_name}.PT.PET_U_FDG_SWB_LM_(Adult).603.PET_CALIBRATION.{date_time}.30.115000.2.0.54764603.ptd",
#     "{last_name}_{first_name}.PT.PET_U_FDG_SWB_LM_(Adult).603.PET_EM_SINO.{date_time}.30.118000.2.0.54764616.ptd",
#     "{last_name}_{first_name}.PT.PET_U_FDG_SWB_LM_(Adult).603.PET_REPLAY_PARAM.{date_time}.30.118000.2.0.54764627.ptd",
# ]


def generate_raw_data(
    dicom_hdr_fspath: Path,
    out_dir: ty.Optional[Path] = None,
    scan_id: int = 602,
    acquisition_id: str = "PET_U_FDG_SWB_LM_(Adult)",
    date_time: datetime = DEFAULT_SCAN_DATE,
):
    dcm_hdr_bytes = dicom_hdr_fspath.read_bytes()
    dcm = pydicom.dcmread(dicom_hdr_fspath)
    if out_dir is None:
        out_dir = Path(mkdtemp())
    if not out_dir.exists():
        out_dir.mkdir(parents=True)

    # 4 bytes for the int that holds the length of the header
    header_offset = len(dcm_hdr_bytes) + len(MAGIC_NUMBER) + 4
    fname = FILENAME_TEMPLATE.format(
        last_name=dcm.PatientName.family_name,
        first_name=dcm.PatientName.given_name,
        scan_id=scan_id,
        acquisition_id=acquisition_id,
        date_time=date_time.strftime("%Y.%m.%d.%H.%M.%S.%f"),
        image_type=dcm.ImageType[-1],
        timestamp="".join(random.choices(string.digits, k=8)),
    )
    fspath = out_dir / fname
    fspath.write_bytes(
        f"dummy data for {fname}\n".encode()
        + dcm_hdr_bytes
        + header_offset.to_bytes(4, "little")
        + MAGIC_NUMBER
    )
    return [fspath]
