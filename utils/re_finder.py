# simple python script to filter stuff from files using regex because grep doesn't get the job done ;)

import re
import click


try:

	@click.command()
	@click.option('--regex','-r', type=str, help='regular expression to use')
	@click.option('--file','-f', type=str, help='file to search in ')
	def filtr(regex,file):

		with open(file, 'r', encoding='latin1') as s:
			stuff = s.readlines() 
			for l in stuff:
				line = l.strip()

				pattern = re.compile(rf'{regex}')

				result = pattern.findall(line)
				print(''.join(result))

	if __name__ == '__main__':
		filtr()

except TypeError:
	print('[-] use python3 re_finder.py --help')