#
# ad: Albeza Kaçar
# mail: albezaaselbvv@gmail.com
# Cezeri Yeşil Teknoloji MTAL' de
# Yenilenebilir Enerji Sistemleri öğrencisi



from machine import Pin, I2C
from time import sleep
import ssd1306, gfx 

i2c = I2C(-1, scl=Pin(18), sda=Pin(19))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)
graphics = gfx.GFX(128, 64, oled.pixel)

graphics._slow_hline(0,0,30,1) #saga uzayan cizgi
graphics._slow_vline(50,30,20,1) #assaya uzayan cizgi
oled.show()