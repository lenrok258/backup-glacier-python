import argparse
import getpass
import re


class ArgumentName:
    # User input
    AWS_ACCESS_KEY_ID = 'AWS_ACCESS_KEY_ID'
    AWS_SECRET_ACCESS_KEY = 'AWS_SECRET_ACCESS_KEY'
    encryption_password = 'encryption_password'

    # Script parameters
    AWS_REGION = 'AWS_REGION'
    AWS_GLACIER_VAULT = 'AWS_GLACIER_VAULT'
    input_directory = 'input_directory'
    months_range = 'months_range'


class ArgumentParser:
    def __init__(self):
        parser = argparse.ArgumentParser(description='Backup media files to AWS Glacier')
        parser.add_argument(ArgumentName.AWS_REGION, help='Region to access Amazon Glacier')
        parser.add_argument(ArgumentName.AWS_GLACIER_VAULT, help='Amazon Glacier vault name')
        parser.add_argument(ArgumentName.input_directory, help='Input directory')
        parser.add_argument(ArgumentName.months_range, type=ArgumentParser.months_arg_checker,
                            help='Months range, e.g. 1-6 or 7-12')
        self.args = parser.parse_args()
        self.__ask_for_secrets()

    def __ask_for_secrets(self):
        aws_key = getpass.getpass(ArgumentName.AWS_ACCESS_KEY_ID + ": ")
        aws_secret = getpass.getpass(ArgumentName.AWS_SECRET_ACCESS_KEY + ": ")
        enc_pass = getpass.getpass(ArgumentName.encryption_password + ": ")

        setattr(self, ArgumentName.AWS_ACCESS_KEY_ID, aws_key)
        setattr(self, ArgumentName.AWS_SECRET_ACCESS_KEY, aws_secret)
        setattr(self, ArgumentName.encryption_password, enc_pass)

    def aws_key_id(self):
        return getattr(self, ArgumentName.AWS_ACCESS_KEY_ID)

    def aws_secret(self):
        return getattr(self, ArgumentName.AWS_SECRET_ACCESS_KEY)

    def encryption_pass(self):
        return getattr(self, ArgumentName.encryption_password)

    def aws_region(self):
        return getattr(self.args, ArgumentName.AWS_REGION)

    def aws_glacier_name(self):
        return getattr(self.args, ArgumentName.AWS_GLACIER_VAULT)

    def input_dir(self):
        return getattr(self.args, ArgumentName.input_directory)

    def months_range(self):
        return getattr(self.args, ArgumentName.months_range)

    def __str__(self):
        return str(self.args)

    @staticmethod
    def months_arg_checker(months_arg):
        try:
            return re.match("^[01]?[0-9]{1}-[01]?[0-9]{1}$", months_arg).group(0)
        except:
            raise argparse.ArgumentTypeError("String '{}' does not match required format".format(months_arg))
