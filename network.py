import socket
import threading
from command_handler import command_handler

class Server:
	def __init__(self, port):
		self.socket = socket.socket()
		self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)
		self.socket.bind(('0.0.0.0', port))

	def listen_connections(self):
		self.socket.listen(1)

		while True:
			try:
				self.client, self.client_addr = self.socket.accept()
				print(f"[*] {self.client_addr[0]} {self.client_addr[1]} connected.")

			except KeyboardInterrupt:
				print("[*] Closing the server...")
				self.socket.close()
				break

			new_thread = threading.Thread(target=self.connection_handler)
			new_thread.start()

		self.close_server()

	def connection_handler(self):
		while True:
			try:
				command = self.client.recv(4096).decode('utf-8').rstrip()
				command_result = command_handler(command.encode('utf-8'))
				self.client.send(command_result)

			except BrokenPipeError:
				print(f"[*] {self.client_addr[0]} {self.client_addr[1]} disconnected.")
				break

		self.close_connection()


	def close_server(self):
		self.socket.close()

	def close_connection(self):
		self.client.close()



class Client:
	def __init__(self, addr, port):
		self.socket = socket.socket()
		self.serv_addr = addr 
		self.serv_port = port

	def connect_to_server(self):
		try:
			self.socket.connect((self.serv_addr, self.serv_port))
			self.connection_handler()

		except ConnectionRefusedError:
			print(f"[!] Can't connect to {self.serv_addr}:{self.serv_port}")
			

	def connection_handler(self):
		recv_len = 1

		while recv_len:
			print("net-tool>: ", end='')

			try:
				command = input("").rstrip()

			except KeyboardInterrupt:
				print("[*] Closing connection...")
				break

			if not command:
				continue

			elif command == 'disconnect':
				self.close_connection()
				break

			self.socket.send(command.encode())
			serv_answer = self.socket.recv(4096)
			print(serv_answer.decode())


		self.close_connection()

	def close_connection(self):
		self.socket.close()

