import aws_glacier
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
    aws_key = args.aws_key_id()
    aws_secret = args.aws_secret()
    aws_region = args.aws_region()
    aws_glacier_vault = args.aws_glacier_name()

    # Directories to backup
    dirs_to_backup = directory_resolver.list_directories(input_dir, months_range)
    print "Directories to backup:".format(dirs_to_backup)

    # Zip (=> list of zipped files paths)
    zips = zipper.zip_directories(input_dir, dirs_to_backup, OUTPUT_DIR)

    # Encrypt (=> tuple(original_file_path, enc_file_path)
    encrypted_files_tuples = cypher.encrypt_files(zips, enc_pass)

    # Verify encrypted file (decrypt, compare checksum with zip before encryption)
    __verify_encrypted_packages(encrypted_files_tuples, enc_pass)

    # Upload each encrypted zip to Glacier
    aws_glacier.upload_files(__get_enc_files(encrypted_files_tuples), aws_key, aws_secret, aws_region, aws_glacier_vault)

    # mark (text file in directory) as 'backed-up'

    # clean up (delete encrypted package)


def __verify_encrypted_packages(encrypted_files_tuples, password):
    for files_tuple in encrypted_files_tuples:
        original_file_path = files_tuple[0]
        enc_file_path = files_tuple[1]
        print "Verifying file [{}]".format(enc_file_path)

        dec_file_path = cypher.decrypt_file(enc_file_path, password)
        original_file_hash = file_hash.hash_file(original_file_path)
        dec_file_hash = file_hash.hash_file(dec_file_path)

        if original_file_hash != dec_file_hash:
            raise Exception('Verification of file=[{}] failed!'.format(original_file_path))

        print "File [{}] verified".format(enc_file_path)


def __get_enc_files(encrypted_files_tuples):
    return map(lambda tuple: tuple[1], encrypted_files_tuples)


if __name__ == '__main__':
    main()
