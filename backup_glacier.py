import cypher
import directory_resolver
import zipper
from argument_parser import ArgumentParser


def main():
    args = ArgumentParser()
    print 'Given arguments: {}'.format(args)

    input_dir = args.input_dir()
    months_range = args.months_range()

    dirs_to_backup = directory_resolver.list_directories(input_dir, months_range)
    print "Directories to backup:".format(dirs_to_backup)

    # zip each directory
    zips = zipper.zip_directories(input_dir, dirs_to_backup)

    # encrypt each zip
    for zip_file_path in zips:
        print "Encrypting {}".format(zip_file_path)
        with open(zip_file_path, 'rb') as in_file, open(zip_file_path + '_enc', 'wb') as out_file:
            cypher.encrypt(in_file, out_file, '28iiKd7Z0oo92w996A7IpSz98DF1D47y')


    # verify file (decrypt, compare checksum with zip before encryption)

    # upload each zip to Glacier

    # mark (text file in directory) as 'backed-up'

    # clean up (delete encrypted package)


if __name__ == '__main__':
    main()
