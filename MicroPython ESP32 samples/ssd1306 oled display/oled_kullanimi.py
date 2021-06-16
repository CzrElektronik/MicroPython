import network
wifi=network.WLAN(network.STA_IF)

import aga_baglan
import machine

from machine import Pin, I2C
Led_status=Pin(22,Pin.OUT)
i2c = I2C(scl=Pin(22), sda=Pin(18), freq=400000)

import ssd1306
oled = ssd1306.SSD1306_I2C(128,64,i2c)


        
# timer objesi olustur.
def tmr1_kesmesi(timer):
    #aga baglımıyım testi
    if wifi.isconnected():
        Led_status.value(1-Led_status.value())   #yanık
        oled.fill(0)
        oled.text("bagli",35,30)
        oled.show()
    else:
        Led_status.value(1)   #sonuk /tersine calısır
        oled.fill(0)
        oled.text("bagli degil",35,30)
        oled.show()


from machine import Timer
tmr1 = Timer(-1) # sanal zamanlayıcı yap
tmr1.init(period=500, mode=Timer.PERIODIC, callback=tmr1_kesmesi)