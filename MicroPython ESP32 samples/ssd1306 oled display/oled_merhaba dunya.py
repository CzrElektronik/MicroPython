#
# ad: Albeza Kaçar
# mail: albezaaselbvv@gmail.com
# Cezeri Yeşil Teknoloji MTAL' de
# Yenilenebilir Enerji Sistemleri öğrencisi



from machine import Pin, I2C
import ssd1306, gfx
from time import sleep

i2c = I2C(-1, scl=Pin(18), sda=Pin(19))
oled = ssd1306.SSD1306_I2C(128, 64,i2c)
graphics = gfx.GFX(128, 64, oled.pixel)



oled.text('MERHABA', 0, 0)   # yazılacak sey, x, y eksenleri
oled.text('DUNYA', 0, 8, )


oled.show()  #degisiklikleri kaydeder