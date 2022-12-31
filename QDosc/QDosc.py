# CQO-EM by #CQD-AU

# to run, use this example - python QDosc.py 44100 1 48000 output.wav


import argparse
import math
import numpy as np
import wave

def quartz_oscillator(frequency, duration, sample_rate):
    # Calculate the number of samples needed based on the duration and sample rate
    num_samples = int(duration * sample_rate)
    
    # Generate an array of time values, with a spacing between samples equal to the reciprocal of the sample rate
    t = np.linspace(0, duration, num_samples, endpoint=False)
    
    # Generate a sine wave with the specified frequency
    y = np.sin(2 * math.pi * frequency * t)
    
    return y

# Parse command-line arguments
parser = argparse.ArgumentParser(description='Generate a clear quartz oscillator signal')
parser.add_argument('frequency', type=int, help='Frequency of the oscillator in Hertz')
parser.add_argument('duration', type=float, help='Duration of the signal in seconds')
parser.add_argument('sample_rate', type=int, help='Sample rate of the signal in Hertz')
parser.add_argument('output_file', help='Name of the output wave file')
args = parser.parse_args()

# Generate the oscillator signal
signal = quartz_oscillator(args.frequency, args.duration, args.sample_rate)

# Save the signal as a raw wave file
with wave.open(args.output_file, 'wb') as wav_file:
    # Set the wave file parameters
    wav_file.setnchannels(1) # 1 channel (mono)
    wav_file.setsampwidth(2) # 2 bytes per sample
    wav_file.setframerate(args.sample_rate) # Sample rate
    
    # Write the signal data to the wave file
    wav_file.writeframes(signal.tobytes())

