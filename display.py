import machine
from machine import I2C

from lib.pico_i2c_lcd import I2cLcd

# Define LCD I2C pins/BUS/address
SDA = 16
SCL = 17
I2C_BUS = 0
LCD_ADDR = 0x27

# Define LCD rows/columns
LCD_NUM_ROWS = 2
LCD_NUM_COLS = 16

# Set up LCD I2C
lcd_i2c = I2C(I2C_BUS, sda=machine.Pin(SDA), scl=machine.Pin(SCL), freq=400000)
lcd = I2cLcd(lcd_i2c, LCD_ADDR, LCD_NUM_ROWS, LCD_NUM_COLS)

last_line = 0


# Show a string on the LCD
def lcd_print(line):
    global last_line
    lcd.move_to(0, last_line)
    lcd.putstr(f"{line:16}")
    last_line = 1 if last_line == 0 else 0
