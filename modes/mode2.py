from hardware.outputs import buzzer
from modes.mode0 import go as go0
from music.merry_xmas import wish_you_a_merry_xmas

description = "Flash+Music"


def go():
    buzzer.play_tune(wish_you_a_merry_xmas, repeat=2)
    go0()
