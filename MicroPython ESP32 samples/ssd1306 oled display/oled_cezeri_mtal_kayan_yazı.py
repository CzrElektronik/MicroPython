#
# ad: Albeza Kaçar
# mail: albezaaselbvv@gmail.com
# Cezeri Yeşil Teknoloji MTAL' de
# Yenilenebilir Enerji Sistemleri öğrencisi


import time, machine, ssd1306
from time import sleep
from machine import Pin, I2C

i2c = I2C(-1, scl=Pin(18), sda=Pin(19))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)
a, c, b, d, x, e = 138, 138, -30, -30, 5, 64
def oledyazdır():
    oled.show()
    time.sleep(0.001)
    oled.fill(0)


while (True):
    while (a>=-70):
        oled.text('CEZERI', a, x+2)
        oledyazdır()
        a=a-2
    a=138
    while (b<=128):
        oled.text('YESIL', b, x+15)
        oledyazdır()
        b=b+2
    b=-30
    while (c>=-70):
        oled.text('TEKNOLOJI', c, x+30)
        oledyazdır()
        c=c-2
    c=138
    while (d<=128):
        oled.text('MTAL', d, x+45)
        oledyazdır()
        d=d+2        
    d=-30
  
    while (e>=-64):
        oled.invert(True)
        oled.text('CEZERI', 40, e+10)
        oled.text('YESIL', 45, e+20)
        oled.text('TEKNOLOJI', 30, e+30)
        oled.text('MTAL', 50, e+40)
        oled.show()
        time.sleep(0.001)
        oled.fill(0)
        e=e-1
    e=64
    oled.invert(False)
    time.sleep(1)
