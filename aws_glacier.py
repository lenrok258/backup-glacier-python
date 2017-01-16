import os

import boto.glacier.layer2 as boto_glacier
import boto3


def upload_files(file_paths_list, aws_key, aws_secret, aws_region, aws_glacier_vault):
    client = __create_glacier_client(aws_key, aws_region, aws_secret)
    layer2 = __create_glacier_layer2()
    __set_retrieval_policy_to_free_tier_only(client)

    for file_path in file_paths_list:
        print "About to upload file [{}]".format(file_path)
        archive_id = __upload_file(layer2, file_path, aws_glacier_vault)
        print "File uploaded. Archive id = {}".format(archive_id)


def __create_glacier_client(aws_key, aws_secret, aws_region):
    client = boto3.client(aws_access_key_id=aws_key,
                          aws_secret_access_key=aws_secret,
                          region_name=aws_region)
    return client


def __create_glacier_layer2(aws_key, aws_secret, aws_region):
    layer2 = boto_glacier.Layer2(aws_access_key_id=aws_key,
                                 aws_secret_access_key=aws_secret,
                                 region_name=aws_region)
    return layer2


def __set_retrieval_policy_to_free_tier_only(client):
    client.set_data_retrieval_policy(Policy={
        'Rules': [
            {
                'Strategy': 'FreeTier'
            },
        ]
    })


def __upload_file(layer2, file_path, aws_glacier_vault):
    vault = layer2.get_vault(aws_glacier_vault)
    description = os.path.basename(file_path)
    return vault.upload_archive(file_path, description)
