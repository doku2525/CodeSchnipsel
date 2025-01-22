import librosa
import matplotlib.pyplot as plt
import numpy as np


def plot_pitch(filename):
    y, sr = librosa.load(filename)
    pitch = librosa.pyin(y=y, fmin=80, fmax=800)[0]
    print(f"{pitch =}")
    # Zeitachse erstellen
    normalized_pitch = (pitch - np.nanmin(pitch)) / (np.nanmax(pitch) - np.nanmin(pitch))
    print(f" {np.min(pitch) = } {np.max(pitch)} {normalized_pitch =}")
    # Glättung (Moving Average)
    window_size = 5
    smoothed_pitch = np.convolve(normalized_pitch, np.ones(window_size) / window_size, mode='valid')
    print(f"{smoothed_pitch =}")

    # plt.plot(normalized_pitch, label='Original')
    plt.plot(smoothed_pitch, label='Smoothed')
    plt.legend()
    plt.show()

    # times = librosa.times_like(smoothed_pitch)
    #
    # # Plot erstellen
    # plt.figure(figsize=(15, 5))
    # plt.plot(times, pitch, label='Pitch')
    # plt.xlabel('Zeit (s)')
    # plt.ylabel('Pitch')
    # plt.title('Pitchverlauf')
    # plt.legend()
    # plt.show()


if __name__ == '__main__':
    plot_pitch("output2.wav")
