import tempfile
from pathlib import Path
from medimages4tests.dummy.raw.pet.siemens.biograph_vision.vr20b.PET_LISTMODE import (
    get_image,
)
from fileformats.medimage import Vnd_Siemens_Biograph128Vision_Vr20b_PetListMode

out_dir = Path(tempfile.mkdtemp())

# Generate raw PET data files
fspaths = get_image(out_dir)

list_mode_file = Vnd_Siemens_Biograph128Vision_Vr20b_PetListMode(fspaths)

assert list_mode_file.metadata["PatientName"] == "FirstName^LastName"
