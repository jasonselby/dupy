#! /usr/bin/env python3

#
# Author: Jason Selby
# Date: 19-Aug-2017
# Description:
#   Recurse directories to get total size for each
#
# Copyright: (c) Jason Selby 2017
#

import sys
import os
import heapq
from timeit import timeit


def get_dir_size(d_name, depth=0, dir_heap=[]):
    size = 0
    blks = 0
    files = ""

    # if not os.access(d_name, os.R_OK):
    #     return size

    try:
        for entry in os.scandir(d_name):
            if entry.is_symlink():
                next
            elif entry.is_file():
                size += entry.stat().st_size
                blks += entry.stat().st_blocks
                print("blocksize {}".format(entry.stat().st_blksize))
            elif entry.is_dir():
                sub_size, sub_blks, dir_heap = get_dir_size(entry.path, depth=depth+1, dir_heap=dir_heap)
                size += sub_size
                blks += sub_blks
        # end for
    except Exception as e:
        print( "*** Unable to access {} - {}".format( d_name, e), file=sys.stderr )
    # end try/except

    # print( "{:12d}\t{}".format(size, d_name) )
    heapq.heappush(dir_heap, (size, blks, d_name))
    return size, blks, dir_heap
# end get_dir_size

def main(script, *script_args):
    print( "{} starting with args {}".format(script, script_args) )
    print( "Current system:\n{} - {} - {} - {} - {}\n".format( *os.uname() ) )

    print( "Running python version:\n{}\n".format( sys.version ) )

    # print( 'CWD is %s'%(os.getcwd()) )
    print( "CWD is {}\n".format(os.getcwd()) )

    size, blks, dir_heap = get_dir_size(os.getcwd())

    while dir_heap:
        d = heapq.heappop(dir_heap)
        print( "{:12d}\t{:12d}\t{}".format(*d) )
    print( "Total: {:d} bytes, {:d} blocks".format(size, blks) )
# end main


if __name__ == '__main__':
    main(*sys.argv)
