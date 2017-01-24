import os
from zipfile import ZipFile


class ArchiveZip:
    def __init__(self, dir_name, dir_path, zip_path):
        self.dir_name = dir_name
        self.dir_path = dir_path
        self.zip_path = zip_path


def zip_directories(archive_directory_list, output_dir):
    zips = list()
    for archive_directory in archive_directory_list:
        dir_name = archive_directory.dir_name
        path_to_backup = archive_directory.dir_path

        zip_file_path = __compute_zip_path(dir_name, output_dir)
        zips.append(ArchiveZip(dir_name, path_to_backup, zip_file_path))
        __create_zip(path_to_backup, zip_file_path)
    return zips


def __compute_zip_path(dir_name, output_dir):
    zip_file_path = "{}/{}.zip".format(output_dir, dir_name)
    return zip_file_path


def __create_zip(path_to_backup, zip_file_path):
    print "About to zip directory: [{}]".format(path_to_backup)
    with ZipFile(zip_file_path, 'w', allowZip64=True) as zip_file:
        for root, dirs, files in os.walk(path_to_backup):
            for file in files:
                zip_file.write(os.path.join(root, file))
    print "Directory zipped: [{}]".format(zip_file_path)
