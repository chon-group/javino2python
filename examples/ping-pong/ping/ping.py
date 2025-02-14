import javino 
import time 
import random 
import string

sizeOfMsg = 64
porta = "/dev/ttyUSB0"  
comm = javino.start(porta)
message = "hello"
count = 0


def random_message(sm):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=sm))

if comm:
    try:
        while True:
            time.sleep(3)
            count = count + 1
            message = f"({count})"+random_message(sizeOfMsg)
            javino.sendMsg(comm,message) 
            print(message, end =" ", flush=True)
            attemp = 50
            while attemp > 0:
                print(".", end =" ", flush=True)
                attemp = attemp -1
                if javino.availableMsg(comm):
                    received = javino.getMsg(comm)
                    if received != None:
                        attemp = 0
                        print(f"received: {received}", end =" ", flush=True)
            print("")            
    except KeyboardInterrupt:
        javino.disconnect(comm)
else:
    print("Não foi possível conectar à porta serial.")
