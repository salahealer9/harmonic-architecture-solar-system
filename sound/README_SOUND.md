# 🎵 The Solar Chord — Audio Exploration

> **Note:** The contents of this folder are **not part of the peer-deposited research paper** and do not form part of the Silver Ratio Harmonic Framework's scientific claims. They represent an independent creative and mathematical exploration of the framework's musical dimension, developed as a companion to the article *Harmonia — The Missing Note in the Solar Symphony* (Gherbi, 2026).
>
> The research paper and its companion scripts are in [`v3.0/scripts/`](../scripts/).

---

## Overview

The Silver Ratio Harmonic Framework predicts planetary orbital distances using rational functions of the Silver Ratio δS = 1 + √2, derived from the geometry of the Celtic Cross. When those distances are expressed logarithmically relative to Earth's orbit using the formula:

**10 × log₂(a / a⊕)**

...the planets map onto a coherent musical scale — a 10-semitone geometric octave derived from the same Celtic Cross ratios that govern the orbital predictions. This is not a metaphor. The intervals are calculated from the same mathematics as the framework itself.

This folder contains Python scripts and the audio files they generate, realising the Solar chord as exact audible frequencies — with Earth tuned to **252 Hz** (digit sum 9) as the tonic.

---

## The Planetary Frequencies

All ten frequencies have a digit sum of 9 and fall within 0.17% of the mathematically calculated values — well within the framework's 0.72% mean orbital error.

| Planet | Frequency (Hz) | Digit Sum | Musical Interval |
|---|---|---|---|
| Mercury | 90 | 9 | Major 9th below Earth |
| Venus | 180 | 9 | Perfect 4th below Earth |
| **Earth** | **252** | **9** | **Unison — the tonic** |
| Mars | 396 | 9 | Tritone — *diabolus in musica* |
| **Harmonia** | **540** | **9** | **Major 7th — the leading tone — MISSING** |
| Jupiter | 1305 | 9 | 2 octaves above Earth |
| Saturn | 2394 | 9 | 2 octaves + Major 3rd |
| Uranus | 4842 | 9 | 3 octaves above Earth |
| Neptune | 7605 | 9 | 3 octaves + Major 3rd |
| Pluto | 9972 | 9 | 4 octaves above Earth |

**Harmonia at 540 Hz** — the predicted missing body at 2.14 AU — falls at the Major 7th interval above Earth. In Western harmony, the Major 7th is the leading tone: the most restless note in the scale, creating irresistible harmonic tension toward the octave above it. Harmonia should resolve upward to Jupiter at 1305 Hz — but the asteroid belt is all that remains.

The Solar Symphony has been playing a suspended chord for billions of years. The asteroid belt is the silence where B should be.

---

## The Musical Scale

Musical intervals are calculated as **10 × log₂(a / a⊕)**, where a⊕ = 1 AU (Earth's orbit). Ten semitones make one octave in this geometric scale — a custom temperament derived from the Celtic Cross ratios, not standard 12-tone equal temperament.

This scale is discussed in full in Chapter 6 of *Scala Harmonica: The Geometry of Planetary Resonance* (Gherbi, 2026), Tables 7 and 8.

---

## Files in This Folder

| File | Description |
|---|---|
| `solar_chord.py` | Python script by Salah-Eddin Gherbi — generates WAV audio files and the frequency map visualisation using pure sine wave synthesis |
| `solar_chord_instruments.py` | Python script contributed by Michiel — extends the framework with orchestral instrument voices using FluidSynth and the Arachno SoundFont |
| `solar_chord_buildup.wav` | The Solar chord building planet by planet — Mercury enters first, each planet adds every 3 seconds, full chord held, then fades out in reverse order. Total ~90 seconds. |
| `solar_planets_sequential.wav` | Each planet's frequency played individually for 5 seconds with 1 second silence between — Mercury to Pluto in order. |
| `harmonia_solo.wav` | Harmonia's leading tone at 540 Hz alone for 30 seconds — with slow breathing amplitude, subtle vibrato, and a faint ghost overtone at 1080 Hz (the Jupiter octave it reaches toward but never arrives at). |
| `solar_chord_frequency_map.pdf` | Frequency ladder visualisation showing all ten planetary frequencies on a logarithmic scale with digit sum verification. |
| `solar_chord_frequency_map.png` | Same at 300 DPI. |

---

## How to Run `solar_chord.py` (Sine Wave Generator)

**Requirements:** Python 3.x, numpy, scipy (standard libraries wave and struct are used for audio output — no additional audio dependencies required).

```bash
cd sound
python solar_chord.py
```

The script generates all five output files in the working directory. Runtime is approximately 10–15 seconds.

**To install dependencies if needed:**
```bash
pip install numpy scipy
```

---

## How to Run `solar_chord_instruments.py` (Instrument Orchestration)

*Contributed by Michiel (2026), extending the planetary frequency framework with orchestral instrument voices.*

**Requirements:** Python 3.x, pyfluidsynth, FluidSynth, PulseAudio, and the [Arachno SoundFont](https://www.arachnosoft.com/main/soundfont.php) (Arachno.sf2 — place in the same directory as the script).

```bash
pip install pyfluidsynth
cd sound
python solar_chord_instruments.py
```

The script presents an interactive menu of eight presets — each assigns a different instrument voice to each planet while preserving the exact mathematical frequencies of the Silver Ratio Harmonic Framework:

| Preset | Name | Character |
|---|---|---|
| 1 | Ethereal Balance | Intense — Church Organ, Ice Rain, Glockenspiel |
| 2 | Pluto's Song | Activating — Trumpet, Choir, Bird Tweet |
| 3 | Resonant Strings | Challenging — Tubular Bells, Echo Drops |
| 4 | Cyber Flute | Playful — Drawbar Organ, Flute, Bird Tweet |
| 5 | Music Box Orbit | Cinematic — Music Box, Slow Strings |
| 6 | The Great Rite | Calming — Church Organ, Tubular Bells throughout |
| 7 | The Great Rite (Salah's tweak) | Calming with Flutes for Neptune and Pluto |
| 8 | Simplicity | Pure — Tubular Bells throughout, Mars as drum |

**Key design features:**
- **Mars at 396 Hz** is permanently assigned a drumbeat — alternating between Taiko Drum and Melodic Tom — the Tritone pulse that drives the entire composition
- **Harmonia at 540 Hz** sings as a Choir voice — the leading tone, warm and unresolved, present in the mathematics but absent in the Solar System
- Planets build up one by one, then sustain together in full resonance before fading to silence
- The exact planetary frequencies are always preserved regardless of instrument choice

---

## Listening Guide

**For the casual listener:**
Start with `solar_planets_sequential.wav` — hear each planet's frequency individually, from Mercury's deep bass rumble to Pluto's high bright tone. Notice Mars's dissonant Tritone and Harmonia's warm, unresolved leading tone.

**For the full experience:**
Listen to `solar_chord_buildup.wav`. The chord assembles itself over 30 seconds — one planet at a time. At 12 seconds, Harmonia enters at 540 Hz. Feel how the leading tone creates tension toward Jupiter above it — and notice that the tension never resolves. The chord holds, suspended, then fades.

**For the most moving experience:**
Listen to `harmonia_solo.wav` in a quiet room. A single sustained tone at 540 Hz — warm, slightly alive with vibrato, leaning forward. A faint ghost overtone of the Jupiter frequency above it. The sound of a missing note. The sound of a planet that should be there but isn't.

**For an orchestral experience:**
Run `solar_chord_instruments.py` and try Preset 8 — Simplicity — first. Then explore the other presets. Notice how the same planetary frequencies take on completely different emotional characters through different instrument voices — while Mars always drums and Harmonia always sings.

---

## Community Contributions

This folder welcomes extensions and creative interpretations of the planetary frequency framework, provided the exact frequencies of the Silver Ratio Harmonic Framework are preserved:

| Contributor | Script | Description |
|---|---|---|
| Salah-Eddin Gherbi | `solar_chord.py` | Original sine wave generator and frequency map |
| Michiel | `solar_chord_instruments.py` | Orchestral instrument orchestration using FluidSynth |

If you have extended this framework in your own work and would like to contribute, please open a pull request or contact the author.

---

## Connection to the Research

The musical dimension of the Solar chord is **not a claim of the research paper**. The paper makes specific, falsifiable predictions about planetary orbital distances — testable by Gaia DR3+ surveys of the asteroid belt at 2.14 AU and by application to exoplanetary systems.

The musical mapping is an observation that emerges naturally from the framework's mathematics when orbital distances are expressed logarithmically. It is presented as a cultural and aesthetic extension of the research — a way of hearing what the mathematics describes.

The full exploration of this musical dimension — including the digit sum 9 frequency table, the identification of Harmonia as the Major 7th leading tone, and the concept of the Solar Symphony's suspended chord — is developed in the companion article:

**Harmonia — The Missing Note in the Solar Symphony**
Salah-Eddin Gherbi, *The Quantum Blueprint* on Substack, 30 March 2026
[https://salaheddin.substack.com/p/harmonia-the-missing-note-in-the-solar-symphony](https://salaheddin.substack.com/p/harmonia-the-missing-note-in-the-solar-symphony)

---

## Citation

If you use or reference these audio files or the frequency framework in your own work, please cite the companion article and the research paper:

**Article:**
> Gherbi, S.-E. (2026). *Harmonia — The Missing Note in the Solar Symphony.* The Quantum Blueprint, Substack. [https://salaheddin.substack.com/p/harmonia-the-missing-note-in-the-solar-symphony](https://salaheddin.substack.com/p/harmonia-the-missing-note-in-the-solar-symphony)

**Research paper:**
> Gherbi, S.-E. (2026). *The Harmonic Architecture of the Solar System: A Silver-Ratio-Based Hypothesis for Planetary Spacing.* Version 3.0. Zenodo. DOI: [10.5281/zenodo.18816002](https://doi.org/10.5281/zenodo.18816002)

**Book:**
> Gherbi, S.-E. (2026). *Scala Harmonica: The Geometry of Planetary Resonance.* ISBN 978-1-837095-20-9. Available at [salaheddingherbiauthor.com/books](https://salaheddingherbiauthor.com/books)

---

## Licence

This folder is licensed under [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/) — the same licence as the rest of the repository. You may share and adapt this material for non-commercial purposes provided appropriate credit is given.

© 2026 Salah-Eddin Gherbi.

---

*The pattern was always there. The cross was the key.*
