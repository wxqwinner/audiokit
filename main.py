"""
main.py Main program entry.

@history
 2021-06-04 wangxq Created.

Copyright (c) 2021~ wangxq.
"""

from audiokit import *


def main():
    wav_file = './data/speech_48k_2_16.wav'
    x, fs = audioread(wav_file)
    sound(x, fs)
    audiowrite('2.wav', x, fs)
    pass


if __name__ == '__main__':
    main()
