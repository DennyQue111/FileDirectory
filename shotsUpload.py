from pathlib import Path
import shutil
import os

source_files_path = input("Enter the path of your movs: ")
target_files_path = input("Enter the path of your movs going to move to: ")
source_files = Path(source_files_path)
target_files = Path(target_files_path)

for file in source_files.iterdir():
    if file.name != '.DS_Store' and file.is_file():

        old_name = file.stem
        VFXshot, shotcode, version = old_name.split('_')

        new_path = target_files.joinpath(VFXshot)
        if not new_path.exists():
            new_path.mkdir()

        new_file_path = new_path.joinpath(VFXshot)

        newnew_path_name = f'{VFXshot}_{shotcode}'

        newnew_path = new_path.joinpath(newnew_path_name)
        if not newnew_path.exists():
            newnew_path.mkdir()

        newnew_file_path = newnew_path.joinpath(newnew_path_name)

        newnewnew_path_name = ("comp")

        newnewnew_path = newnew_path.joinpath(newnewnew_path_name)
        if not newnewnew_path.exists():
            newnewnew_path.mkdir()

        newnewnew_file_path = newnew_path.joinpath(newnewnew_path_name)

        shutil.copy(file, newnewnew_file_path)
        print("Succeed!")
