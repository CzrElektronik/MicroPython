#
# ad: Albeza Kaçar
# mail: albezaaselbvv@gmail.com
# Cezeri Yeşil Teknoloji MTAL' de
# Yenilenebilir Enerji Sistemleri öğrencisi


from machine import Pin, I2C
from time import sleep
import ssd1306, gfx 

i2c = I2C(0)
oled = ssd1306.SSD1306_I2C(128, 64, i2c)
graphics = gfx.GFX(128, 64, oled.pixel)

graphics.fill_triangle (0,15,63,0,127,15,1) #ucgen cati
graphics.fill_rect(0,16,128,64 ,1)  #bina duvarı
graphics.fill_rect(50,40,28,23 ,0)  #kapılar
graphics.line(64, 40, 64, 64, 1 )   #kapı orta cizgi
graphics.line(62, 50, 62, 54, 1 )   #kapı kol cizgi
graphics.line(66, 50, 66, 54, 1 )   #kapı kol çizgi
graphics.fill_circle(64,8,5,0)      #yuvarlak pencere     
graphics.fill_rect(10,22,20,10 ,0)  #pencere
graphics.fill_rect(40,22,20,10 ,0)   #pencere
graphics.fill_rect(70,22,20,10 ,0)   #pencere
graphics.fill_rect(100,22,20,10 ,0)  #pencere
graphics.fill_rect(110,40,16,11 ,0) #bayrak
graphics.line(110, 40, 110, 64, 0 )  #bayrak direk
graphics.fill_circle(115,45,3,1)      #dolunay  
graphics.fill_circle(116,45,2,0)      #hilal yapıcı silici
graphics.fill_circle(120,46,1,1)      #yıldız
oled.show()