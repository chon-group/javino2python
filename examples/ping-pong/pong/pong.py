import javino 
import time 
import random 
import string

porta = "/dev/ttyUSB1" 
comm = javino.start(porta)

if comm:
    try:
        while True:
            if javino.availableMsg(comm):
                mensagem = javino.getMsg(comm)
                if mensagem != None:
                    print(f"received: {mensagem}")
                    javino.sendMsg(comm,mensagem)
                else:
                    print(f"received: {mensagem}")
    except KeyboardInterrupt:
        javino.disconnect(comm)
else:
    print("Não foi possível conectar à porta serial.")
