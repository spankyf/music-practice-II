import time
import contextlib
with contextlib.redirect_stdout(None):
    from pygame import mixer


def play_finished():
    mixer.init()
    soundObj = mixer.Sound('finished.wav')
    soundObj.play()
    time.sleep(2)  # wait and let the sound play for 1 second
    soundObj.stop()


def play_intermission():
    mixer.init()
    soundObj = mixer.Sound('almost.wav')
    soundObj.play()
    time.sleep(2)  # wait and let the sound play for 1 second
    soundObj.stop()


play_finished()
play_intermission()
