# =============================================================================
# SOLAR CHORD — INSTRUMENT ORCHESTRATION
# Contributed by Michiel (2026)
# Extending the planetary frequency framework of Salah-Eddin Gherbi
# Original frequencies: solar_chord.py by Salah-Eddin Gherbi
# Based on: The Harmonic Architecture of the Solar System (Gherbi, 2026)
# Zenodo DOI: 10.5281/zenodo.18816002
# Article: https://salaheddin.substack.com/p/harmonia-the-missing-note-in-the-solar-symphony
# =============================================================================

import fluidsynth
import time
import math
import os

# Kill any lingering audio processes
os.system('pkill -9 fluidsynth 2>/dev/null')
os.system('pkill -9 pulseaudio 2>/dev/null')
time.sleep(0.5)

# --- 4. Global State ---
drum_toggle = True # Must be top-level for the 'global' keyword to work

PLANET_FREQS = [90, 180, 252, 396, 540, 1305, 2394, 4842, 7605, 9972]
PLANET_NAMES = ["Mercury", "Venus", "Earth", "Mars", "Harmonia", "Jupiter", "Saturn", "Uranus", "Neptune", "Pluto"]

# --- RHYTHM REFERENCE ARRAY ---
# (Strikes, Interval in seconds) 
# 0 = Infinite Sustain | >0 = Number of pulses in a 'burst'
# --- 2. DICTIONARY-BASED RHYTHM ---
# Format: { 0: (Default_Strikes, Interval), Preset_Num: (Override_Strikes, Interval) }
RHYTHM_ATTR = [
    {0: (0, 0.0)}, # 0: Mercury
    {0: (0, 0.0)},              # 1: Venus
    {0: (0, 0.0)},              # 2: Earth
    {0: (0, 0.7)},              # 3: Mars (Infinite Drum)
    {0: (0, 0.0)},              # 4: Harmonia
    {0: (0, 0.0)},              # 5: Jupiter
    {0: (0, 0.0)},              # 6: Saturn
    {0: (0, 0.0)},              # 7: Uranus
    {0:(0, 0), 6: (3, 0.14), 8: (3, 0.14)},             # 8: Neptune
    {0:(0, 0), 6: (5, 0.14), 8: (5, 0.14)} # 9: Pluto (Default 5 hits, but 10 hits in Preset 2)
]

# =============================================================================
# INSTRUMENT REFERENCE LIST (Arachno SoundFont / General MIDI)
# =============================================================================
#  6: Harpsichord      |  10: Glockenspiel   |  11: Music Box      |  14: Tubular Bells
# 16: Drawbar Organ   |  19: Church Organ   |  24: Nylon Guitar   |  40: Violin
# 46: Orchestral Harp |  49: Slow Strings   |  52: Choir Aahs     |  54: Voice Oohs
# 59: Muted Trumpet   |  73: Flute          |  80: Sine Wave      |  89: Warm Pad
# 92: Bowed Glass     |  97: Ice Rain       |  98: Crystal        | 102: Echo Drops
# 116: Taiko Drum     | 117: Melodic Tom    | 123: Bird Tweet
# =============================================================================

PRESETS = {
    1: ("Ethereal Balance (intense)", [19, 97, 10, 116, 52, 49, 73, 123, 46, 80]),
    2: ("Pluto's Song (activating)",     [19, 59, 97, 116, 54, 80, 80, 80, 24, 123]),
    3: ("Resonant Strings (challenging)", [19, 14, 10, 116, 52, 49, 102, 123, 80, 14]),
    4: ("Cyber Flute (funny bird)",      [16, 59, 97, 117, 52, 80, 73, 102, 123, 46]),
    5: ("Music Box Orbit (cinematic)",  [19, 97, 97, 116, 52, 11, 80, 123, 49, 80]),
    6: ("The Great Rite (calming)",   [19, 59, 10, 116, 52, 14, 14, 14, 14, 14]),
    7: ("The Great Rite (Salah's tweak)",   [19, 59, 10, 116, 52, 14, 14, 14, 73, 75]), # Neptune/Pluto swapped to Flutes
    8: ("Simplicity",   [14, 14, 14, 116, 52, 14, 14, 14, 14, 14])
}

# Salah's Volume Scaling to make high frequencies audible
VOLUME_BOOST = {
    "Uranus": 1.4,
    "Neptune": 1.6, 
    "Pluto": 1.8
}

def get_rhythm(planet_idx, preset_choice):
    """Checks for a preset-specific rhythm, otherwise returns the default (0)."""
    planet_dict = RHYTHM_ATTR[planet_idx]
    return planet_dict.get(preset_choice, planet_dict[0])

def get_midi_params(freq):
    midi_float = 69 + 12 * math.log2(freq / 440.0)
    midi_note = int(round(midi_float))
    deviation_cents = (midi_float - midi_note) * 100
    bend_value = int(8192 + (deviation_cents * 40.96))
    return midi_note, bend_value
   
def play_exact_freq(fs, channel, freq, velocity=70):
    name = PLANET_NAMES[channel]
    # Apply Salah's volume boost if the planet is in the list
    boost = VOLUME_BOOST.get(name, 1.0)
    final_velocity = min(int(velocity * boost), 127) # Cap at MIDI max 127
    
    note, bend = get_midi_params(freq)
    fs.pitch_bend(channel, bend)
    fs.noteon(channel, note, final_velocity)

def silence_system(fs):
    for chan in range(16):
        fs.cc(chan, 123, 0)
        fs.cc(chan, 120, 0)
        fs.cc(chan, 7, 100)
    time.sleep(0.3)

# --- Engine Setup ---
fs = fluidsynth.Synth()
fs.start(driver="pulseaudio")
sfid = fs.sfload("Arachno.sf2")

print(f"✓ SoundFont loaded: Arachno.sf2 (ID: {sfid})")

def perform():
    print("\n" + "="*40 + "\n      PLANET FREQUENCY PLAY \n" + "="*40)
    print("Based on: Gherbi, S.-E. (2026). Harmonia — The Missing Note in the Solar Symphony. The Quantum Blueprint, Substack. https://salaheddin.substack.com/p/harmonia-the-missing-note-in-the-solar-symphony")
    print("and: Gherbi, S.-E. (2026). The Harmonic Architecture of the Solar System: A Silver-Ratio-Based Hypothesis for Planetary Spacing. Version 3.0. Zenodo. DOI: 10.5281/zenodo.18816002")
    for num, (name, _) in PRESETS.items():
        print(f" {num}: {name}")
    print(" 0: Exit Program")
    
    try:
        choice = int(input("\nSelect a preset: "))
        if choice == 0: return False
        selected_name, program_list = PRESETS[choice]
    except (ValueError, KeyError): return True
    
    # --- RESET THE STATE FOR THE NEW SESSION ---
    last_trigger_times = [0.0] * 10
    strikes_done_list = [0] * 10  # <--- This is the key reset!
    active_planets = []
    # -------------------------------------------
    
    print(f"\n>>> Orchestrating: {selected_name}")

    # 1. Build-up Phase
    for i, prog in enumerate(program_list):
        fs.program_select(i, sfid, 0, prog)
        active_planets.append(i)
        
        # Determine rhythm for drone check
        max_s, inter = get_rhythm(i, choice)
        if max_s == 0 and inter == 0:
            play_exact_freq(fs, i, PLANET_FREQS[i])
            
        print(f"  + {PLANET_NAMES[i]:9s} | {PLANET_FREQS[i]:5.1f} Hz")

        # Wait 1.3s for next planet, but process rhythmic pulses for all active planets
        entry_start = time.time()
        while (time.time() - entry_start) < 1.3:
            process_rhythms(active_planets, last_trigger_times, strikes_done_list, sfid, choice)
            time.sleep(0.01)

    # 2. Main Sustain Phase
    print("\nFull Resonance...")
    sustain_start = time.time()
    while (time.time() - sustain_start) < 7.0:
        process_rhythms(active_planets, last_trigger_times, strikes_done_list, sfid, choice)
        time.sleep(0.01)

    # Fade Out
    print("Closing...")
    for vol in range(100, -1, -10):
        for chan in range(10): fs.cc(chan, 7, vol)
        time.sleep(0.1)
    
    silence_system(fs)
    return True

def process_rhythms(active_indices, last_times, strikes_done_list, sfid, preset_choice):
    global drum_toggle

    now = time.time()
    
    for i in active_indices:
        # Pull rhythm based on current preset choice
        max_strikes, interval = get_rhythm(i, preset_choice)
        
        # 1. Rhythmic Check (Skip Drones)
        if interval > 0:
            # 2. Trigger if interval passed AND (it's Mars OR we haven't hit the limit)
            if (now - last_times[i]) > interval and (i == 3 or strikes_done_list[i] < max_strikes):
 
                last_times[i] = now                
 
                # 3. MARS SPECIAL: Alternating Drum
                if i == 3:
                    # Toggle between 116 (Taiko) and 117 (Tom)
                    fs.program_select(3, sfid, 0, 116 if drum_toggle else 117)
                    drum_toggle = not drum_toggle
                    play_exact_freq(fs, 3, PLANET_FREQS[3], velocity=95)
                
                # 4. OTHERS: Standard Strike
                else:
                    play_exact_freq(fs, i, PLANET_FREQS[i], velocity=85)
                    # Increment counter for everyone EXCEPT Mars
                    strikes_done_list[i] += 1

try:
    while perform(): pass
except KeyboardInterrupt: pass

fs.delete()
print("\nSee you soon.")
