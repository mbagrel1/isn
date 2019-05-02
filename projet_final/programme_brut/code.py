import board
import time

from analogio import AnalogIn
from digitalio import DigitalInOut, Direction

led_connections = [
    [board.D2, board.D3, board.D4],
    [board.D5, board.D6, board.D7],
    [board.D8, board.D9, board.D10],
    [board.D11, board.D12, board.D13]
]

leds = []

for pins in led_connections:
    led = []
    for pin in pins:
        pin_interface = DigitalInOut(pin)
        pin_interface = Direction.OUTPUT
        led.append(pin_interface)
    leds.append(led)

button_connections = [
    board.A2,
    board.A3,
    board.A4,
    board.A5
]

buttons = []

for pin in button_connections:
    button = AnalogIn(pin)

def is_pressed(button):
    return button.value / 65535.0 > 0.5

def switch_led_on(led, color):
    for (pin_interface, int_value) in zip(led, color):
        pin_interface.value = bool(int_value)

def switch_led_off(led):
    for pin_interface in led:
        pin_interface.value = False

COLORS = [
    (1, 0, 0),
    (0, 1, 0),
    (0, 0, 1),
    (1, 0, 1)
]

while True:
    for (button, led, color) in zip(buttons, leds, COLORS):
        if is_pressed(button):
            switch_led_on(led, color)
        else:
            switch_led_off(led)
    time.sleep(0.05)
