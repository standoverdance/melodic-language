# Libraries made based on repository's readme.md letter numbers
MELODIC_CIPHERS = {   # Notice! Library of a cipher has to have capitalized letters
    'eariot': {
    "E": 1, "A": 2, "R": 3, "I": 4, "O": 5, "T": 6, "N": 7, "S": 8,
    "L": 9, "C": 10, "U": 11, "D": 12, "P": 13, "M": 14, "H": 15,
    "G": 16, "B": 17, "F": 18, "Y": 19, "W": 20, "K": 21, "Q": 21,
    "V": 22, "X": 23, "Z": 24, "J": 25
}, 'tuxvy':{
    "O": 1, "K": 2, "Q": 2, "W": 3, "B": 4, "G": 5, "P": 6, "D": 7, "S": 8,
    "N": 9, "E": 10, "A": 11, "J": 12, "Z": 13, "I": 14, "R": 15,
    "L": 16, "C": 17, "M": 18, "H": 19, "F": 20, "Y": 21,
    "V": 22, "X": 23, "U": 24, "T": 25
}, 'etaoin': { # Based on Wikipedia's Robert Lewand's frequency string. (Like Eariot but different)
    "E": 1, "T": 2, "A": 3, "O": 4, "I": 5, "N": 6, "S": 7, "H": 8,
    "R": 9, "D": 10, "L": 11, "C": 12, "U": 13, "M": 14, "W": 15,
    "F": 16, "G": 17, "Y": 18, "P": 19, "B": 20, "V": 21, "K": 22,
    "Q": 22, "J": 23, "X": 24, "Z": 25
}, 'eotha': { # Based on Wikipedia's frequency of letters in bible (Very similar to Etaoin)
    "E": 1, "O": 2, "T": 3, "H": 4, "A": 5, "S": 6, "I": 7, "N": 8,
    "R": 9, "D": 10, "L": 11, "U": 12, "Y": 13, "M": 14, "W": 15,
    "F": 16, "G": 17, "C": 18, "B": 19, "P": 20, "K": 21, "Q": 21,
    "V": 22, "J": 23, "X": 24, "Z": 25}}
CIPHER_REPRESENTATION = {
    'eariot': 'e',
    'tuxvy': 't',
    'etaoin': 'et',
    'eotha': 'eo'
}
INTRODUCTION = {   # Notice! Introduction words must be capitalized.
    'e': 'TSLN',
    't': 'SPDN',
    'et': 'HHRR',
    'eo': 'SSII'
}
RESET_WORDS = {  # Reset words also needs to be capitalized
    'e': 'RAAR',
    't': 'EAO',
    'et': 'ETER',
    'eo': 'ETER'
}
# Language Settings;
INTRODUCE = False  # If you want to include introduction word in translation
RESET_BOOL = False  # If you want to include reset words in translation

# Singer settings:
MAX_range = 95 # Based on MIDI notes numbers chart
MIN_range = 32 # MIDI notes numbers chart
STARTING_NOTE = 60 # MIDI notes numbers chart
NOTE_DURATION = 500 # Duration of each note in miliseconds
