from hardware.outputs import buzzer
from modes.mode1 import go as go1
from music.merry_xmas import wish_you_a_merry_xmas

description = "Fading+Music"


def go():
    buzzer.play_tune(wish_you_a_merry_xmas, repeat=1)
    go1()
