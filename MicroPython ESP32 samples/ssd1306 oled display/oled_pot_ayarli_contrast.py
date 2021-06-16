# pot analog değer ayarlı oled contrast orneği
# esp32 analog 0-4095 aralıklı deger okur


#
# ad: Albeza Kaçar
# mail: albezaaselbvv@gmail.com
# Cezeri Yeşil Teknoloji MTAL' de
# Yenilenebilir Enerji Sistemleri öğrencisi



"""
    POT            ESP32
  1. pin<---------->3v
  2. pin<---------->adc_pin
  3. pin<---------->gnd
    OLED
    SDA <---------->Pin 19
    SCL <---------->Pin 18
    GND <---------->GND
    Vcc <---------->3V
 
 0x3c OLED ADRESI


oled.contrast(255)    #0-255 degerler arası contrast yapar

"""



from machine import I2C, Pin, ADC   
from time import sleep_ms
import ssd1306


POT_PIN = 32   #adc pin
i=0

i2c0 = I2C(scl=Pin(18), sda=Pin(19), freq=400000)
oled = ssd1306.SSD1306_I2C(128,64,i2c0)

Pot = ADC(Pin(POT_PIN))   
Pot.atten(ADC.ATTN_11DB)

oled.fill(1)   # oledi 1 e boya

while True:
    Pot_Value=Pot.read()   #analog okuma
    
    i = 255-int((Pot_Value*255) / 4095)
    print("Pot_Value=", Pot_Value, "    /     Contrast=", i)
    
    oled.contrast(int(i))
    oled.show()
    
    sleep_ms(1)
    
    
    