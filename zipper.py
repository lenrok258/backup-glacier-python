import os
from zipfile import ZipFile


def zip_directories(dirs_path, dirs_names_list):
    zips = list()
    for dir_name in dirs_names_list:
        path_to_backup = os.path.join(dirs_path, dir_name)
        zip_file_name = __compute_zip_name(dir_name)
        zips.append(zip_file_name)
        __create_zip(path_to_backup, zip_file_name)
    return zips


def __compute_zip_name(dir_name):
    zip_file_name = "{}.zip".format(dir_name)
    return zip_file_name


def __create_zip(path_to_backup, zip_file_name):
    print "About to zip directory: {}".format(path_to_backup)
    with ZipFile(zip_file_name, 'w') as zip_file:
        for root, dirs, files in os.walk(path_to_backup):
            for file in files:
                zip_file.write(os.path.join(root, file))
    print "Directory zipped: {}".format(zip_file_name)
