import RPi.GPIO as GPIO
import javino

PIN_LED = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN_LED, GPIO.OUT)

def getExogenousPerceptions():
    javino.addPercept(ledStatus())

###################### LED 
def ledOn():
    GPIO.output(PIN_LED, GPIO.HIGH)

def ledOff():
    GPIO.output(PIN_LED, GPIO.LOW)

def ledStatus():
    estado = GPIO.input(PIN_LED)
    return "ledStatus(on)" if estado == GPIO.HIGH else "ledStatus(off)"
################################

if __name__ == "__main__":
    porta = "/dev/ttyExogenous0"  # Substitua pela porta serial desejada
    comm = javino.start(porta)
    
    if comm:
        try:
            while True:
                # Verifica se há mensagens disponíveis na porta serial
                if javino.availableMsg(comm):
                    mensagem = javino.getMsg(comm)                   
                    if mensagem == "getPercepts":
                        getExogenousPerceptions()
                        print("sending perceptions")
                        javino.sendPercepts(comm)
                    elif mensagem == "ledOn":
                        ledOn()
                    elif mensagem == "ledOff":
                        ledOff()
                    else:
                        print(f"Action not implemented:{mensagem}")
        except KeyboardInterrupt:
            GPIO.cleanup()
            javino.disconnect(comm)
    else:
        print("Não foi possível conectar à porta serial.")
