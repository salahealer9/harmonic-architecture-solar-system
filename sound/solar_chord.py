import matplotlib
matplotlib.rcParams["pdf.fonttype"] = 42
matplotlib.rcParams["ps.fonttype"] = 42

import numpy as np
import os
import wave
import struct
import matplotlib.pyplot as plt

# =============================================================================
# THE SOLAR CHORD
# Exact frequency realisation of the Silver Ratio Harmonic Framework
# Earth = 252 Hz (digit sum 9), 10-semitone octave from Celtic Cross geometry
# Author: Salah-Eddin Gherbi — companion script to Scala Harmonica (2026)
# =============================================================================

# --- Planetary frequencies (digit sum 9 throughout) -----------------------
planets = [
    ("Mercury",  90,   "Major 9th below Earth",      "#888899"),
    ("Venus",   180,   "Perfect 4th below Earth",    "#ddcc88"),
    ("Earth",   252,   "Unison — the tonic",         "#3399cc"),
    ("Mars",    396,   "Tritone — diabolus in musica","#dd4444"),
    ("Harmonia",540,   "Major 7th — the leading tone","#ddbb33"),
    ("Jupiter", 1305,  "2 octaves above Earth",      "#dd9933"),
    ("Saturn",  2394,  "2 octaves + Major 3rd",      "#ccbb77"),
    ("Uranus",  4842,  "3 octaves above Earth",      "#33bbdd"),
    ("Neptune", 7605,  "3 octaves + Major 3rd",      "#3344aa"),
    ("Pluto",   9972,  "4 octaves above Earth",      "#aaaaaa"),
]

SAMPLE_RATE = 44100   # Hz
FADE        = 0.15    # seconds for fade in/out

# =============================================================================
# HELPER — generate one sine wave with amplitude envelope
# =============================================================================
def sine_wave(freq, duration, amplitude=1.0, sample_rate=SAMPLE_RATE):
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    wave_data = amplitude * np.sin(2 * np.pi * freq * t)

    # Fade in and fade out to avoid clicks
    fade_samples = int(FADE * sample_rate)
    fade_in  = np.linspace(0, 1, fade_samples)
    fade_out = np.linspace(1, 0, fade_samples)

    wave_data[:fade_samples]  *= fade_in
    wave_data[-fade_samples:] *= fade_out

    return wave_data

# =============================================================================
# HELPER — write numpy array to 16-bit WAV
# =============================================================================
def write_wav(filename, data, sample_rate=SAMPLE_RATE):
    # Normalise to 16-bit range with headroom
    peak = np.max(np.abs(data))
    if peak > 0:
        data = data / peak * 0.85
    data_int = (data * 32767).astype(np.int16)

    with wave.open(filename, 'w') as wf:
        wf.setnchannels(1)
        wf.setsampwidth(2)
        wf.setframerate(sample_rate)
        wf.writeframes(data_int.tobytes())

    print(f"  Saved: {filename}")

# =============================================================================
# FILE 1 — INDIVIDUAL PLANET TONES
# Each planet as a 5-second solo tone, sequential with 1 second silence between
# =============================================================================
print("\n--- Generating individual planet tones ---")

tone_duration  = 5.0   # seconds per planet
silence_duration = 1.0 # seconds between planets

all_tones = np.array([])
for name, freq, interval, colour in planets:
    tone    = sine_wave(freq, tone_duration, amplitude=0.7)
    silence = np.zeros(int(SAMPLE_RATE * silence_duration))
    all_tones = np.concatenate([all_tones, tone, silence])
    print(f"  {name:10s}  {freq:5d} Hz  —  {interval}")

file_path = os.path.expanduser("~/scala_harmonica/music/solar_planets_sequential.wav")
os.makedirs(os.path.dirname(file_path), exist_ok=True)
write_wav(file_path, all_tones)

# =============================================================================
# FILE 2 — THE SOLAR CHORD (all planets simultaneously)
# Building up one planet at a time, then full chord held, then fading down
# =============================================================================
print("\n--- Generating Solar chord build-up ---")

build_duration  = 3.0   # seconds per planet added
hold_duration   = 10.0  # seconds full chord held
fadedown_duration = 3.0 # seconds each planet removed

# Amplitude scaling — reduce higher frequencies to balance perception
# Human hearing is most sensitive in the 1-5 kHz range so we reduce those
def perceptual_amplitude(freq):
    """Rough perceptual balancing so all planets are heard equally."""
    if freq < 200:
        return 0.90
    elif freq < 500:
        return 0.85
    elif freq < 2000:
        return 0.70
    elif freq < 5000:
        return 0.45
    else:
        return 0.25

# Build up — add one planet at a time
chord_parts = []
cumulative_time = 0.0

# Generate the full duration for each planet's contribution
total_duration = (len(planets) * build_duration) + hold_duration + (len(planets) * fadedown_duration)
full_samples   = int(SAMPLE_RATE * total_duration)
chord_signal   = np.zeros(full_samples)

# Add each planet's tone starting at its entry point
for i, (name, freq, interval, colour) in enumerate(planets):
    entry_time   = i * build_duration
    entry_sample = int(entry_time * SAMPLE_RATE)

    # This planet sounds from entry to end of hold, then fades in fadedown
    planet_duration = total_duration - entry_time
    amp = perceptual_amplitude(freq)
    tone = sine_wave(freq, planet_duration, amplitude=amp)

    # Fade out during the fadedown phase for this planet
    # Planets fade out in reverse order (Pluto first, Mercury last)
    fadeout_start_time = (len(planets) * build_duration) + hold_duration + ((len(planets) - 1 - i) * fadedown_duration)
    fadeout_start_sample = int(fadeout_start_time * SAMPLE_RATE) - entry_sample
    fadeout_samples = int(fadedown_duration * SAMPLE_RATE)

    if fadeout_start_sample > 0 and fadeout_start_sample < len(tone):
        end_sample = min(fadeout_start_sample + fadeout_samples, len(tone))
        actual_fade_len = end_sample - fadeout_start_sample
        tone[fadeout_start_sample:end_sample] *= np.linspace(1, 0, actual_fade_len)
        if end_sample < len(tone):
            tone[end_sample:] = 0

    # Add to chord signal
    end_sample_in_chord = entry_sample + len(tone)
    if end_sample_in_chord <= full_samples:
        chord_signal[entry_sample:end_sample_in_chord] += tone
    else:
        chord_signal[entry_sample:] += tone[:full_samples - entry_sample]

    print(f"  {name:10s} enters at {entry_time:5.1f}s  —  {freq} Hz")

file_path = os.path.expanduser("~/scala_harmonica/music/solar_chord_buildup.wav")
os.makedirs(os.path.dirname(file_path), exist_ok=True)
write_wav(file_path, chord_signal)

# =============================================================================
# FILE 3 — HARMONIA SOLO (the leading tone alone — Movement 2)
# 30 seconds of Harmonia's frequency with slow breathing amplitude
# =============================================================================
print("\n--- Generating Harmonia solo tone ---")

harmonia_freq = 540
duration      = 30.0
t = np.linspace(0, duration, int(SAMPLE_RATE * duration), endpoint=False)

# Slow breathing amplitude — like a sustained bow stroke
breath_rate = 0.12  # Hz — one breath every ~8 seconds
amplitude   = 0.7 * (0.75 + 0.25 * np.sin(2 * np.pi * breath_rate * t))

# Add slight vibrato
vibrato_rate  = 5.5   # Hz
vibrato_depth = 0.003 # semitones — very subtle
freq_variation = harmonia_freq * (1 + vibrato_depth * np.sin(2 * np.pi * vibrato_rate * t))
harmonia_tone  = amplitude * np.sin(2 * np.pi * np.cumsum(freq_variation) / SAMPLE_RATE)

# Fade in and out
fade_samples = int(FADE * SAMPLE_RATE)
harmonia_tone[:fade_samples]  *= np.linspace(0, 1, fade_samples)
harmonia_tone[-fade_samples:] *= np.linspace(1, 0, fade_samples)

# Add faint overtone — the ghost of the resolution
overtone_freq = harmonia_freq * 2  # one octave up — toward Jupiter
overtone = 0.08 * np.sin(2 * np.pi * overtone_freq * t)
overtone[:fade_samples]  *= np.linspace(0, 1, fade_samples)
overtone[-fade_samples:] *= np.linspace(1, 0, fade_samples)

harmonia_signal = harmonia_tone + overtone
file_path = os.path.expanduser("~/scala_harmonica/music/harmonia_solo.wav")
os.makedirs(os.path.dirname(file_path), exist_ok=True)
write_wav(file_path, harmonia_signal)
print(f"  Harmonia solo: {harmonia_freq} Hz with vibrato and ghost overtone at {overtone_freq} Hz")

# =============================================================================
# VISUALISATION — The Solar Chord Frequency Map
# =============================================================================
print("\n--- Generating frequency map visualisation ---")

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 7), facecolor='#080818')

# Left panel — frequency ladder
ax1.set_facecolor('#080818')
ax1.set_title("The Solar Chord — Frequency Ladder",
              color='#e8e8f0', fontsize=13, fontfamily='serif', pad=15)

freqs  = [p[1] for p in planets]
names  = [p[0] for p in planets]
colors = [p[3] for p in planets]

for i, (name, freq, interval, color) in enumerate(planets):
    # Horizontal line
    ax1.axhline(y=np.log2(freq), color=color, alpha=0.3, linewidth=0.8, linestyle='--')
    # Dot
    ax1.scatter(0.5, np.log2(freq), color=color, s=120 if name == "Harmonia" else 60,
                zorder=5, edgecolors='white' if name == "Harmonia" else 'none',
                linewidths=1.5 if name == "Harmonia" else 0)
    # Label
    label = f"{name}  —  {freq} Hz"
    if name == "Harmonia":
        label += "  * MISSING"
    ax1.text(0.6, np.log2(freq), label,
             color=color, fontsize=9.5, va='center', fontfamily='serif')

ax1.set_xlim(0, 2)
ax1.set_ylim(np.log2(80), np.log2(11000))
ax1.set_yticks([np.log2(f) for f in freqs])
ax1.set_yticklabels([f"{f} Hz" for f in freqs], color='#888899', fontsize=8)
ax1.set_xticks([])
ax1.spines['top'].set_visible(False)
ax1.spines['right'].set_visible(False)
ax1.spines['bottom'].set_visible(False)
ax1.spines['left'].set_color('#2a2a3e')
ax1.tick_params(axis='y', colors='#2a2a3e')

# Octave markers
for octave in [1, 2, 3, 4]:
    freq_earth = 252
    octave_freq = freq_earth * (2 ** octave)
    if octave_freq < 11000:
        ax1.axhline(y=np.log2(octave_freq), color='#2a2a3e',
                    alpha=0.8, linewidth=0.5, linestyle=':')
        ax1.text(1.85, np.log2(octave_freq), f"octave {octave}",
                 color='#2a2a3e', fontsize=7, va='center', ha='right')

# Right panel — digit sum verification
ax2.set_facecolor('#080818')
ax2.set_title("Digit Sum Verification — All Frequencies Sum to 9",
              color='#e8e8f0', fontsize=13, fontfamily='serif', pad=15)

for i, (name, freq, interval, color) in enumerate(planets):
    digits = [int(d) for d in str(freq)]
    digit_sum = sum(digits)
    while digit_sum > 9:
        digit_sum = sum([int(d) for d in str(digit_sum)])

    y = len(planets) - i
    ax2.barh(y, digit_sum, color=color, alpha=0.7, height=0.6)
    ax2.text(-0.3, y, f"{name}", color=color, fontsize=9.5,
             va='center', ha='right', fontfamily='serif')
    ax2.text(digit_sum + 0.1, y,
             f"{freq} Hz  →  {' + '.join(str(d) for d in digits)} = {sum(digits) if sum(digits) <= 9 else sum(digits)} → {digit_sum}",
             color='#e8e8f0', fontsize=8.5, va='center', fontfamily='serif')

ax2.axvline(x=9, color='#ddbb33', linewidth=1.5, linestyle='--', alpha=0.8)
ax2.text(9.1, 0.3, "= 9", color='#ddbb33', fontsize=11, fontfamily='serif')
ax2.set_xlim(-4, 18)
ax2.set_ylim(0, len(planets) + 1)
ax2.set_xticks([])
ax2.set_yticks([])
ax2.spines['top'].set_visible(False)
ax2.spines['right'].set_visible(False)
ax2.spines['bottom'].set_visible(False)
ax2.spines['left'].set_visible(False)

plt.suptitle("The Solar Chord — Silver Ratio Harmonic Framework\nEarth = 252 Hz  |  All frequencies have digit sum 9  |  Scala Harmonica (2026)",
             color='#ddbb33', fontsize=11, fontfamily='serif', y=0.02)

plt.tight_layout(rect=[0, 0.06, 1, 1])
pdf_path = os.path.expanduser("~/scala_harmonica/music/solar_chord_frequency_map.pdf")
png_path = os.path.expanduser("~/scala_harmonica/music/solar_chord_frequency_map.png")
os.makedirs(os.path.dirname(pdf_path), exist_ok=True)
plt.savefig(pdf_path, bbox_inches='tight', facecolor='#080818', pad_inches=0.1)
plt.savefig(png_path, dpi=300, bbox_inches='tight', facecolor='#080818', pad_inches=0.1)
plt.close()
print("  Saved: solar_chord_frequency_map.pdf and .png")

print("\n=== All files generated successfully ===")
print("\nOutput files:")
print("  solar_planets_sequential.wav  — each planet's tone played one by one")
print("  solar_chord_buildup.wav       — Solar chord building up planet by planet")
print("  harmonia_solo.wav             — Harmonia's leading tone alone with vibrato")
print("  solar_chord_frequency_map.pdf — frequency ladder and digit sum visualisation")
print("  solar_chord_frequency_map.png — same at 300 DPI")

