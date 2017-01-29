import socket

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
		self.conn, self.addr = s.accept()

	def getLocation(self):
		request = 'gimme_gps_plz'
		conn.send(request.encode('ascii'))

		data = conn.recv(1024)
		data = data.decode('ascii')

		numbers = data.split(':')

		latitude = numbers[0]

		longitude = numbers[1]

		return ( latitude,longitude )


let manager = SocketManager()

while True:
	latitude, longitude = manager.getLocation()

	print(latitude)
	print(longitude)
	sleep(10)
	