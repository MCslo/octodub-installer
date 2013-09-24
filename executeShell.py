from subprocess import Popen,PIPE


class executeShell(object):
	
	def __init__(self,commands):
		Popen(commands, stdout=PIPE, shell=True).stdout.read()