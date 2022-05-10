import getopt

opt_template = "t:p:l"
long_opts = ["target", "port", "listen"]

class Options:
	def __init__(self, opt_template, long_opts=''):
		self.opt_template = opt_template
		self.long_opts = long_opts
		self.listen = False
		self.addr = ''
		self.port = ''

	def load_options(self, options):
		opts, args = getopt.getopt(options, self.opt_template, self.long_opts)

		for opt, arg in opts:
			if opt in ('-t', '--target'):
				self.addr = arg

			elif opt in ('-p', '--port'):
				self.port = arg

			elif opt in ('-l', '--listen'):
				self.listen = True 

			else:
				self.usage()