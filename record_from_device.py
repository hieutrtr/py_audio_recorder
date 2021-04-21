import sounddevice as sd
import sys

if __name__ == '__main__':
    duration = round(int(sys.argv[1]))
    print(duration)
    fs = open('soundfile.wav', 'w')
    myrecording = sd.rec(int(duration * 1000), samplerate=fs, channels=2)
    sd.wait()
    sd.play(myrecording, fs)
    sd.wait()