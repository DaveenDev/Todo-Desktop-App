import zipfile
import pathlib

def make_archive(filepaths, dest_dir):
    dirpath = pathlib.Path(dest_dir,"comppressed.zip")
    with zipfile.ZipFile(dirpath, 'w') as archive:
        for filepath in filepaths:
            filepath = pathlib.Path(filepath)
            archive.write(filepath, arcname=filepath.name)

