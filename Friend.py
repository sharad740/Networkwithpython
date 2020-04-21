import socket,os,sys,subprocess
def main(HOST,PORT):
	s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	s.connect((HOST,PORT))
	print("[ + ] CONNECTED TO SERVER :OKEY")
	while True:
		data = s.recv(1024)
		if data:
			show = str(data.decode("utf-8"))
			print("[ - ] Server :" ,show)
		send = input("[ * ] Client :")
		if send == "exit":
			s.send(bytes("[# <--- CLient is Offline ---> #]",encoding="utf-8"))
			sys.exit("[ % ] CONNECTION TERMINATED ! . ")
		s.send(bytes(send,encoding="utf-8"))
main(socket.gethostname(),6521)