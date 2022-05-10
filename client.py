import socket

class Client:
	def __init__(self, addr, port):
		self.socket = socket.socket()
		self.serv_addr = addr 
		self.serv_port = port

	def connect_to_server(self):
		self.socket.connect((self.serv_addr, self.serv_port))

	def connection_handler(self):
		recv_len = 1

		while recv_len:
			print("net-tool>: ", end='')

			command = input("").rstrip()

			if not command:
				continue

			elif command == 'disconnect':
				self.close_connection()
				break

			self.socket.send(command.encode())
			serv_answer = self.socket.recv(4096)
			print(serv_answer.decode())

	def close_connection(self):
		self.socket.close()

client = Client('127.0.0.1', 5555)
client.connect_to_server()
client.connection_handler()