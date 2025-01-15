import time
import RPi.GPIO as gpio

pin = 4
gpio.setwarnings(False)
gpio.setmode(gpio.BOARD)
gpio.setup(pin, gpio.OUT)

try:
    print("Buzzer z generatorem włączony. Naciśnij Ctrl+C, aby zatrzymać.")
    while True:
        gpio.output(pin, 0)
        time.sleep(0.3)
        gpio.output(pin, 1)
        time.sleep(0.3)
except KeyboardInterrupt:
    gpio.cleanup()
    print("\nProgram zakończony.")
