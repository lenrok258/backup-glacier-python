import argparse
import re


class ArgumentName:
    AWS_ACCESS_KEY_ID = 1
    AWS_SECRET_ACCESS_KEY = 2
    AWS_DEFAULT_REGION = 3
    encryption_password = 4
    input_directory = 5
    months_range = 6


class ArgumentParser:
    def __init__(self):
        parser = argparse.ArgumentParser(description='Backup media files to AWS Glacier')
        parser.add_argument(ArgumentName.AWS_ACCESS_KEY_ID, help='Access key to access Amazon Glacier')
        parser.add_argument(ArgumentName.AWS_SECRET_ACCESS_KEY, help='Secret key to access Amazon Glacier')
        parser.add_argument(ArgumentName.AWS_DEFAULT_REGION, help='Region to access Amazon Glacier')
        parser.add_argument(ArgumentName.encryption_password, help='Password to use to encrypt zip packages')
        parser.add_argument(ArgumentName.input_directory, help='Input directory')
        parser.add_argument(ArgumentName.months_range, type=ArgumentParser.__months_arg_checker,
                            help='Months range, e.g. 1-6 or 7-12')
        self.args = parser.parse_args()

    def aws_key_id(self):
        return self.args[ArgumentName.AWS_ACCESS_KEY_ID]

    def aws_secret(self):
        return self.args[ArgumentName.AWS_SECRET_ACCESS_KEY]

    def aws_region(self):
        return self.args[ArgumentName.AWS_DEFAULT_REGION]

    def encryption_pass(self):
        return self.args[ArgumentName.encryption_password]

    def input_dir(self):
        return self.args[ArgumentName.input_directory]

    def months_range(self):
        return self.args[ArgumentName.months_range]

    @staticmethod
    def __months_arg_checker(months_arg):
        try:
            return re.match("^[01]?[0-9]{1}-[01]?[0-9]{1}$", months_arg).group(0)
        except:
            raise argparse.ArgumentTypeError("String '{}' does not match required format".format(months_arg))
