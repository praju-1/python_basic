#!/usr/bin/env python3

import argparse

class CmdParser(object):

    """
    A class represent a command parser

    ...

    Attributes
    ----------
    opts : str
        options from the arguments
    handler : str
        used for target function

    Methods
    -------
    validate(self):
        Validate the algo of sign
    exec(self):
        Execute the function through cmdparser
    set_handler(func):
        Set handler for function
    get_handler():
        Get handler for function
    get_parseopt():
        Get the option of argparse
    set_parseopt(opt):
        Set the option of argparse
    """

    def __init__(self, opts, handler=None):
        """
        Constructs all the necessary attributes for the Cmdparser object.
        """

        self._opts = opts
        self._handler = handler
        cmdp = argparse.ArgumentParser()

        for e in opts:
            cmdp.add_argument(
                e[0],           # for long option
                e[1],           # for short option
                help=e[2],      # help for option
                required=e[3])  # mandatory / optional

        self._args = cmdp.parse_args()

    def validate(self):
        if self._args.sign != "md5" and self._args.sign != "crc":
            raise ValueError("{} sign algorithm is not supported".format(self._args.sign))

    def exec(self):
        try:
            return self._handler(self._args)
        except Exception as e:
            print(e)

    def set_handler(self, func):
        try:
            self._handler = func
        except Exception as e:
            print(e)

    def get_handler(self):
        try:
            return self._handler
        except Exception as e:
            print(e)

    def get_parseopt(self):
        try:
            return self._opts
        except Exception as e:
            print(e)

    def set_parseopt(self, opts):
        try:
            self._opts = opts
        except Exception as e:
            print(e)
