from machine import Pin, SPI
from drivers.st7789.st7789_4bit import *
import gc

TFT_SCLK = 1  # This pin is used to be serial interface clock.
TFT_MOSI = 2  # (SDA) SPI interface output/input pin.
TFT_RST = 42  # This signal will reset the device,Signal is active low.
TFT_DC = 41  # Display data/command selection pin in 4-line serial interface.
TFT_CS = 40  # Chip selection pin, low enable, high disable.
TFT_BL = 39  # Display backlight control pin.

pdc = Pin(TFT_DC, Pin.OUT, value=0)  # Arbitrary pins
pcs = Pin(TFT_CS, Pin.OUT, value=1)
prst = Pin(TFT_RST, Pin.OUT, value=1)
pbl = Pin(TFT_BL, Pin.OUT, value=1)

# Conservative low baudrate. Can go to 62.5MHz.
spi = SPI(2, 62_500_000, sck=Pin(TFT_SCLK), mosi=Pin(TFT_MOSI))
SSD = ST7789
gc.collect()  # Precaution before instantiating framebuf
ssd = SSD(spi, height=240, width=320, dc=pdc, cs=pcs, rst=prst, disp_mode=PORTRAIT)
