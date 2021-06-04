from audiokit import *

if __name__ == '__main__':
    wav_file = './data/speech_48k_2_16.wav'
    x, fs = audioread(wav_file)
    sound(x, fs)
    audiowrite('2.wav', x, fs)
    pass
