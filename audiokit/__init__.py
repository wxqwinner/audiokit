"""
audiokit.py Audio toolkit.

@history
 2021-06-04 wangxq Created.

Copyright (c) 2021~ wangxq.
"""

import os

import numpy as np
import pyaudio
from pydub import AudioSegment
from audiokit.utils import get_format

"""
shape = (batchsize \ num_frame, channels, monolen)
"""

__version__ = '0.0.2'


def audioread(filename, samples=None, dtype=np.float64) -> tuple:
    format = get_format(filename)
    sound = AudioSegment.from_file(filename, format=format)

    if sound.sample_width == 2:
        dtype = np.int16
        max_sample = 32768
    elif sound.sample_width == 4:
        dtype = np.int32
        max_sample = 2147483648

    data = sound.raw_data
    y = np.frombuffer(data, dtype=dtype)
    y = y / max_sample
    y = np.reshape(y, (-1, sound.channels)).T
    fs = sound.frame_rate

    return y, fs


def audiowrite(filename: str, y:np.ndarray, fs:int, **kwargs):
    format = get_format(filename)
    channels = y.shape[0]
    y = (y*32767).astype(np.int16).T
    data = y.tobytes()
    sound = AudioSegment(
        data=data, # raw audio data (bytes)
        sample_width=2, # 2 byte (16 bit) samples
        frame_rate=fs,
        channels=channels
    )

    sound.file_handle = sound.export(filename, format=format)


def sound(y: np.ndarray, fs: int=8000, bits: int=16, **kwargs) -> bool:
    framesize_ms = 10
    framesize = fs * framesize_ms // 1000
    channels = y.shape[0]
    ylen = y.shape[1]
    y = (y * 32767).astype(np.int16).T

    p = pyaudio.PyAudio()
    stream = p.open(
                format=p.get_format_from_width(bits//8),
                channels=channels,
                rate=fs,
                output=True)

    pin = 0
    while True:
        if pin+framesize > ylen-1:
            data = y[pin:ylen-1, :]
            stream.write(data.tobytes())
            break
        data = y[pin:pin+framesize, :]
        stream.write(data.tobytes())
        pin += framesize

    stream.stop_stream()
    stream.close()
    p.terminate()


def list_devices():
    pass
