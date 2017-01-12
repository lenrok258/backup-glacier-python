import cypher
import directory_resolver
import file_hash
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
    enc_pass = args.encryption_pass()

    # Directories to backup
    dirs_to_backup = directory_resolver.list_directories(input_dir, months_range)
    print "Directories to backup:".format(dirs_to_backup)

    # Zip
    zips = zipper.zip_directories(input_dir, dirs_to_backup, OUTPUT_DIR)

    # Encrypt
    encrypted_files = cypher.encrypt_files(zips, enc_pass)

    # verify file (decrypt, compare checksum with zip before encryption)
    __verify_encrypted_packages(encrypted_files, enc_pass)

    # upload each zip to Glacier

    # mark (text file in directory) as 'backed-up'

    # clean up (delete encrypted package)


def __verify_encrypted_packages(encrypted_files, password):
    for file_tuple in encrypted_files:
        original_file_path = file_tuple[0]
        enc_file_path = file_tuple[1]
        dec_file_path = cypher.decrypt_file(enc_file_path, password)

        original_file_hash = file_hash.hash_file(original_file_path)
        dec_file_hash = file_hash.hash_file(dec_file_path)

        if original_file_hash != dec_file_hash:
            raise Exception('Verification for file=<<{}>> failed!'.format(original_file_path))


if __name__ == '__main__':
    main()
