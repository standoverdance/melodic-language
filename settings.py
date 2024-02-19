# Libraries made based on melodic language documentation table
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
}}
CIPHER_REPRESENTATION = {
    'eariot': 'e',
    'tuxvy': 't'
}
INTRODUCTION = {   # Notice! Introduction words must be capitalized.
    'e': 'TSLN',
    't': 'SPDN'
}
RESET_WORDS = {  # Reset words also needs to be capitalized
    'e': 'RAAR',
    't': 'EAO'
}
# Language Settings;
INTRODUCE = True  # If you want to include introduction word in translation
RESET_BOOL = True  # If you want to include reset words in translation

# Singer settings:
MAX_range = 95
MIN_range = 32
STARTING_NOTE = 60
NOTE_DURATION = 500 # Duration of each note in miliseconds