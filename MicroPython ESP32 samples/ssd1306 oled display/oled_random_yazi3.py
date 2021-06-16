# Ornek OLED_random
# SSD1306 kutuphanesinin kullanilmasi
# ESP32 icin I2C0 
# SDA <---------->Pin 21
# SCL <---------->Pin 22
# GND <---------->GND
# Vcc <---------->3.3 V
# 0x3c OLED ADRESI

#
# ad: Albeza Kaçar
# mail: albezaaselbvv@gmail.com
# Cezeri Yeşil Teknoloji MTAL' de
# Yenilenebilir Enerji Sistemleri öğrencisi


#     X=80 MAX
#     Y=56 MAX

#     X=7 MİN
#     Y=7 MİN

from machine import Pin,I2C
import random,ssd1306,gfx
from time import sleep

i2c0 = I2C(scl=Pin(18), sda=Pin(19), freq=400000)
oled = ssd1306.SSD1306_I2C(128,64,i2c0)
graphics = gfx.GFX(128, 64, oled.pixel)
#veya
#from ssd1306 import SSD1306_I2C
#oled = SSD1306_I2C(128, 64, I2C(scl=Pin(18), sda=Pin(19)))

while True:
    X=(int(random.randint(7,80)))
    Y=(int(random.randint(7,56)))

    graphics.fill_circle(X,Y,7,1)   #X60  Y30
    graphics.fill_circle((X+40),Y,7,1)
    graphics.fill_rect(X,(Y-7),41,15 ,1)
    oled.text("CEZERI",(X-3),(Y-3),0)

    oled.show()