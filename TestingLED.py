from machine import Pin

pins = [13, 14, 15]

for p in pins:
    pin = Pin(p, Pin.OUT)

    print("Testing GPIO", p)

    pin.value(1)
    input("Press Enter...")
    pin.value(0)
