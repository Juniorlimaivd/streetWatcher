import socket
from time import sleep

class SocketManager:
	socket = None
	host = ''
	port = 1235
	conn = ''
	addr = ''

	def __init__(self):
		self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		parametros = (self.host,self.port)
		self.socket.bind(parametros)
		self.socket.listen(1)
		self.conn, self.addr = self.socket.accept()

	def getLocation(self):
		request = 'gimme_gps_plz'
		self.conn.send(request.encode('ascii'))

		data = self.conn.recv(1024)
		data = data.decode('ascii')

		numbers = data.split(':')

		latitude = numbers[0]

		longitude = numbers[1]

		return ( latitude,longitude )


manager = SocketManager()

while True:
	sleep(10)
	latitude, longitude = manager.getLocation()

	print(latitude)
	print(longitude)
	
	