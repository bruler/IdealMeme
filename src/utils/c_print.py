#!/usr/bin/env python
__author__ = "Kapil Gupta"
__copyright__ = "Copyright 2016, TheMallCloud"
__credits__ = ["Kapil Gupta"]
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "Kapil Gupta"
__email__ = "kpgupta98@gmail.com"
__status__ = "Production"


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