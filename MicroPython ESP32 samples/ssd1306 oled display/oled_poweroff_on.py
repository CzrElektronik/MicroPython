# Ornek OLED_poweron_poweroff
# SSD1306 kutuphanesinin kullanilmasi
#
#
# ad: Albeza Kaçar
# mail: albezaaselbvv@gmail.com
# Cezeri Yeşil Teknoloji MTAL' de
# Yenilenebilir Enerji Sistemleri öğrencisi



# ESP32 icin I2C0 
# SDA <---------->Pin 19
# SCL <---------->Pin 18
# GND <---------->GND
# Vcc <---------->3.3 V
# 0x3c OLED ADRESI
#
# oled.poweroff()   #oleddeki enerjiyi keser.
# oled.poweron()    # oleddeki enerjiyi açar.
#
"""
  Bu fonksiyonları oledi kapatmak veya açmak için kullanabilirsiniz
  Ekrana gostermek istemediğiniz anlarda ekranı temizlemek yerine
ekranı kolay bir şekilde kapatabilirsiniz
"""

from machine import I2C, Pin
from time import sleep

import ssd1306
i2c0 = I2C(scl=Pin(18), sda=Pin(19), freq=400000)
oled = ssd1306.SSD1306_I2C(128,64,i2c0)
i=0

#veya
#from ssd1306 import SSD1306_I2C
#lcd = SSD1306_I2C(128, 64, I2C(scl=Pin(18), sda=Pin(19)))

oled.fill(0)
oled.show()

oled.text("Micropython",0,0)
oled.text("Merhaba",24,16)
oled.text("Dunya",32,24)
oled.show()

while True:
    sleep(3)
    oled.poweroff()  #oled i kapatır.
    sleep(3)
    oled.poweron()   # oledi acar. ekrandaki veriler hala yerindedir.


