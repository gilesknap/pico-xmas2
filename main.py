import asyncio

# repetition - could get a bit more clever with module manipulation here
import modes.mode0 as mode0
import modes.mode1 as mode1
import modes.mode2 as mode2
import modes.mode3 as mode3
from hardware.inputs import dips, environment, green_button, red_button, slider
from hardware.outputs import (
    big_red_led,
    buzzer,
    rgb_led1,
    rgb_led2,
    rgb_ring,
    rgb_strand,
    segmented,
)

modes = [mode0, mode1, mode2, mode3]

# list all outputs we want to control in stop and poll functions
outputs = [rgb_led1, rgb_led2, rgb_ring, rgb_strand, segmented, buzzer]

# global to track if the program is running
running = True


def stop(_):
    global running
    for output in outputs:
        # using duck typing here - really ought to create a class hierarchy!
        output.stop()
    running = False


# global poll function - default poll behaviour for most modes
# updates the interval from the slider
def poll():
    val = int(slider.value * 250)
    for output in outputs:
        # duck typing again
        output.period_ms = val
    return val


# arrays of go, poll and stop functions for each mode]
gos = [mode0.go, mode1.go, mode2.go, mode3.go]
polls = [poll, poll, poll, poll]
stops = [stop, stop, stop, stop]


async def main():
    # use the global running variable to terminate the program
    global running

    # set up a heartbeat to show the code is running - same for all modes
    big_red_led.blink(500)

    while True:
        print("\n\nSelect mode with DIP switches and press green button to start")
        print("modes:")
        for i, m in enumerate(modes):
            print(f"{i}: {m.description}")

        # wait for the green button to be pressed to start the program
        await green_button().wait_for_press()
        # get the mode from the DIP switches
        mode = dips.value

        if mode >= len(gos):
            print(f"\n ERROR: Please set dip switches between 0 and {len(gos) - 1}")
            # go back to start of while loop
            continue
        else:
            print(f"\nStarting mode {mode}: {modes[mode].description}")

        running = True
        gos[mode]()

        # set the red button to stop the program
        red_button(callback=stops[mode])

        # check environment
        print()
        environment.measurements()

        while running:
            polls[mode]()
            await asyncio.sleep(0.1)


asyncio.run(main())
