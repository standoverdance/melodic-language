from mido import MidiFile, MidiTrack, Message
from settings import *

# Singer setup
input_var = input("Translate to the song:")
text = input_var.upper()
chosen_lang = input(f"Chose a language:{CIPHER_REPRESENTATION}")  # Library selection


class Song:
    def __init__(self, str_input, chosen_language, min_range, max_range, starting_note=60):
        self.input = str_input.upper()
        self.lang = chosen_language
        self.min_range = min_range
        self.max_range = max_range
        self.starting_note = starting_note

    def to_cipher(self):
        cipher = []
        lang_found = False
        space_positions = [index for index, char in enumerate(self.input) if char.isspace()]
        for language in CIPHER_REPRESENTATION:
            if self.lang == CIPHER_REPRESENTATION[language]:
                dictionary = MELODIC_CIPHERS[language]  # Sets a dictionary from settings
                if INTRODUCE:
                    for letter in INTRODUCTION[self.lang]:
                        cipher.append(dictionary[letter])
                    cipher.append(332)
                lang_found = True
                
        if not lang_found:
            print(f"{self.lang} is not an option")
            exit()
        else:
            for index, letter in enumerate(self.input):
                if letter in dictionary: cipher.append(dictionary[letter])
                elif index in space_positions: cipher.append(332)  # 332 is a space/pause
        
        reset_cipher = []
        if RESET_BOOL:
            for letter in RESET_WORDS[self.lang]:
                reset_cipher.append(dictionary[letter])
            
        return cipher, reset_cipher

    def semitone_director(self):
        cipher = self.to_cipher()[0]
        reset_cipher = self.to_cipher()[1]
        directed = []
        directed_reset = []
        for number in cipher:
            if number == 1: directed.append(0)  # Instance with no semitones - note with the same pitch
            elif number == 332: directed.append(332)  # Number symbolizing pause
            elif number % 2 == 0: directed.append(number + 100)  # Even numbers go up. (look at the semitones in language docs)
            elif number % 2 != 0: directed.append(number + 200)  # Odd numbers go down.
        
        for number in reset_cipher:
            if number == 1: directed_reset.append(0)
            elif number == 332: directed_reset.append(332)
            elif number % 2 == 0: directed_reset.append(number + 100)
            elif number % 2 != 0: directed_reset.append(number + 200)
            
        return directed, directed_reset
    
    def complete_midi_list(self):
        directed = self.semitone_director()[0]
        directed_reset = self.semitone_director()[1]
        noting = self.starting_note
        notes = [self.starting_note]
        
        for number in directed:  # Loop to convert directed to midi notes
            if number == 0: notes.append(noting)
            elif number < 200:
                noting = int(noting + (number - 100)/2)
                notes.append(noting)
            elif number > 200 and number != 332:
                noting = int(noting - (number - 201)/2)
                notes.append(noting)
            else: notes.append(332)
            
            if noting > self.max_range:
                noting = self.starting_note
                notes.append(noting)
                if RESET_BOOL:
                    for num_reset in directed_reset:
                        if num_reset == 0:
                            notes.append(noting)
                        elif num_reset < 200:
                            noting = int(noting + (num_reset - 100) / 2)
                            notes.append(noting)
                        elif num_reset > 200 and num_reset != 332:
                            noting = int(noting - (num_reset - 201) / 2)
                            notes.append(noting)
                        else:
                            notes.append(332)
                        
            elif noting < self.min_range:
                noting = self.starting_note
                notes.append(noting)
                if RESET_BOOL:
                    for num_reset in directed_reset:
                        if num_reset == 0:
                            notes.append(noting)
                        elif num_reset < 200:
                            noting = int(noting + (num_reset - 100) / 2)
                            notes.append(noting)
                        elif num_reset > 200 and num_reset != 332:
                            noting = int(noting - (num_reset - 201) / 2)
                            notes.append(noting)
                        else:
                            notes.append(332)
        return notes
    
    def complete_chord_list(self):
        melody = self.complete_midi_list()
        sheet = []
        total = 0
        count = 0
        setter = False
        for i, notes in enumerate(melody):
            if notes != 332:
                if setter == False:
                    sheet.append(notes)
                    sheet.append(notes + 7)
                    setter = True
                total += notes
                count += 1
            if notes == 332 or i == len(melody) - 1:
                average = total / count
                sheet.append(round(average))
                sheet.append(count + 400)
                total = 0
                count = 0
                setter = 0
        
        return sheet
        
        
my_song = Song(input_var, chosen_lang, MIN_range, MAX_range, STARTING_NOTE)


def sing(melody, duration=1, velocity=64, output_file='output.mid'):
    track = MidiTrack()
    
    for note in melody:
        if note != 332:
            track.append(Message('note_on', note=note, velocity=velocity, time=0))
            track.append(Message('note_off', note=note, velocity=velocity, time=duration))
        if note == 332:  # Adds a ghost note during pause
            track.append(Message('note_on', note=1, velocity=0, time=0))
            track.append(Message('note_off', note=1, velocity=0, time=duration))

    midi_file = MidiFile()
    midi_file.tracks.append(track)
    
    # Save
    midi_file.save(output_file)


def accompaniment(chords, duration=1, velocity=64, output_file='output.mid'):
    track = MidiTrack()

    chord_list = []
    chord_end = False
    for note in chords:
        if note < 400:
            if chord_end == True:
                # Pause before placing note
                track.append(Message('note_on', note=note, velocity=velocity, time=duration))
                chord_end = False
            else:
                track.append(Message('note_on', note=note, velocity=velocity, time=0))
            chord_list.append(note)
        elif note >= 400:
            stack = note - 400
            chord_duration = duration * stack
            for i, sound in enumerate(chord_list):
                if i == 0:
                    track.append(Message('note_off', note=sound, velocity=velocity, time=chord_duration))
                else:
                    track.append(Message('note_off', note=sound, velocity=velocity, time=0))
            chord_list = []
            chord_end = True
    midi_file = MidiFile()
    midi_file.tracks.append(track)
    
    # Save
    midi_file.save(output_file)
    
    
sing(my_song.complete_midi_list(), duration=NOTE_DURATION, output_file='melody.mid')
accompaniment(my_song.complete_chord_list(), duration=NOTE_DURATION, output_file='chords.mid')

# Debug
# print(my_song.complete_midi_list())
# print(my_song.complete_chord_list())
