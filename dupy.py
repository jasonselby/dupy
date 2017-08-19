#! /usr/bin/env python3

#
# Author: Jason Selby
# Date: 19-Aug-2017
# Description:
#
# Copyright: (c) Jason Selby 2017
#

import sys
from timeit import timeit


class MyClass:
    def __init__(self):
        super().__init__()
    # end __init__
# end class MyClass


def main(script, *script_args):
    print( '%s starting with args %s'%(script, script_args) )
# end main


if __name__ == '__main__':
    main(*sys.argv)
