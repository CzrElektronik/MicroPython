#
# ad: Albeza Kaçar
# mail: albezaaselbvv@gmail.com
# Cezeri Yeşil Teknoloji MTAL' de
# Yenilenebilir Enerji Sistemleri öğrencisi



from machine import I2C, Pin
import ssd1306, random
from time import sleep

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
sleep(1)


def random_heart():
    xofs = random.randint(0,127)
    yofs = random.randint(0,63)
    for y, row in enumerate(ICON):
        for x, c in enumerate(row):
            display.pixel(x + xofs, y + yofs, c)

for n in range(80):
    random_heart()

display.show()