import directory_resolver

from argument_parser import ArgumentParser


def main():
    args = ArgumentParser()
    print 'Given arguments: {}'.format(args)

    paths_to_backup = directory_resolver.list_directories(args.input_dir(), args.months_range())

    # zip each directory 

    # encrypt each zip

    # upload each zip to Glacier

    # mark (text file in directory) as 'backed-up'

    # clean up (delete encrypted package)


if __name__ == '__main__':
    main()
