import pyaudio
import numpy as np

p = pyaudio.PyAudio()

CONCERT_PITCH = 440  # kammertonen
HALF_INTERVAL = 2 ** (1 / 12)
C_FREQUENCY = CONCERT_PITCH * HALF_INTERVAL ** (-9)
D_FREQUENCY = C_FREQUENCY * HALF_INTERVAL ** (2)
E_FREQUENCY = C_FREQUENCY * HALF_INTERVAL ** (4)
F_FREQUENCY = C_FREQUENCY * HALF_INTERVAL ** (5)
G_FREQUENCY = C_FREQUENCY * HALF_INTERVAL ** (7)
B_FREQUENCY = C_FREQUENCY * HALF_INTERVAL ** (11)
major = [0, 2, 2, 1, 2, 2, 2, 1]
minor = [0, 2, 1, 2, 2, 1, 2, 2]
#print(C_FREQUENCY, D_FREQUENCY, E_FREQUENCY, F_FREQUENCY, G_FREQUENCY, B_FREQUENCY)

def play_tone(frequency, duration, volume=0.3):
    """
    Kode funnet på SO: https://stackoverflow.com/questions/8299303/generating-sine-wave-sound-in-python
    Se også: http://en.wikipedia.org/wiki/Bit_rate#Audio
    """
    sampling_rate = 44100
    global stream
    # generate samples, note conversion to float32 array
    samples = (np.sin(2 * np.pi * np.arange(sampling_rate * duration) * frequency / sampling_rate)).astype(np.float32)
    # for paFloat32 sample values must be in range [-1.0, 1.0]
    stream = p.open(format=pyaudio.paFloat32, channels=1, rate=sampling_rate, output=True)
    # play. May repeat with different volume values (if done interactively)
    stream.write(volume * samples)


def close():
    global stream
    stream.stop_stream()
    stream.close()
    p.terminate()

def get_scale_frequencies(scale, start_frequency):
    frequencies = []
    frequencies.append(round(start_frequency, 3))
    for i in range(1, len(scale)):
        frequencies.append(round(frequencies[i-1] * HALF_INTERVAL ** scale[i], 3))
    return frequencies

def play_song(frequencies, lengths, s):
    if s:
        note = ""
        for i in range(0, len(frequencies)):
            note = frequency_from_note(frequencies[i])
            #print(frequencies[i], note)
            play_tone(note, lengths[i])
    else:
        for i in range(0, len(frequencies)):
            play_tone(frequencies[i], lengths[i])

def frequency_from_note(note):
    if note == 'C':
        return C_FREQUENCY
    elif note == 'D':
        return D_FREQUENCY
    elif note == 'E':
        return E_FREQUENCY
    elif note == 'F':
        return F_FREQUENCY
    elif note == 'G':
        return G_FREQUENCY
    elif note == 'A':
        return CONCERT_PITCH
    elif note == 'B':
        return B_FREQUENCY
    else:
        return "Tone finnes ikke"

def transpose(frequencies, steps):
    transponert = []
    for i in range(0, len(frequencies)):
        transponert.append(round(frequencies[i] * HALF_INTERVAL ** steps, 3))
    return transponert

def frequencies_from_notes(notes):
    freqs = []
    for i in range(0, len(notes)):
        freq = round(frequency_from_note(notes[i][0]), 3)
        faktor = 1
        if "-" in notes[i] and freqs[i-1] <= freq and i != 0:
            faktor = 1/2
        elif "+" in notes[i] and freqs[i-1] >= freq and i != 0:
            faktor = 2
        freqs.append(freq*faktor)
    return freqs

def read_sheet(path):
    f = open(path, "r")
    innhold = f.read()
    print(innhold)
    lst = "".join(innhold.split("\n")).split(" ")
    print(lst)
    tones = []
    lengths = []
    for i in range(0, len(lst)):
        lengths.append(int(lst[i][0]))
        if "+" in lst[i] or "-" in lst[i]:
            if "b" in lst[i]:
                tones.append(lst[i][1] + lst[i][3])
            else:
                tones.append(lst[i][1:3])
        else:
            tones.append(lst[i][1])

        if "b" in lst[i]:
            faktor = 2 ** (1/12*(-1))
    print(tones)
    print(lengths)
    tones = frequencies_from_notes(tones)
    play_song(tones, lengths, False)



read_sheet("song.txt")
#tones, lengths = read_sheet("song.txt")
#play_song(tones, lengths, True)

#bjørnen_sover = ['C', 'C', 'C', 'E', 'D-', 'D', 'D', 'F', 'E-', 'E', 'D-', 'D', 'C-', 'C', 'C+']
#print(frequencies_from_notes(bjørnen_sover))
#tones = ['C', 'D', 'E', 'F', 'G', 'G', 'A', 'A', 'A', 'A', 'G', 'F', 'F', 'F', 'F', 'E', 'E', 'D', 'D', 'D', 'D', 'C']
#lengths = [1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 4, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 4]
#print(get_scale_frequencies(minor, CONCERT_PITCH))
#play_song(get_scale_frequencies(major, C_FREQUENCY), [1, 1, 2, 2, 4, 3, 2, 1])
#play_song([261.626, 293.665, 329.628, 349.228, 391.995], [1, 1, 2, 2, 4])
#print(transpose([261.626, 293.665, 329.628, 349.228, 391.995], 9))
#play_song(tones, lengths, True)
play_tone(440, 4)
#play_song(frequencies_from_notes(bjørnen_sover), [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2], False)

close()