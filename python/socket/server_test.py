# -*- coding: utf-8 -*-

# ソケット通信(サーバー側)
import socket

if __name__ == "__main__":
	ip = '127.0.0.1'
	port = 8765
	server = (ip, port)

	print('サーバー開始')
	socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	socket_server.bind(server)
	socket_server.listen(1)

	# コネクション取得
	connection, address = socket_server.accept()
	print('接続:{}'.format(address))

	# 無限ループ
	recvline = ''
	sendline = ''
	num = 0

	while True:
		# データ受信
		recvline = connection.recv(4096).decode()

		if recvline == 'bye':
			break

		try:
			num = int(recvline)

			if num % 2 == 0:
				sendline = 'OKです'.encode('UTF-8')
			else:
				sendline = 'NGです'.encode('UTF-8')

			connection.send(sendline)

		except ValueError as e:
			sendline = '数値でない'.encode('UTF-8')
			connection.send(sendline)

		finally:
			print('受信文字{}'.format(recvline))
	
	connection.close()
	socket_server.close()
	print('サーバー終了')








