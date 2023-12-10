import asyncio

import modes.mode1 as mode1
from hardware.inputs import dips, environment, green_button, red_button, slider
from hardware.outputs import (
    big_red_led,
    rgb_led1,
    rgb_led2,
    rgb_ring,
    rgb_strand,
    segmented,
)

# list all outputs we want to control in stop and poll functions
outputs = [rgb_led1, rgb_led2, rgb_ring, rgb_strand, segmented]

# global to track if the program is running
running = True


def stop(_):
    for output in outputs:
        # using duck typing here - really ought to create a class hierarchy!
        # (but type checking in MicroPython is a bit limited so let's leave it)
        output.stop()


# global poll function - default poll behaviour for most modes
# updates the interval from the slider
def poll():
    val = int(slider.value * 250)
    for output in outputs:
        # duck typing again
        output.period_ms = val
    return val


# arrays of go, tick and stop functions for each mode]
gos = [mode1.go, mode1.go]
polls = [poll, poll]
stops = [stop, stop]


async def main():
    # use the global running variable to terminate the program
    global running

    while True:
        # set up a heartbeat to show the code is running - same for all modes
        big_red_led.blink(500)

        # wait for the green button to be pressed to start the program
        await green_button().wait_for_press()
        # get the mode from the DIP switches
        mode = dips.value

        if mode >= len(gos):
            print(f"Invalid mode, please set dip switches between 0 and {len(gos) - 1}")
            # go back to start of while loop
            continue

        running = True
        gos[mode]()

        # set the red button to stop the program
        red_button(callback=stops[mode])

        # check environment
        environment.measurements()

        while running:
            polls[mode]()
            await asyncio.sleep(0.1)


asyncio.run(main())
