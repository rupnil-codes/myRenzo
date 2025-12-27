import json
import os
import time

import pyaudio
import numpy as np
from silero_vad import load_silero_vad, read_audio, get_speech_timestamps
import wave

from transcription import transcribe_audio
import config

## Parameters

CHUNK = 256
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 16000

SILENCE_DURATION = 1.5 # Silence duration in seconds
NOISE_SENSITIVITY = 1500

FOLDER = "recordings"
