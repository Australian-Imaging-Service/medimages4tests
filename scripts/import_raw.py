#!/usr/bin/env python3
from pathlib import Path
from argparse import ArgumentParser
from medimages4tests.import_tools import raw_pet_to_gen_code


if __name__ == "__main__":
    parser = ArgumentParser(
        description=(
            "Generates a module containing extracted metadata from a Siemens PET raw dataset"
            "in Python dictionaries so that a dummy dataset with similar "
            "header configuration can be generated in test fixtures"
        )
    )
    parser.add_argument(
        "raw_pet_file", help="The directory containing the source dicoms"
    )
    parser.add_argument(
        "fixture_file",
        help="The file to save the extracted header information and byte data in",
    )
    args = parser.parse_args()

    fpath = Path(args.fixture_file)

    with open(fpath, "w") as f:
        f.write(raw_pet_to_gen_code(Path(args.raw_pet_file), image_type=fpath.stem))
