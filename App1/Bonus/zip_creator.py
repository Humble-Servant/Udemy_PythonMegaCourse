import zipfile
import pathlib

def make_archive(filepaths, dest_dir):
    dest_path = pathlib.Path(dest_dir, "compressed.zip")
    print(dest_path)
    with zipfile.ZipFile(dest_path, 'w') as archive:
        for filepath in filepaths:
            filepath = pathlib.Path(filepath)
            archive.write(filepath, arcname=filepath.name)


if __name__ == '__main__':
    make_archive(filepaths=['App1/Bonus/bonus5.py', 'App1/Bonus/bonus7.py'], dest_dir='App1/Bonus/dest')