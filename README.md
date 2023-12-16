# pico-xmas 2023 Alternative Advent Calendar Project

giles' final project for the RaspberryPi Pico from the XMas Advent
Calendar 2023.

This one project endeavours to include all of the components from the
2023 PiHut XMas Advent Calendar.

See [PiHut Calendar 2023 Guides](https://thepihut.com/pages/maker-advent-2023-guides)

Click the image below for a video of the final version of the project.

[![image](https://github.com/gilesknap/pico-xmas2/assets/964827/2cc1b1c8-6536-4c89-ae70-3180e0974a34)](https://photos.app.goo.gl/Pukf7e8uYN1kK16x9 "Let It Glow Advent Calenar")

## Setup

First you need to wire all your components together. I used a couple of extras:

- an extra breadboard from last years calendar, this is required as there is
  not enough room otherwise. You can buy these for a few pounds in the UK.
- the piezoelectric buzzer from the 2022 calendar, this is not required but
  but it allows you to play a christmas tune while viewing the lights.

Here is a wiring diagram:

![Wiring Diagram](board/Advent2023.excalidraw.svg)

And here is a picture of the setup to help interpret the above:

![image](https://github.com/gilesknap/pico-xmas2/assets/964827/8c77d835-c7dc-4d6f-b013-b9dfe5ffd60e)

## What the Code can do

So the idea here is that you can pick the 'mode' by setting the dip switches and
start and stop the code using the green and red buttons respectively. You can
also use the slider to speed up or slow down operation.

The code is structured using modules and classes for reusability. It also uses
asyncio for parallel operation so that it can drive all of the output devices and
monitor all of the input devices simultaneously.

I have written 4 'modes' so far,  I will be accepting PRs to add some more if anyone
feels like contributing.

I was considering some games where you have to repeat sequences etc.

Current modes are as follows: (note you need to use binary to select them!):

```
Select mode with DIP switches and press green button to start
modes:
0: Colour Cycle
1: Colour Fading Loops
2: Colour Cycle with Music
3: Colour Fading Loops with Music
```

## How to get the code

Todo: I'll add some simple instructions for getting this project onto your pico.
Expect these to be doen at the latest Sun 17th December 2023!

## Todo

Also I still have the final day's item to add onto the board!


