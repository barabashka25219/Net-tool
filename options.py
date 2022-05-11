import getopt

class Options:
	def __init__(self, opt_template, long_opts=''):
		self.opt_template = opt_template
		self.long_opts = long_opts
		self.listen = False
		self.addr = ''
		self.port = ''

	def load_options(self, options):
		if not options:
			self.usage()

		try:
			opts, args = getopt.getopt(options, self.opt_template, self.long_opts)

			for opt, arg in opts:
				if opt in ('-t', '--target'):
					self.addr = arg

				elif opt in ('-p', '--port'):
					self.port = int(arg)

				elif opt in ('-l', '--listen'):
					self.listen = True 

				elif opt in ('-h', '--help'):
					self.usage()

				else:
					self.usage()

		except getopt.GetoptError as gerr:
			print(f"[*] {gerr}")
			

	def usage(self):
		print("Net tool")
		print("")
		print("-t, --target - target ip address")
		print("-p, --port   - target port")
		print("-l, --listen - listen connections (if it's a server)")
		print("")
		print("python3 net_tool.py -t 192.168.0.1 -p 5555")
		print("python3 net_tool.py -l -p 5555")