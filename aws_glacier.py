import os
from time import sleep

import boto3

import progress_bar

__DOWNLOAD_PARTIAL_SIZE_B = 8


def upload_file(file_path, aws_key, aws_secret, aws_region, aws_glacier_vault):
    client = __create_glacier_client(aws_key, aws_secret, aws_region)
    resource = __create_glacier_resource(aws_key, aws_secret, aws_region)
    __set_retrieval_policy_to_free_tier_only(client)
    return __upload_file(resource, file_path, aws_glacier_vault)


def initiate_archive_retrieval(archive_id, aws_key, aws_secret, aws_region, aws_glacier_vault):
    resource = __create_glacier_resource(aws_key, aws_secret, aws_region)
    archive = resource.Archive('-', aws_glacier_vault, archive_id)
    print "JOB_ID: {}".format(archive.initiate_archive_retrieval())


def get_job(job_id, aws_key, aws_secret, aws_region, aws_glacier_vault):
    resource = __create_glacier_resource(aws_key, aws_secret, aws_region)
    job = resource.Job('-', aws_glacier_vault, job_id)
    print "JOB STATUS: {}".format(job.status_code)

    output = job.get_output()
    archive_size_b = job.archive_size_in_bytes
    print "OUTPUT: {}".format(output)

    with open('output.test.txt', 'w+') as output_file:
        body_stream = output['body']
        stream_tile = body_stream.read(amt=__DOWNLOAD_PARTIAL_SIZE_B)
        downloaded_b = len(stream_tile)
        while stream_tile:
            # progress_bar.printProgress(downloaded_b, archive_size_b)
            output_file.write(stream_tile)
            stream_tile = output['body'].read(amt=__DOWNLOAD_PARTIAL_SIZE_B)
            downloaded_b += len(stream_tile)
            # sleep(0.1)
        body_stream.close()


def __create_glacier_client(aws_key, aws_secret, aws_region):
    return boto3.client('glacier',
                        aws_access_key_id=aws_key,
                        aws_secret_access_key=aws_secret,
                        region_name=aws_region)


def __create_glacier_resource(aws_key, aws_secret, aws_region):
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
    with open(file_path, 'r') as file_to_backup:
        return vault.upload_archive(body=file_to_backup, archiveDescription=description)


if __name__ == '__main__':
    get_job(
        '',
        '',
        '',
        'us-west-2',
        'test-vault'
    )
