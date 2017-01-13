#!/usr/bin/env python

from __future__ import absolute_import
from __future__ import print_function



class colors:
  HEADER = '\033[95m'
  OKBLUE = '\033[94m'
  OKGREEN = '\033[92m'
  WARNING = '\033[93m'
  FAIL = '\033[91m'
  ENDC = '\033[0m'
  BOLD = '\033[1m'
  UNDERLINE = '\033[4m'


def __ERR_SIG__():
	print(colors.BOLD + '[#] Help!! There\'s a glitch here' + colors.ENDC)