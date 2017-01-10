import os
import re


def list_directories(input_dir, months_range):
    months_list = __expand_months_list(months_range)
    months_regexp = __prepare_months_regexp(months_list)
    dirs = __list_all_dirs_in_input_dir(input_dir)
    dirs_in_range = __filter_dirs_with_regexp(dirs, months_regexp)
    paths_in_range = map(lambda dir_name: input_dir + "/" + dir_name, dirs_in_range)
    return paths_in_range


def __filter_dirs_with_regexp(dirs, months_regexp):
    dirs_in_range = filter(lambda dir_name: re.match(months_regexp, dir_name), dirs)
    return dirs_in_range


def __list_all_dirs_in_input_dir(input_dir):
    paths = os.listdir(input_dir)
    dirs = filter(lambda path: os.path.isdir(input_dir + '/' + path), paths)
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
