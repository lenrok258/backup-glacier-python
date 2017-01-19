import json
import os

import cypher
import directory_resolver
import file_hash
import zipper
from argument_parser import ArgumentParser

OUTPUT_DIR = 'out'
OUTPUT_DIR_AWS_ARCHIVES_IDS = 'out-aws-archives-ids'
RESULT_FILE_NAME = 'aws-archive-info.json'


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

    # Directories to backup (=> list of ArchiveDirectory)
    archive_directory_list = directory_resolver.list_directories(input_dir, months_range)
    print "Directories to backup: {}".format(archive_directory_list)

    # Zip (=> list of ArchiveZip)
    archive_zip_list = zipper.zip_directories(archive_directory_list, OUTPUT_DIR)

    # Encrypt (=> list of ArchiveEnc)
    archive_enc_list = cypher.encrypt_files(archive_zip_list, enc_pass)

    # Verify encrypted file (decrypt, compare checksum with zip before encryption)
    __verify_encrypted_packages(archive_enc_list, enc_pass)

    # Upload each encrypted zip to Glacier
    __upload_files(archive_enc_list, aws_key, aws_secret, aws_region, aws_glacier_vault)

    # Put text file to source directory with Glacier Archive ID for further reference

    # clean up (delete OUTPUT_DIR content)


def __verify_encrypted_packages(archive_enc_list, password):
    for archive_enc in archive_enc_list:
        original_file_path = archive_enc.zip_path
        enc_file_path = archive_enc.enc_path
        print "Verifying file [{}]".format(enc_file_path)

        dec_file_path = cypher.decrypt_file(enc_file_path, password)
        original_file_hash = file_hash.hash_file(original_file_path)
        dec_file_hash = file_hash.hash_file(dec_file_path)

        if original_file_hash != dec_file_hash:
            raise Exception('Verification of file=[{}] failed!'.format(original_file_path))

        print "File [{}] verified".format(enc_file_path)


def __upload_files(archive_enc_list, aws_key, aws_secret, aws_region, aws_glacier_vault):
    for archive_enc in archive_enc_list:
        dir_name = archive_enc.dir_name
        dir_path = archive_enc.dir_path
        zip_path = archive_enc.zip_path
        enc_path = archive_enc.enc_path

        print "About to upload file [{}]".format(enc_path)
        # archive_id = aws_glacier.upload_file(enc_path, aws_key, aws_secret, aws_region, aws_glacier_vault)
        archive_id = "TETS"
        print "File uploaded. Archive id = {}".format(archive_id)
        print "About to put result file in directory {}".format(dir_path)
        __mark_directory_as_completed(dir_name, dir_path, zip_path, enc_path, archive_id)


def __mark_directory_as_completed(dir_name, dir_path, zip_path, enc_path, archive_id):
    zip_hash = file_hash.hash_file(zip_path)
    enc_hash = file_hash.hash_file(enc_path)
    file_content = {
        "dir_name": dir_name,
        "dir_path": dir_path,
        "zip_path": zip_path,
        "enc_path": enc_path,
        "zip_hash": zip_hash,
        "enc_hash": enc_hash,
        "aws_archive_id": archive_id}
    with open(os.path.join(dir_path, RESULT_FILE_NAME), 'w') as result_file:
        json.dump(file_content, result_file, indent=4)
    with open(os.path.join(OUTPUT_DIR_AWS_ARCHIVES_IDS, dir_name + '.json', ), 'w') as result_file:
        json.dump(file_content, result_file, indent=4)


if __name__ == '__main__':
    main()
1
