"""
Docstring for pico-send
"""

import time

import pyudev
import serial
import serial.tools.list_ports


def check_for_pico():
    # Check if a pico is connected
    ports = serial.tools.list_ports.comports()
    for port in ports:
        if port.vid == 0x2E8A and port.pid == 0x0005:
            return port.device
    return None


def wait_for_device():
    """
    Wait for a Raspberry Pi Pico device to be connected using udev events.
    Returns the serial port path when found.
    """
    # Check if device is already connected
    device = check_for_pico()

    while not device:
        print("Waiting for device to be connected...")

        # Set up udev monitoring
        context = pyudev.Context()
        monitor = pyudev.Monitor.from_netlink(context)
        monitor.filter_by(subsystem="tty")

        # Wait for device connection events
        for action, device in monitor:
            if action == "add":
                device = check_for_pico()

    return device


def main():
    """
    A function that waits for a raspi pico device 2e8a:0005 to be connected via USB
    and sends "hello pico" to it via the serial port.
    """
    port_path = wait_for_device()
    print(f"Device found on {port_path}!")

    # Open serial connection
    try:
        ser = serial.Serial(port_path, baudrate=115200, timeout=1)
        time.sleep(2)  # Give the device time to initialize

        # Clear any pending data
        ser.reset_input_buffer()
        ser.reset_output_buffer()

        # Send the message
        msg = b"hello pico\n"
        ser.write(msg)
        print(f"Sent message: {msg.decode().strip()}")

        # Wait for and read response if any
        time.sleep(0.5)
        if ser.in_waiting > 0:
            response = ser.read(ser.in_waiting)
            print(f"Response: {response.decode(errors='ignore').strip()}")

        ser.close()

    except serial.SerialException as e:
        print(f"Error opening serial port: {e}")
        return


if __name__ == "__main__":
    main()
