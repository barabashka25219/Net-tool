import subprocess

def command_handler(command_string):
	command = subprocess.run(command_string.rstrip(), shell=True, capture_output=True)

	# if we'll get error
	if command.returncode != 0:
		result = f"[!] Can't execute {command_string}! :(".encode()

	# if we'll get success code and process output
	elif command.stdout and not command.returncode:
		result = command.stdout

	# if we'll get success code, but not output
	else:
		result = f"[*] Done!".encode()

	return result 