import machine
import utime

led_pin = machine.Pin("LED", machine.Pin.OUT) # The onboard LED of Raspberry Pi Pico is connected to pin 25

print("Starting the LED blinking loop...")

while True:
    print("Turning LED on...")
    led_pin.value(1)  # Turn LED on (high)
    utime.sleep(0.5) # Wait for 0.5 seconds
    
    print("Turning LED off...")
    led_pin.value(0)  # Turn LED off (low)
    utime.sleep(0.5) # Wait for 0.5 seconds
