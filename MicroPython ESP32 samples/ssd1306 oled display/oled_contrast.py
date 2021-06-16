# Ornek oled_contrast
# SSD1306 kutuphanesinin kullanilmasi
# ESP32 icin I2C0 
# SDA <---------->Pin 19
# SCL <---------->Pin 18
# GND <---------->GND
# Vcc <---------->3.3 V
# 0x3c OLED ADRESI
#
#
#oled.contrast(255) 0-255 degerler arası contrast yapar
#parantez içine girilen sayının mutlak degerini 255 e boler ve kalan kontrasta esit olur.

#
# ad: Albeza Kaçar
# mail: albezaaselbvv@gmail.com
# Cezeri Yeşil Teknoloji MTAL' de
# Yenilenebilir Enerji Sistemleri öğrencisi

from machine import I2C, Pin
import ssd1306

i2c0 = I2C(scl=Pin(18), sda=Pin(19), freq=400000)
oled = ssd1306.SSD1306_I2C(128,64,i2c0)
i=0

#veya
#from ssd1306 import SSD1306_I2C
#lcd = SSD1306_I2C(128, 64, I2C(scl=Pin(18), sda=Pin(19)))

while True:
    i = input("parlaklık gir = ")    #0-255 arası degerler ile contrast ayarı yapmak mumkun
    oled.contrast(int(i))
    oled.fill(1)
    oled.show()
    