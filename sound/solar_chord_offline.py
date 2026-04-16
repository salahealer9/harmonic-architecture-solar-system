# =============================================================================
# SOLAR CHORD — OFFLINE MIDI RENDER VERSION
# Writes a .mid file per preset, then renders it to WAV via fluidsynth.
# =============================================================================
#
# Requires: pip install mido
# Requires: fluidsynth on PATH, Arachno.sf2 in current directory
# Optional: ffmpeg (for MP3 conversion)
# =============================================================================

import subprocess
import math
import os
import sys

try:
    import mido
except ImportError:
    print("!! This script needs mido:  pip install mido")
    sys.exit(1)

# --- Config ---
OUTPUT_DIR = "recordings"
SOUNDFONT = "Arachno.sf2"
SAMPLE_RATE = 44100
CONVERT_TO_MP3 = True
KEEP_MIDI = True                 # keep the .mid files next to the .wav

# --- Musical Data ---
PLANET_FREQS = [90, 180, 252, 396, 540, 1305, 2394, 4842, 7605, 9972]
PLANET_NAMES = ["Mercury", "Venus", "Earth", "Mars", "Harmonia",
                "Jupiter", "Saturn", "Uranus", "Neptune", "Pluto"]

RHYTHM_ATTR = [
    {0: (0, 0.0)},
    {0: (0, 0.0)},
    {0: (0, 0.0)},
    {0: (0, 0.7)},
    {0: (0, 0.0)},
    {0: (0, 0.0)},
    {0: (0, 0.0)},
    {0: (0, 0.0)},
    {0:(0, 0), 6: (3, 0.14), 8: (3, 0.14)},
    {0:(0, 0), 6: (5, 0.14), 8: (5, 0.14)}
]

PRESETS = {
    1: ("Ethereal Balance (intense)", [19, 97, 10, 116, 52, 49, 73, 123, 46, 80]),
    2: ("Pluto's Song (activating)",   [19, 59, 97, 116, 54, 80, 80, 80, 24, 123]),
    3: ("Resonant Strings (challenging)", [19, 14, 10, 116, 52, 49, 102, 123, 80, 14]),
    4: ("Cyber Flute (funny bird)",    [16, 59, 97, 117, 52, 80, 73, 102, 123, 46]),
    5: ("Music Box Orbit (cinematic)", [19, 97, 97, 116, 52, 11, 80, 123, 49, 80]),
    6: ("The Great Rite (calming)",    [19, 59, 10, 116, 52, 14, 14, 14, 14, 14]),
    7: ("The Great Rite (Salah's tweak)", [19, 59, 10, 116, 52, 14, 14, 14, 73, 75]),
    8: ("Simplicity",                  [14, 14, 14, 116, 52, 14, 14, 14, 14, 14])
}

VOLUME_BOOST = {"Uranus": 1.4, "Neptune": 1.6, "Pluto": 1.8}

# Timing constants (formerly time.sleep durations)
BUILD_UP_DUR   = 1.3     # seconds each instrument takes to enter
SUSTAIN_DUR    = 15.0    # main resonance
FADE_STEPS     = 11      # 100, 90, ..., 0
FADE_STEP_DUR  = 0.1     # each fade step
TOTAL_FADE_DUR = FADE_STEPS * FADE_STEP_DUR

# MIDI tempo: we'll use 1 tick = 1 millisecond so time math is easy
TICKS_PER_BEAT = 480
TEMPO_BPM      = 125     # 480 ticks/beat * 125 bpm / 60 = 1000 ticks/sec = 1 ms/tick
MICROSECONDS_PER_BEAT = int(60_000_000 / TEMPO_BPM)

def seconds_to_ticks(seconds):
    return int(round(seconds * 1000))   # 1 tick = 1 ms

# =============================================================================
# MIDI EVENT BUILDER
# =============================================================================

class MidiBuilder:
    """Collects absolute-time MIDI events, then writes a sorted .mid file."""

    def __init__(self):
        # List of (abs_tick, channel, mido.Message)
        self.events = []
        # Also track program-changes-per-channel for reset
        self.meta_events = []

    def add(self, abs_tick, msg):
        self.events.append((abs_tick, msg))

    def set_instrument(self, abs_tick, channel, program):
        self.add(abs_tick, mido.Message('program_change',
                                        channel=channel, program=program))

    def note_on(self, abs_tick, channel, note, velocity):
        self.add(abs_tick, mido.Message('note_on',
                                        channel=channel, note=note,
                                        velocity=velocity))

    def note_off(self, abs_tick, channel, note):
        self.add(abs_tick, mido.Message('note_off',
                                        channel=channel, note=note, velocity=0))

    def pitch_bend(self, abs_tick, channel, value):
        # mido expects pitch in -8192..8191
        pitch = max(-8192, min(8191, value - 8192))
        self.add(abs_tick, mido.Message('pitchwheel',
                                        channel=channel, pitch=pitch))

    def cc(self, abs_tick, channel, controller, value):
        self.add(abs_tick, mido.Message('control_change',
                                        channel=channel, control=controller,
                                        value=value))

    def write(self, path):
        mid = mido.MidiFile(ticks_per_beat=TICKS_PER_BEAT)
        track = mido.MidiTrack()
        mid.tracks.append(track)

        # Tempo at tick 0
        track.append(mido.MetaMessage('set_tempo',
                                      tempo=MICROSECONDS_PER_BEAT, time=0))

        # Stable sort by absolute tick — preserves insertion order for ties,
        # which matters for things like program_change before note_on.
        sorted_events = sorted(self.events, key=lambda e: e[0])

        prev_tick = 0
        for abs_tick, msg in sorted_events:
            delta = abs_tick - prev_tick
            if delta < 0:
                delta = 0
            msg.time = delta
            track.append(msg)
            prev_tick = abs_tick

        # Small end-of-track pad so fluidsynth doesn't cut release tails
        track.append(mido.MetaMessage('end_of_track', time=1000))

        mid.save(path)

# =============================================================================
# FREQ → MIDI
# =============================================================================

def get_rhythm(planet_idx, preset_choice):
    return RHYTHM_ATTR[planet_idx].get(preset_choice, RHYTHM_ATTR[planet_idx][0])

def get_midi_params(freq):
    midi_float = 69 + 12 * math.log2(freq / 440.0)
    midi_note = int(round(midi_float))
    deviation_cents = (midi_float - midi_note) * 100
    bend_value = int(8192 + (deviation_cents * 40.96))
    return midi_note, bend_value

def boosted_velocity(channel, velocity):
    name = PLANET_NAMES[channel]
    boost = VOLUME_BOOST.get(name, 1.0)
    return min(int(velocity * boost), 127)

# =============================================================================
# PRESET → MIDI COMPOSITION
# =============================================================================

def compose_preset(choice, program_list):
    """Build a MidiBuilder with all events for this preset, then return it."""
    mb = MidiBuilder()

    # Track currently-held notes per channel for clean note_off at the end
    held_notes = {}  # channel -> list of (note, off_tick)
    drum_toggle = True

    # Each channel gets an initial volume of 100 (matches original)
    for chan in range(10):
        mb.cc(0, chan, 7, 100)

    # ---- Build-up phase: instrument i enters at tick = i * BUILD_UP_DUR ----
    active_planets = []
    for i, prog in enumerate(program_list):
        entry_tick = seconds_to_ticks(i * BUILD_UP_DUR)
        # Program change slightly before the note so fluidsynth applies it
        mb.set_instrument(entry_tick - 1 if entry_tick > 0 else 0, i, prog)
        active_planets.append(i)

        max_s, inter = get_rhythm(i, choice)
        if max_s == 0 and inter == 0:
            # Sustained note — starts here, will be turned off at the very end
            note, bend = get_midi_params(PLANET_FREQS[i])
            vel = boosted_velocity(i, 70)
            mb.pitch_bend(entry_tick, i, bend)
            mb.note_on(entry_tick, i, note, vel)
            held_notes.setdefault(i, []).append(note)

    # ---- Rhythmic layer ----
    # For each active planet with interval > 0, schedule strikes across
    # the full build-up + sustain window.
    buildup_end   = seconds_to_ticks(len(program_list) * BUILD_UP_DUR)
    sustain_end   = buildup_end + seconds_to_ticks(SUSTAIN_DUR)
    rhythm_window_end = sustain_end  # stop striking when fade begins

    for i in active_planets:
        max_strikes, interval = get_rhythm(i, choice)
        if interval <= 0:
            continue

        entry_tick = seconds_to_ticks(i * BUILD_UP_DUR)
        interval_ticks = seconds_to_ticks(interval)
        t = entry_tick + interval_ticks
        strikes_done = 0

        # Per-strike note duration (short percussive hit)
        strike_len = seconds_to_ticks(0.12)

        while t < rhythm_window_end:
            # Mars (channel 3) toggles between programs 116/117 each hit
            if i == 3:
                prog = 116 if drum_toggle else 117
                drum_toggle = not drum_toggle
                mb.set_instrument(t - 1, 3, prog)
                note, bend = get_midi_params(PLANET_FREQS[3])
                vel = boosted_velocity(3, 95)
                mb.pitch_bend(t, 3, bend)
                mb.note_on(t, 3, note, vel)
                mb.note_off(t + strike_len, 3, note)
            else:
                if strikes_done >= max_strikes:
                    break
                note, bend = get_midi_params(PLANET_FREQS[i])
                vel = boosted_velocity(i, 85)
                mb.pitch_bend(t, i, bend)
                mb.note_on(t, i, note, vel)
                mb.note_off(t + strike_len, i, note)
                strikes_done += 1

            t += interval_ticks

    # ---- Fade-out ----
    fade_start = sustain_end
    for step, vol in enumerate(range(100, -1, -10)):
        step_tick = fade_start + seconds_to_ticks(step * FADE_STEP_DUR)
        for chan in range(10):
            mb.cc(step_tick, chan, 7, vol)

    # ---- End: note_off for any sustained notes ----
    end_tick = fade_start + seconds_to_ticks(TOTAL_FADE_DUR) + 100
    for chan, notes in held_notes.items():
        for note in notes:
            mb.note_off(end_tick, chan, note)
        # All notes off + all sound off
        mb.cc(end_tick + 10, chan, 123, 0)
        mb.cc(end_tick + 10, chan, 120, 0)

    return mb, end_tick

# =============================================================================
# RENDER
# =============================================================================

def render_midi_to_wav(midi_path, wav_path):
    """Call fluidsynth as a one-shot renderer."""
    cmd = [
        "fluidsynth",
        "-ni",
        "-F", os.path.abspath(wav_path),
        "-r", str(SAMPLE_RATE),
        SOUNDFONT,
        midi_path,
    ]
    print(f"  [RENDER] {' '.join(cmd)}")
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"  !! fluidsynth returned {result.returncode}")
        print(f"  stderr: {result.stderr[:500]}")
        return False
    return True

def convert_to_mp3(wav_path):
    mp3_path = wav_path.rsplit('.', 1)[0] + '.mp3'
    try:
        subprocess.run(
            ["ffmpeg", "-y", "-i", wav_path, "-codec:a", "libmp3lame",
             "-b:a", "192k", mp3_path],
            check=True, capture_output=True
        )
        print(f"  [MP3] Saved {mp3_path}")
    except FileNotFoundError:
        print("  [MP3] ffmpeg not found — skipping")
    except subprocess.CalledProcessError as e:
        print(f"  [MP3] Failed: {e.stderr.decode()[:200]}")

def safe_filename(s):
    keep = "-_. "
    return "".join(c if c.isalnum() or c in keep else "_" for c in s).strip().replace(" ", "_")

# =============================================================================
# DRIVER
# =============================================================================

def run_preset(choice, name, program_list):
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    base = f"preset_{choice}_{safe_filename(name)}"
    midi_path = os.path.join(OUTPUT_DIR, base + ".mid")
    wav_path  = os.path.join(OUTPUT_DIR, base + ".wav")

    print(f"\n>>> Composing: {name}")
    mb, end_tick = compose_preset(choice, program_list)
    print(f"  Duration: {end_tick/1000:.2f}s  ({len(mb.events)} events)")
    mb.write(midi_path)
    print(f"  [MIDI] {midi_path}")

    print(f"  [WAV]  Rendering...")
    ok = render_midi_to_wav(midi_path, wav_path)
    if ok and os.path.exists(wav_path):
        size_kb = os.path.getsize(wav_path) / 1024
        print(f"  [WAV]  ✓ {wav_path} ({size_kb:.1f} KB)")
        if CONVERT_TO_MP3:
            convert_to_mp3(wav_path)
    else:
        print(f"  [WAV]  !! render failed")

    if not KEEP_MIDI:
        try:
            os.remove(midi_path)
        except OSError:
            pass

def menu():
    print("\n" + "="*40 + "\n     PLANET FREQUENCY RENDER\n" + "="*40)
    print("Based on: Gherbi, S.-E. (2026). Harmonia — The Missing Note in the Solar Symphony.")
    print(f"Output folder: ./{OUTPUT_DIR}/")
    for num, (name, _) in PRESETS.items():
        print(f" {num}: {name}")
    print(" 99: Render ALL presets")
    print(" 0: Exit")

    try:
        choice = int(input("\nSelect: "))
    except ValueError:
        return True

    if choice == 0:
        return False
    if choice == 99:
        for c, (name, progs) in PRESETS.items():
            run_preset(c, name, progs)
        return True
    if choice in PRESETS:
        name, progs = PRESETS[choice]
        run_preset(choice, name, progs)
    return True

if __name__ == "__main__":
    if not os.path.exists(SOUNDFONT):
        print(f"!! SoundFont not found: {SOUNDFONT}")
        sys.exit(1)
    try:
        while menu():
            pass
    except KeyboardInterrupt:
        pass
    print("\nSee you soon.")
