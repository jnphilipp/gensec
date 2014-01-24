#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
		This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

from optparse import OptionParser
import sys

fasta_line_length = 70

def read_fasta(file):
	sequence=''
	description=''
	with open(file, 'r') as f:
		for line in f:
			if line.startswith('>'):
				description = description + str(line).strip()
			else:
				sequence = sequence + str(line).strip()

	return (description, sequence)

def run():
	usage = "usage: %prog [options]"
	parser = OptionParser(usage)
	parser.add_option('-f', '--fasta', action='store', type='string', dest='fasta', help='Path to fasta file')
	parser.add_option('-s', '--start', action='store', type='int', dest='start', help='start position')
	parser.add_option('-e', '--end', action='store', type='int', dest='end', help='end position')
	parser.add_option('-u', '--unformatted', action='store_true', dest='unformatted', help='prints the sequence as a long unformatted string')
	(options, args) = parser.parse_args()

	if not options.fasta or options.start is None or options.end is None:
		parser.print_help()
		sys.exit()

	description, sequence = read_fasta(options.fasta)
	start = int(options.start) if int(options.start) == 0 else int(options.start) - 1
	subsec = sequence[start:int(options.end)]
	if options.unformatted:
		print subsec
	else:
		print '%s:%s-%s' % (description, start, options.end)
		for i in range(0, len(subsec), fasta_line_length):
			print subsec[i:i+fasta_line_length]

if __name__ == '__main__':
	run()