import argparse
import re

def __months_arg_checker(months_arg):
    try:
        return re.match("^[01]?[0-9]{1}-[01]?[0-9]{1}$", months_arg).group(0)
    except:
        raise argparse.ArgumentTypeError("String '{}' does not match required format".format(months_arg))

def parse_args():
    parser = argparse.ArgumentParser(description='Backup media files to AWS Glacier')
    parser.add_argument('AWS_ACCESS_KEY_ID', help='Access key to access Amazon Glacier')
    parser.add_argument('AWS_SECRET_ACCESS_KEY', help='Secret key to access Amazon Glacier')
    parser.add_argument('AWS_DEFAULT_REGION', help='Region to access Amazon Glacier')
    parser.add_argument('encryption_password', help='Password to use to encrypt zip packages')
    parser.add_argument('input_directory', help='Input directory')
    parser.add_argument('months_range', type=__months_arg_checker, help='Months range, e.g. 1-6 or 7-12')
    return parser.parse_args()