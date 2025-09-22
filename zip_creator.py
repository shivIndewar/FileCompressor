import zipfile
import pathlib

def compress_file(file_paths, destination_folder):
    dest_path = pathlib.Path(destination_folder,"compressed.zip")
    with zipfile.ZipFile(dest_path, "w") as zip_file:
        for file_path in file_paths:
            file_path = pathlib.Path(file_path)
            zip_file.write(file_path, arcname=file_path.name)
