"""
Docstring for pico-send
"""

import time

import pyudev
import usb.core
import usb.util


def wait_for_device():
    """
    Wait for a Raspberry Pi Pico device to be connected using udev events.
    Returns the USB device when found.
    """
    # Check if device is already connected
    dev = usb.core.find(idVendor=0x2E8A, idProduct=0x0005)
    if dev is not None:
        return dev

    print("Waiting for device to be connected...")

    # Set up udev monitoring
    context = pyudev.Context()
    monitor = pyudev.Monitor.from_netlink(context)
    monitor.filter_by(subsystem="usb")

    # Wait for device connection events
    for action, device in monitor:
        if action == "add":
            # Check if the newly added device matches our criteria
            dev = usb.core.find(idVendor=0x2E8A, idProduct=0x0005)
            if dev is not None:
                return dev


def main():
    """
    A function that waits for a raspi pico device 2e8a:0005 to be connected via USB
    and sends "hello pico" to it via the device it is mounted as.
    """
    dev = wait_for_device()
    print("Device found!")

    # # Detach kernel driver if it's active
    # interface = 0
    # if dev.is_kernel_driver_active(interface):
    #     print("Detaching kernel driver...")
    #     dev.detach_kernel_driver(interface)

    # set the active configuration. With no arguments, the first configuration will be the active one
    dev.set_configuration()

    # get an endpoint instance
    cfg = dev.get_active_configuration()
    intf = cfg[(0, 0)]

    ep = usb.util.find_descriptor(
        intf,
        # match the first OUT endpoint
        custom_match=lambda e: usb.util.endpoint_direction(e.bEndpointAddress)
        == usb.util.ENDPOINT_OUT,
    )

    if ep is None:
        print("Error: Could not find OUT endpoint")
        print(f"Available endpoints in interface:")
        for endpoint in intf:
            print(
                f"  Address: 0x{endpoint.bEndpointAddress:02x}, Direction: {usb.util.endpoint_direction(endpoint.bEndpointAddress)}"
            )
        return

    # Wait for device to be ready
    print("Waiting for device to be ready...")
    max_retries = 10
    for i in range(max_retries):
        try:
            # Try to get device status - if it succeeds, device is ready
            dev.is_kernel_driver_active(0)
            time.sleep(0.5)
            break
        except usb.core.USBError:
            time.sleep(0.5)
            if i == max_retries - 1:
                print("Device not ready after maximum retries")
                return

    # write the data
    msg = b"hello pico\n"
    ep.write(msg)
    print(f"Sent message: {msg.decode().strip()}")

    # give the device some time to process
    time.sleep(1)


if __name__ == "__main__":
    main()
