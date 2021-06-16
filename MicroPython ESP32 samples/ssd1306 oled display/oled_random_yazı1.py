# Ornek OLED_random1
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



from machine import Pin,I2C
import random
from time import sleep
import ssd1306
i2c0 = I2C(scl=Pin(18), sda=Pin(19), freq=400000)
oled = ssd1306.SSD1306_I2C(128,64,i2c0)
#veya
#from ssd1306 import SSD1306_I2C
#lcd = SSD1306_I2C(128, 64, I2C(scl=Pin(18), sda=Pin(19)))

while True:
    oled.fill(0)
    oled.show()
    x=(int(random.randint(0,126)))
    y=(int(random.randint(0,62)))
    oled.pixel(x,y,1)
    oled.show()
    sleep(1)