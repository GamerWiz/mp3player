import pyaudio
import wave
import threading

CHUNK = 1024


def playSong():
    stream.start_stream()


def pausePlay():
    while(True):
        input1 = input()
        if input1 == "p":
            if stream.is_active():
                stream.stop_stream()
            elif stream.is_stopped():
                stream.start_stream()


p = pyaudio.PyAudio()


def callback(in_data, frame_count, time_info, status):
    data = mtr.readframes(frame_count)
    return (data, pyaudio.paContinue)


mtr = wave.open("Miss The Rage Extended.wav")


stream = p.open(format=p.get_format_from_width(mtr.getsampwidth()),
                channels=mtr.getnchannels(),
                rate=mtr.getframerate(),
                output=True,
                stream_callback=callback)

pausePlayThread = threading.Thread(target=pausePlay, name="pauseplay")
initThread = threading.Thread(target=playSong, name="playSong")

pausePlayThread.start()
print("pp thread started!")
initThread.start()
print("initThread started!")
