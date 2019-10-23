#!/usr/bin/env python

import sys
import csv
from io import StringIO
import textwrap
import argparse

# help flag provides flag help
# store_true actions stores argument as True

parser = argparse.ArgumentParser()
parser.add_argument('-d', '--in-delimeter', dest='indelimeter', type=str,
    help="sets in delimeter")
parser.add_argument('-q', '--in-quote', dest='inquote', type=str,
    help="sets in quote")
parser.add_argument('infile')
parser.add_argument('outfile')

args = parser.parse_args()


if args.inquote:
    inquote = args.inquote

infile = args.infile
outfile = args.outfile

f = open(outfile, mode = 'a')

with open(infile, newline='') as csvfile:
    dialect = csv.Sniffer().sniff(csvfile.read(1024))
    csvfile.seek(0)
    if args.indelimeter:
      indelimeter = args.indelimeter
      reader = csv.reader(csvfile, dialect, delimiter=indelimeter)
    else:
      reader = csv.reader(csvfile, dialect)
    writer = csv.writer(f)
    for row in reader:
      writer.writerow(row)

#print(open(outfile, 'rt').read())
