#!/usr/bin/python3
"""
    Servidor Calculadora
    Jaime Fernández Sánchez
"""

import socket
import calculadora

mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mySocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
mySocket.bind(('localhost', 1234))
mySocket.listen(5)

try:
    while True:
        print('Waiting for connections')
        (recvSocket, address) = mySocket.accept()
        Respuesta = str(recvSocket.recv(1024), 'utf-8')
        Operacion = Respuesta.split()[1]
        Basura,Op1,Oper,Op2 = Operacion.split('/')

        Num1 = int(Op1)
        Num2 = int(Op2)
        Solucion = "Resultado: "
        try:
            Respuesta_Html = Solucion + str(calculadora.Operaciones[Oper](Num1,Num2))
        except KeyError:
            Respuesta_Html = "No existe la funcion " + Oper

        recvSocket.send(bytes('HTTP/1.1 200 OK\r\n\r\n' + "<html><body><title>Calculadora Online</title>"
            + "<h1>" + Respuesta_Html + "</h1></body></html>" '\r\n', 'utf-8'))
        recvSocket.close()
except KeyboardInterrupt:
    print("Closing binded socket")
    mySocket.close()
