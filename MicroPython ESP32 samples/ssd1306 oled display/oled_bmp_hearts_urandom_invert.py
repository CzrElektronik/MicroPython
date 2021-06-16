#
# ad: Albeza Kaçar
# mail: albezaaselbvv@gmail.com
# Cezeri Yeşil Teknoloji MTAL' de
# Yenilenebilir Enerji Sistemleri öğrencisi


from machine import I2C, Pin
import ssd1306

i2c0 = I2C(scl=Pin(18), sda=Pin(19), freq=400000)
display = ssd1306.SSD1306_I2C(128,64,i2c0)

ICON = [
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [ 0, 1, 1, 0, 0, 0, 1, 1, 0],
    [ 1, 1, 1, 1, 0, 1, 1, 1, 1],
    [ 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [ 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [ 0, 1, 1, 1, 1, 1, 1, 1, 0],
    [ 0, 0, 1, 1, 1, 1, 1, 0, 0],
    [ 0, 0, 0, 1, 1, 1, 0, 0, 0],
    [ 0, 0, 0, 0, 1, 0, 0, 0, 0],
]

display.fill(0) # Clear the display
for y, row in enumerate(ICON):
    for x, c in enumerate(row):
        display.pixel(x, y, c)

display.show()

import urandom

def random_heart():
    xofs = urandom.getrandbits(8)
    yofs = urandom.getrandbits(5)
    for y, row in enumerate(ICON):
        for x, c in enumerate(row):
            display.pixel(x + xofs, y + yofs, c)

for n in range(100):
    random_heart()

display.show()
import time
while True:
    display.invert(0)
    time.sleep(0.1)
    display.invert(1)
    time.sleep(0.1)