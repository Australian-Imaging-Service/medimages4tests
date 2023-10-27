from pathlib import Path
from tempfile import mkdtemp


raw_data_files = [
    "TESTNAME_GePhantom.PT.PET_U_FDG_SWB_LM_(Adult).602.PETCT_SPL.2023.08.25.15.50.51.065000.2.0.52858823.ptd",
    "TESTNAME_GePhantom.PT.PET_U_FDG_SWB_LM_(Adult).602.PET_CALIBRATION.2023.08.25.15.50.51.080000.2.0.52858842.ptd",
    "TESTNAME_GePhantom.PT.PET_U_FDG_SWB_LM_(Adult).602.PET_COUNTRATE.2023.08.25.15.50.51.083000.2.0.52858872.ptd",
    "TESTNAME_GePhantom.PT.PET_U_FDG_SWB_LM_(Adult).602.PET_LISTMODE.2023.08.25.15.50.51.080000.2.0.52858858.ptd",
    "TESTNAME_GePhantom.PT.PET_U_FDG_SWB_LM_(Adult).603.PET_CALIBRATION.2023.08.25.15.54.30.115000.2.0.54764603.ptd",
    "TESTNAME_GePhantom.PT.PET_U_FDG_SWB_LM_(Adult).603.PET_EM_SINO.2023.08.25.15.54.30.118000.2.0.54764616.ptd",
    "TESTNAME_GePhantom.PT.PET_U_FDG_SWB_LM_(Adult).603.PET_REPLAY_PARAM.2023.08.25.15.54.30.118000.2.0.54764627.ptd",
]

def get_raw_data_files(out_dir=None):
    if out_dir is None:
        out_dir = Path(mkdtemp())
    fspaths = []
    for fname in raw_data_files:
        fspath = out_dir / fname
        fspath.write_bytes(f"dummy data for {fname}".encode())
        fspaths.append(fspath)
    return fspaths
