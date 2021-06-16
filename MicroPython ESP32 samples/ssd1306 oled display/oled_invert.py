# Ornek OLED_invert
# SSD1306 kutuphanesinin kullanilmasi
# ESP32 icin I2C0 
# SDA <---------->Pin 19
# SCL <---------->Pin 18
# GND <---------->GND
# Vcc <---------->3.3 V
# 0x3c OLED ADRESI
#
# oled.invert(1)  # invert=tersini alır.
# yanı ekran piksel renklerini tersine donurur
# invert(1)=true
# invert(0)=false
# yapar.

#
# ad: Albeza Kaçar
# mail: albezaaselbvv@gmail.com
# Cezeri Yeşil Teknoloji MTAL' de
# Yenilenebilir Enerji Sistemleri öğrencisi


from machine import Pin,I2C
from time import sleep

import ssd1306
i2c0 = I2C(scl=Pin(18), sda=Pin(19), freq=400000)
oled = ssd1306.SSD1306_I2C(128,64,i2c0)

#veya
#from ssd1306 import SSD1306_I2C
#lcd = SSD1306_I2C(128, 64, I2C(scl=Pin(18), sda=Pin(19)))

oled.text("Micropython",0,0)
oled.text("Merhaba",24,16)
oled.text("Dunya",32,24)
oled.show()
sleep(1)

while True:
    
    oled.invert(1)      #piksel renklerini tersine dondur 
    sleep(1)

    oled.invert(0)      #pikselleri tekrar ters renk yap
    sleep(1)


