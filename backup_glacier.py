import os
from zipfile import ZipFile

import directory_resolver
from argument_parser import ArgumentParser


def main():
    args = ArgumentParser()
    print 'Given arguments: {}'.format(args)
    input_dir = args.input_dir()

    dirs_to_backup = directory_resolver.list_directories(input_dir, args.months_range())
    print "Directories to backup:".format(dirs_to_backup)

    # zip each directory
    for dir_name in dirs_to_backup:
        path_to_backup = os.path.join(input_dir, dir_name)
        print "About to zip directory: {}".format(path_to_backup)
        zip_file_name = "{}.zip".format(dir_name)
        with ZipFile(zip_file_name, 'w') as zip_file:
            for root, dirs, files in os.walk(path_to_backup):
                for file in files:
                    zip_file.write(os.path.join(root, file))
        print "Directory zipped: {}".format(zip_file_name)

    # encrypt each zip

    # upload each zip to Glacier

    # mark (text file in directory) as 'backed-up'

    # clean up (delete encrypted package)


if __name__ == '__main__':
    main()
