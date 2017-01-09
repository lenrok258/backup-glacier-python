import argparse
import re


class ArgumentName:
    AWS_ACCESS_KEY_ID = 'AWS_ACCESS_KEY_ID'
    AWS_SECRET_ACCESS_KEY = 'AWS_SECRET_ACCESS_KEY'
    AWS_DEFAULT_REGION = 'AWS_DEFAULT_REGION'
    encryption_password = 'encryption_password'
    input_directory = 'input_directory'
    months_range = 'months_range'


class ArgumentParser:
    def __init__(self):
        parser = argparse.ArgumentParser(description='Backup media files to AWS Glacier')
        parser.add_argument(ArgumentName.AWS_ACCESS_KEY_ID, help='Access key to access Amazon Glacier')
        parser.add_argument(ArgumentName.AWS_SECRET_ACCESS_KEY, help='Secret key to access Amazon Glacier')
        parser.add_argument(ArgumentName.AWS_DEFAULT_REGION, help='Region to access Amazon Glacier')
        parser.add_argument(ArgumentName.encryption_password, help='Password to use to encrypt zip packages')
        parser.add_argument(ArgumentName.input_directory, help='Input directory')
        parser.add_argument(ArgumentName.months_range, type=ArgumentParser.months_arg_checker,
                            help='Months range, e.g. 1-6 or 7-12')
        self.args = parser.parse_args()

    def aws_key_id(self):
        return getattr(self.args, ArgumentName.AWS_ACCESS_KEY_ID)

    def aws_secret(self):
        return getattr(self.args, ArgumentName.AWS_SECRET_ACCESS_KEY)

    def aws_region(self):
        return getattr(self.args, ArgumentName.AWS_DEFAULT_REGION)

    def encryption_pass(self):
        return getattr(self.args, ArgumentName.encryption_password)

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
