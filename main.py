import asyncio
import select
import sys

from hardware.outputs import display

# Set up the poll object
poll_obj = select.poll()
poll_obj.register(sys.stdin, select.POLLIN)


async def main():
    display.lcd_print("Await input ... ", 0)
    await asyncio.sleep(1)

    while True:
        # Wait for input on stdin, waiting for 100 ms
        poll_results = poll_obj.poll(100)
        if poll_results:
            # Read the data from stdin (read data coming from PC)
            data = sys.stdin.readline().strip()
            # Write the data to the input file
            sys.stdout.write("received data: " + data + "\r")
            if len(data) > 0:
                display.lcd_print(data, 1)
        else:
            # do something if no message received (like feed a watchdog timer)
            continue

        await asyncio.sleep(1)


asyncio.run(main())
