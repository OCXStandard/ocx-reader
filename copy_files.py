#  Copyright (c) 2024. #  OCX Consortium https://3docx.org. See the LICENSE

from pathlib import Path
import shutil
from shutil import SameFileError
from ocx_common.utilities import SourceValidator, SourceError

def copy_block(block: str):
    try:
        folder =  'C:/Users/oca/OneDrive - DNV/Git_Repos/TestModels/Latest/NAPA/_Customer/VARD/2024.05.12/N973_MidShip_OCX/N973_MidShip_STP'
        destination ='C:/Users/oca/OneDrive - DNV/Git_Repos/TestModels/Latest/NAPA/_Customer/VARD/2024.05.12/novorender'
        if not SourceValidator.is_directory(destination):
            SourceValidator.mkdir(destination)
        SourceValidator.mkdir(str(Path(destination).joinpath(block)))
        count = 0
        if SourceValidator.is_directory(folder) and SourceValidator.is_directory(destination):
            for dir in Path(folder).iterdir():
                if dir.is_dir():
                    files = Path(dir).glob(pattern='**/*.stp')
                    print(f'{len(list(files))} files in folder {dir.name}')
                    for file in Path(dir).glob(pattern='**/*.stp'):
                        name = file.name
                        copy_file = Path(destination).joinpath(block) / name
                        copy = shutil.copy(file, copy_file)
                        print(f'Copied {file} to {copy_file}')
                        count += 1
        print(f'Copied {count} files')
    except (SourceError, SameFileError) as e:
        print(e)

copy_block(block = 'N973_MidShip_OCX')
