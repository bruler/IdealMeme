#!/usr/bin/env python

from __future__ import absolute_import
from __future__ import print_function

__author__ = "Kapil Gupta"
__copyright__ = "Copyright 2016, TheMallCloud"
__credits__ = ["Kapil Gupta"]
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "Kapil Gupta"
__email__ = "kpgupta98@gmail.com"
__status__ = "Production"


import template_features_req_pb2
import json
import sys
import os.path

sys.path.append('..')
path_to_json = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "_conf.json")
path_to_book = os.path.join(os.path.dirname(os.path.abspath(__file__)), "parameters_book.prototxt")

with open(path_to_json) as conf_file:
	conf = json.load(conf_file)

def CheckTemplatesNeeded(templates) :
  pass

def CreateTemplates(templates) :
	CheckTemplatesNeeded(templates)


parameters_book = template_features_req_pb2.Templates()

try:
	with open(path_to_book, 'rb') as file:
		parameters_book.ParseFromString(file.read())
except IOError:
	print('[!] Parameters Book not present, creating new book')

CreateTemplates(parameters_book.templates.add())

with open(path_to_book, 'wb') as file:
	file.write(parameters_book.SerializeToString())