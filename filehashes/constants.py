#!/usr/bin/env python3
""" Module constant store the constant value of queue, workers and arguments option"""
import logging as logger

MAX_QSIZE   =   10
MAX_WORKERS =   4

""" options are arguments added in the parser for user input """
options = (
#   ("long option", "short option", "help for the option", required)
    ("--list", "-l", "Please provide directory name.", True),
    ("--sign", "-s", "Please provide signature algo, md5 | crc", True))

LOG_FILE    = "/filehashes/logs/file_hash.log"
# LOG_FILE = "F:\Gitworkplace\python_basic\filehashes\logs\file_hash.log"
LOG_FORMAT  = "%(module)s - %(thread)s- %(message)s"

"""Debug provide detailed information"""
logger.basicConfig(
    filename=LOG_FILE,
    format=LOG_FORMAT,
    level=logger.DEBUG)