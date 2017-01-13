import os

import boto3


def upload_files(file_paths_list, aws_key, aws_secret, aws_region, aws_glacier_vault):
    client = __create_glacier_client(aws_key, aws_region, aws_secret)
    __set_retrieval_policy_to_free_tier_only(client)

    for file_path in file_paths_list:
        with open(file_path, 'rb') as file:
            print "About to upload file [{}]".format(file.name)
            __upload_file(client, file, aws_glacier_vault)


def __create_glacier_client(aws_key, aws_region, aws_secret):
    client = boto3.client('glacier',
                          region_name=aws_region,
                          aws_access_key_id=aws_key,
                          aws_secret_access_key=aws_secret)
    return client


def __set_retrieval_policy_to_free_tier_only(client):
    client.set_data_retrieval_policy(Policy={
        'Rules': [
            {
                'Strategy': 'FreeTier'
            },
        ]
    })


def __upload_file(client, file, aws_glacier_vault):
    client.upload_archive(vaultName=aws_glacier_vault,
                          archiveDescription=os.path.basename(file.name),
                          body=file)
