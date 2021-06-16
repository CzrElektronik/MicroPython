#
# ad: Albeza Kaçar
# mail: albezaaselbvv@gmail.com
# Cezeri Yeşil Teknoloji MTAL' de
# Yenilenebilir Enerji Sistemleri öğrencisi



from machine import Pin, I2C
from time import sleep, sleep_ms
import utime, ssd1306, framebuf, random, gfx

i2c0 = I2C(scl=Pin(18), sda=Pin(19), freq=400000)
oled = ssd1306.SSD1306_I2C(128,64,i2c0)


fb = framebuf.FrameBuffer(bytearray(
    b'\x1c\x3e\x7e\xfc\xf8\xfc\x7e\x3e\x1c\x00\x00\x00\x00\x01\x00\x00\x00\x00'),
    9, 9, framebuf.MONO_VLSB)

def random_heart():
    xofs = random.randint(0,127)
    yofs = random.randint(0,63)
    oled.blit(fb, xofs, yofs)
# sleep(5)
while True:
    oled.fill(0)
    x=22
    y=40
    xline=84
    yline=17

    for n in range(30):
        random_heart()
        oled.show()
        sleep_ms(10)
        
    for n in range(50):
        random_heart()
        oled.fill_rect((x-1),(y-1),(xline+2),(yline+2) ,1)
        oled.fill_rect(x ,y ,xline , yline, 0)
        oled.show()
        sleep_ms(10)

    oled.text("CEZERI", 41, 45)    
    oled.show()
    sleep(2)

