from options import Options
from command_handler import command_handler
from network import Server, Client
import sys

opt_template = 't:p:lh'
long_opts = ['target', 'port', 'listen', 'help']

if __name__ == '__main__':

	# load our comandline options
	options = Options(opt_template, long_opts)
	options.load_options(sys.argv[1:])

	# creation of server
	if options.listen and options.port:
		server = Server(options.port)
		server.listen_connections()

	# creation of client
	elif options.addr and options.port:
		client = Client(options.addr, options.port)
		client.connect_to_server()

	sys.exit(0)