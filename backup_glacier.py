import os

from argument_parser import ArgumentParser


def get_directories_list(input_dir, months_range):
    range_split = months_range.split("-")
    range_start = range_split[0]
    range_end = range_split[1]
    moths_range_list = range(int(range_start), int(range_end) + 1)

    paths = os.listdir(input_dir)
    dirs = filter(lambda path: os.path.isdir(input_dir + '/' + path), paths)



def main():
    args = ArgumentParser()
    print 'Given arguments: {}'.format(args)

    # list directories => paths list
    input_dir = args.input_dir()
    months_range = args.months_range()
    dirs = get_directories_list(input_dir, months_range)


    # zip each directory 

    # encrypt each zip

    # upload each zip to Glacier

    # mark (text file in directory) as 'backed-up'

    # clean up (delete encrypted package)


if __name__ == '__main__':
    main()
