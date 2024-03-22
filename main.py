import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(5)
host = input("please enter the IP you want to scan: ")
port = int(input("please enter the port you want to scan: "))


def portScanner(port):
    if s.connect_ex((host, port)):
        print("the port is closed")

    else:
        print("the port is open")


portScanner(port)
