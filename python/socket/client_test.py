# -*- coding: utf-8 -*-

# ソケット通信(クライアント側)
import socket

if __name__ == "__main__":
	ip = '127.0.0.1'
	port = 8765
	server = (ip, port)

	print('クライアント接続')
	socket_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	socket_client.connect(server)

	line = ''
	while line != 'bye':

		# 標準入力からデータを取得
		print('偶数を入力')
		line = input('>>>')

		# サーバーに送信
		socket_client.send( line.encode('UTF-8') )

		# サーバーから受信
		dat = socket_client.recv(4096).decode()

		# 受信データの表示
		print('サーバーからの回答: {}'.format(dat))

	socket_client.close()
	print('クライアント終了')

