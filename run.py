# Tiago Trotta - 09/04/2021
# GNU General Public License v3.0

import argparse
from sys import exit

parser = argparse.ArgumentParser()
parser.add_argument('--run', required=True, type=int, help='Determines if the program should run or not')
r = bool(vars(parser.parse_args())['run'])

def run():
	pass

if __name__ == "__main__":
	if r:
		run()
	else:
		exit(0)
