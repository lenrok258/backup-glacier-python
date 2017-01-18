import os
import re


class ArchiveDirectory:
    def __init__(self, input_path, dir_name):
        self.input_path = input_path
        self.dir_name = dir_name

    @property
    def dir_path(self):
        return os.path.join(self.input_path, self.dir_name)

    def __str__(self):
        return self.dir_path

    def __repr__(self):
        return self.dir_path


def list_directories(input_dir, months_range):
    months_list = __expand_months_list(months_range)
    months_regexp = __prepare_months_regexp(months_list)
    dirs = __list_all_dirs_in_input_dir(input_dir)
    dirs_in_range = __filter_dirs_with_regexp(dirs, months_regexp)
    # TODO: Check if directory is marked as archived, exclude it and log warning
    return prepare_result(input_dir, dirs_in_range)


def __filter_dirs_with_regexp(dirs, months_regexp):
    dirs_in_range = filter(lambda dir_name: re.match(months_regexp, dir_name), dirs)
    return dirs_in_range


def __list_all_dirs_in_input_dir(input_dir):
    paths = os.listdir(input_dir)
    dirs = filter(lambda path: os.path.isdir(os.path.join(input_dir, path)), paths)
    return dirs


def __prepare_months_regexp(months_list):
    months_range_list_strings = map(lambda i: "_{:02d}".format(i), months_list)
    months_regexp = "|".join(months_range_list_strings)
    return ".*(" + months_regexp + ").*"


def __expand_months_list(months_range):
    range_split = months_range.split("-")
    range_start = range_split[0]
    range_end = range_split[1]
    months_range_list = range(int(range_start), int(range_end) + 1)
    return months_range_list


def prepare_result(input_dir, dirs_in_range):
    return map(lambda dir_name: ArchiveDirectory(input_dir, dir_name), dirs_in_range)
