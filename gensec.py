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

def read_fasta(file):
	sequence=''
	with open(file, 'r') as f:
		next(f)
		for line in f:
			sequence = sequence + str(line).strip()

	return sequence

def run():
	usage = "usage: %prog [options]"
	parser = OptionParser(usage)
	parser.add_option('-f', '--fasta', action='store', type='string', dest='fasta')
	parser.add_option('-s', '--start', action='store', type='int', dest='start')
	parser.add_option('-e', '--end', action='store', type='int', dest='end')
	(options, args) = parser.parse_args()

	sequence = read_fasta(options.fasta)
	print sequence[int(options.start):int(options.end)]

if __name__ == '__main__':
	run()