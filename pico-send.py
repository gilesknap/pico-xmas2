"""
A script to send the MAC address of the host machine to a connected Raspberry
Pi Pico device via USB serial communication. The script waits for the device to
be connected and sends the message once connected.
"""

import pyudev
import serial
import serial.tools.list_ports

pico_vid = 0x2E8A  # Raspberry Pi Pico Vendor ID
pico_pid = 0x0005  # Pico with MicroPython firmware


def get_mac_address() -> str:
    import uuid

    mac = uuid.getnode()
    mac_str = ":".join(
        ["{:02x}".format((mac >> ele) & 0xFF) for ele in range(0, 8 * 6, 8)][::-1]
    )
    return mac_str


def check_for_pico():
    # Check if a pico is connected
    ports = serial.tools.list_ports.comports()
    for port in ports:
        if port.vid == pico_vid and port.pid == pico_pid:
            print("Pico found!")
            return port.device
    return None


def wait_for_device():
    """
    Wait for a Raspberry Pi Pico device to be connected using udev events.
    Returns the serial port path when found.
    """

    # Set up udev monitoring
    context = pyudev.Context()
    monitor = pyudev.Monitor.from_netlink(context)
    monitor.filter_by(subsystem="tty")

    while True:
        print("Waiting for device to be connected...")

        # Wait for device connection events
        for action, device in monitor:
            if action == "add":
                print(f"Device added: {device.device_node}")
                device = check_for_pico()
                if device is not None:
                    return device


def send_message(port_path: str, message: str):
    try:
        # Open serial connection
        ser = serial.Serial(port_path, baudrate=115200, timeout=1)

        # Clear any pending data
        ser.reset_output_buffer()

        # Send the message
        ser.write(message.encode())
        print(f"Sent message: {message}")

        ser.close()

    except serial.SerialException as e:
        print(f"Error opening serial port: {e}")


def main():
    """
    A function that waits for a raspi pico device 2e8a:0005 to be connected via USB
    and sends the current MAC address to it via the serial port.
    """
    msg = (get_mac_address() + "\n").replace(":", "")

    port_path = check_for_pico()
    if port_path is not None:
        send_message(port_path, msg)

    while True:
        port_path = wait_for_device()
        send_message(port_path, msg)


if __name__ == "__main__":
    main()
