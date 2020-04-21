import socket,sys,os
def main(HOST,PORT):
    # This is my first Socket programming with Python.Server.py [{"Author":"Sharad Bhandari"}]
    try:
        __BIND_ME__ = (HOST,PORT);s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        print("[ + ] SERVER CREATION : OKAY")
        s.bind(__BIND_ME__)
        s.listen(5)
        conn,address = s.accept()
        print("[ + ] CLIENT PORT BINDING AND LISTENING : OKAY")
        print("[ + ] SERVER ACCEPTING CONNECTION FROM :[IP] >> {} , [PORT] >> {}".format(address[0],address[1]))
        while True:
            cmd = input("[ * ] Server :")
            if cmd == "exit":
                s.sendall(bytes("*#<---Server is Offline -->#*",encoding="utf-8"))
                conn.close()
                s.close()
                sys.exit("[ % ] Connection Terminated ! . ")
            if len(str.encode(cmd)) > 0:
                conn.send(bytes(cmd,encoding="utf-8"))
                client_response =("CLIENT [ {} ][] :".format(address[0],address[1]),conn.recv(1024).decode("utf-8"))
                print(client_response)
    except Exception as e:
        print("""
        [ - ] ERROR occurred :
        [ + ] NAME        : {}
        """.format(e))
main(socket.gethostname(),6521)