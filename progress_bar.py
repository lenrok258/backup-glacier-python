# -*- coding: utf-8 -*-

import sys


# Print iterations progress
def printProgress(iteration, total, prefix='', suffix='', decimals=1, barLength=100, fill='█'):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        barLength   - Optional  : character length of bar (Int)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(barLength * iteration // total)
    bar = fill * filledLength + '-' * (barLength - filledLength)
    sys.stdout.write('\r%s |%s| %s%s %s' % (prefix, bar, percent, '%', suffix)),
    if iteration == total:
        sys.stdout.write('\n')
    sys.stdout.flush()


def test():
    from time import sleep
    items = list(range(0, 57))
    i = 0
    l = len(items)

    # Initial call to print 0% progress
    print 'Going to do very important stuff:'
    printProgress(i, l, prefix='Progress:', suffix='Complete', barLength=50)
    for item in items:
        # Do stuff...
        sleep(0.1)
        # Update Progress Bar
        i += 1
        printProgress(i, l, prefix='Progress:', suffix='Complete', barLength=50)

    print 'Done, so proud.'


if __name__ == '__main__':
    test()
