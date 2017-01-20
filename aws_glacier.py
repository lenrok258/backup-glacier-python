import os

import boto3


def upload_file(file_path, aws_key, aws_secret, aws_region, aws_glacier_vault):
    client = __create_glacier_client(aws_key, aws_secret, aws_region)
    resource = __create_glacier_resource(aws_key, aws_secret, aws_region)
    __set_retrieval_policy_to_free_tier_only(client)
    return __upload_file(resource, file_path, aws_glacier_vault)


def retrieve_archive(archive_id, aws_key, aws_secret, aws_region, aws_glacier_vault):
    pass


def __create_glacier_client(aws_key, aws_secret, aws_region):
    return boto3.client('glacier',
                        aws_access_key_id=aws_key,
                        aws_secret_access_key=aws_secret,
                        region_name=aws_region)


def __create_glacier_resource(aws_key, aws_secret, aws_region):
    # return boto_glacier.Layer2(aws_access_key_id=aws_key,
    #                            aws_secret_access_key=aws_secret,
    #                            region_name=aws_region)
    return boto3.resource('glacier',
                          aws_access_key_id=aws_key,
                          aws_secret_access_key=aws_secret,
                          region_name=aws_region)


def __set_retrieval_policy_to_free_tier_only(client):
    client.set_data_retrieval_policy(Policy={
        'Rules': [
            {
                'Strategy': 'FreeTier'
            },
        ]
    })


def __upload_file(glacier_resource, file_path, aws_glacier_vault):
    vault = glacier_resource.Vault('-', aws_glacier_vault)
    description = os.path.basename(file_path)
    archive = vault.upload_archive(body=file_path, archiveDescription=description)
    return archive
