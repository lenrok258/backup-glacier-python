import zipper

import directory_resolver
from argument_parser import ArgumentParser


def main():
    args = ArgumentParser()
    print 'Given arguments: {}'.format(args)
    input_dir = args.input_dir()

    dirs_to_backup = directory_resolver.list_directories(input_dir, args.months_range())
    print "Directories to backup:".format(dirs_to_backup)

    # zip each directory
    zips = zipper.zip_directories(input_dir, dirs_to_backup)

    # encrypt each zip

    # upload each zip to Glacier

    # mark (text file in directory) as 'backed-up'

    # clean up (delete encrypted package)


if __name__ == '__main__':
    main()
