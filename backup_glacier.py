import cypher
import directory_resolver
import zipper
from argument_parser import ArgumentParser

OUTPUT_DIR = 'out'


def main():
    # Parse argument
    args = ArgumentParser()
    print 'Given arguments: {}'.format(args)

    # Arguments
    input_dir = args.input_dir()
    months_range = args.months_range()

    # Directories to backup
    dirs_to_backup = directory_resolver.list_directories(input_dir, months_range)
    print "Directories to backup:".format(dirs_to_backup)

    # Zip
    zips = zipper.zip_directories(input_dir, dirs_to_backup, OUTPUT_DIR)

    # Encrypt
    encrypted_files = cypher.encrypt_files(zips, '28iiKd7Z0oo92w996A7IpSz98DF1D47y')

    # verify file (decrypt, compare checksum with zip before encryption)

    # upload each zip to Glacier

    # mark (text file in directory) as 'backed-up'

    # clean up (delete encrypted package)


if __name__ == '__main__':
    main()
