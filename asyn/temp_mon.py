from machine import I2C, Pin

from lib.dht20 import DHT20


class TempMon:
    """
    A class to represent a DHT20 temperature and humidity sensor attached to
    an I2C bus on the Pico.

    Asynchronous monitoring could be supported. (TODO)
    """

    def __init__(self, i2c1_sda: int, i2c1_sdc: int):
        # Set up I2C pins
        sda = Pin(i2c1_sda)
        scl = Pin(i2c1_sdc)
        # Set up I2C
        self._i2c = I2C(1, sda=sda, scl=scl)

        # Set up DHT20 device with I2C address
        self.dht20 = DHT20(0x38, self._i2c)
        self._print = print

    def set_print(self, print):
        self._print = print

    def measurements(self):
        measurements = self.dht20.measurements

        # Print the data
        self._print(f"Temp: {round(measurements['t'],1)}")
        self._print(f"Humid: {round(measurements['rh'],1)}%")
