import subprocess

def command_handler(command_string):
	result = subprocess.run(command_string, shell=True, capture_output=True)
	return result.stdout.decode('utf-8')