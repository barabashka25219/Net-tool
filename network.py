import socket
import threading
from command_handler import command_handler
from options import Options

class Server:
	def __init__(self, port):
		self.socket = socket.socket()
		self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)
		self.socket.bind(('0.0.0.0', port))

	def listen_connections(self):
		self.socket.listen(1)

		while True:
			self.client, self.client_addr = self.socket.accept()

			new_thread = threading.Thread(target=self.connection_handler)
			new_thread.start()

	def connection_handler(self):

		while True:
			try:
				command = self.client.recv(4096).decode('utf-8').rstrip()
				command_result = command_handler(command.encode('utf-8'))
				self.client.send(command_result)

			except:
				break


	def close_connection(self):
		self.client.close()

server = Server(5555)
server.listen_connections()