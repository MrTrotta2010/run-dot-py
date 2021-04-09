import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--run', required=True, type=int, help='Determines if the program should run or not')
r = bool(vars(parser.parse_args())['run'])

def run():
	pass

if __name__ == "__main__":
	if r:
		run()